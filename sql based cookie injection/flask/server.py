from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import MySQLdb

app = Flask(__name__)

app.config['SECRET_KEY'] = 'EWuuMqhcZU2j85BQ'

bootstrap = Bootstrap(app)

# TODO make connection more robust so it reconnects on disconnect?
# TODO test app extensively with automated scanners like sqlmap?
# TODO test how robust app is installed as service
# TODO run service as restricted user?
# TODO log sth of waitress service to file?

db = MySQLdb.connect(host="localhost", port= 3306, user="flask", passwd="v5UmnxifRv", db="flask")
# db = _mysql.connect(host="172.28.222.152", port= 3000, user="flask", passwd="v5UmnxifRv", db="flask")


class DBQueryForm(FlaskForm):
    # deactivate csrf
    class Meta:
        csrf = False
    query = StringField('Search for our available yummy products :)')
    submit = SubmitField('Submit')
    


def query_db(query: str) -> list:
    # possible injection to display all products:
    #            %' or 'a'='a'; --
    try:
        query = """SELECT imagefile FROM products where lower(productname) like '%{}%'""".format(query)
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        result_list = list()
        for element in result:
            result_list.append(element[0])
    except Exception:
        result_list = ["Stop it script kiddy"]

    return result_list
    


@app.route('/', methods=['GET', 'POST'])
def index():
    result_list = None
    form = DBQueryForm()
    # only do sth when there is a filename given!
    if form.validate_on_submit():
        if form.query.data != "":
            result_list = query_db(form.query.data)
        #form.filename.data = ''        
    return render_template('index.html', form=form, result_list=result_list)

if __name__ == "__main__":
    app.run()


# windows: set FLASK_APP=server.py
# linux: export FLASK_APP=server.py
# flask run -p 6666
# only available on unix: gunicorn --bind 127.0.0.1:6666 server:app
# curl -X POST -d "tablename=flag&submit=Submit" http://localhost:6666