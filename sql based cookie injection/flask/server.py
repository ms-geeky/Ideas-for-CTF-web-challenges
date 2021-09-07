from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import platform
import subprocess
import random
import base64
import codecs
from MySQLdb import _mysql

app = Flask(__name__)

app.config['SECRET_KEY'] = 'EWuuMqhcZU2j85BQ'

bootstrap = Bootstrap(app)

encodings_set = {"base64","rot13", "hex", "binary"}



class MagicForm(FlaskForm):
    # deactivate csrf
    class Meta:
        csrf = False
    filename = StringField('Enter filename')
    submit = SubmitField('Submit')
    
def detect_os() -> str:
    return platform.system()

def binary_encode(filecontent: str) -> str:
    result = ' '.join(format(ord(x), 'b') for x in filecontent)
    return result

def hex_encode(filecontent: str) -> str:    
    result = filecontent.encode("utf-8").hex()
    return result

def rot13_encode(filecontent: str) -> str:    
    result = codecs.encode(filecontent, "rot-13")
    return result

def base64_encode(filecontent: str) -> str:
    filecontent_bytes = filecontent.encode('ascii')
    base64_bytes = base64.b64encode(filecontent_bytes)
    result = base64_bytes.decode('ascii')
    return result

def encode_randomly(filecontent: str) -> str:
    func = random.choice(tuple(encodings_set))
    result = ""
    if func == "base64":
        result = base64_encode(filecontent)
    if func == "rot13":
        result = rot13_encode(filecontent)
    if func == "hex":
        result = hex_encode(filecontent)
    if func == "binary":
        result = binary_encode(filecontent)
    return result

def get_filecontent(filename: str) -> str:
    os = detect_os()
    process_name = ""
    if os == "Linux":
        process_name = "cat"
        result = subprocess.check_output([process_name, filename])
    if os == "Windows":
        process_name = "type"
        result = subprocess.check_output([process_name, filename], shell=True)    
    utf8decoded_result = result.decode('UTF-8') 
    randomly_encoded = encode_randomly(utf8decoded_result)
    return randomly_encoded
    


@app.route('/', methods=['GET', 'POST'])
def index():
    filecontent = None
    form = MagicForm()
    # only do sth when there is a filename given!
    if form.validate_on_submit():
        if form.filename.data != "":
            filecontent = get_filecontent(form.filename.data)
        #form.filename.data = ''        
    return render_template('index.html', form=form, filecontent=filecontent)

if __name__ == "__main__":
    app.run()

    #db = _mysql.connect(host="localhost", user="flask", passwd="v5UmnxifRv", db="flask")
    #query = db.query("""SELECT * FROM flag""")
    #query_result = db.store_result()
    #print(query_result.fetch_row())

# windows: set FLASK_APP=magiccat.py
# linux: export FLASK_APP=magiccat.py
# flask run -p 6666
# only available on unix: gunicorn --bind 127.0.0.1:6666 magiccat:app
# curl -X POST -d "filename=file.txt&submit=Submit" http://localhost:6666