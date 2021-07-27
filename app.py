from flask import Flask,render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dba@localhost:5433/sampledb'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'cairocoders-ednalan'
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


class Student(db.Model):
    __tablename__ = 'students2'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    email = db.Column(db.String(40))
    profile_pic = db.Column(db.String(150))

    def __init__(self,fname,lname,email,profile_pic):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.profile_pic = profile_pic

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['inputFile']
    fname = request.form['fname']
    lname = request.form['lname']
    filename = secure_filename(file.filename)

    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        newFile = Student(profile_pic=file.filename, fname=fname, lname=lname, email='skillchen@gmail.com')
        db.session.add(newFile)
        db.session.commit()
        flash("File successfully uploaded " + file.filename + " !")
        return redirect("/")
    else:
        flash('Invalid Upload only txt, pdf, png, jpg, jpeg, gif')


    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)