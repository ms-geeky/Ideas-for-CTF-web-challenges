from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from MySQLdb import _mysql

app = Flask(__name__)

app.config['SECRET_KEY'] = 'EWuuMqhcZU2j85BQ'

bootstrap = Bootstrap(app)

# TODO make connection more robust so it reconnects on disconnect?
db = _mysql.connect(host="localhost", user="flask", passwd="v5UmnxifRv", db="flask")

class DBQueryForm(FlaskForm):
    # deactivate csrf
    class Meta:
        csrf = False
    query = StringField('Enter tablename')
    submit = SubmitField('Submit')
    


def query_db(query: str) -> str:

    try:
        query = db.query("""SELECT * FROM {}""".format(query))
        query_result = db.store_result()
        result = query_result.fetch_row()
    except Exception:
        result = "Stop it script kiddy"

    return str(result)
    


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    form = DBQueryForm()
    # only do sth when there is a filename given!
    if form.validate_on_submit():
        if form.query.data != "":
            result = query_db(form.query.data)
        #form.filename.data = ''        
    return render_template('index.html', form=form, result=result)

if __name__ == "__main__":
    app.run()


# windows: set FLASK_APP=server.py
# linux: export FLASK_APP=server.py
# flask run -p 6666
# only available on unix: gunicorn --bind 127.0.0.1:6666 server:app
# curl -X POST -d "tablename=flag&submit=Submit" http://localhost:6666