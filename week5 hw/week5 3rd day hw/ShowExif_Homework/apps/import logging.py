import logging
from apps import app
from flask import Flask, render_template, request, url_for
from PIL import Image
from PIL.ExifTags import TAGS
from StringIO import StringIO

from google.appengine.ext import db
from member import Member

class Photo(db.Model):
    photo = db.BlobProperty()

ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg', 'gif']


def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    fileinfo = {}
    try:
        img = Image.open(fname)
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            print exifinfo
            if exifinfo != None:
                fileinfo = dict([(TAGS.get(key,key), str(value).decode('utf-8', 'ignore'))
                        for key, value in exifinfo.items()
                        if type(TAGS.get(key,key)) is str])
    except IOError:
        logging.error(fname)
    return fileinfo


def allowed_file(filename):
    return '.' in filename.lower() and \
           filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

id_db = {}

# login.html
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        given_id = request.form['id']
        given_pw = request.form['pw']

        if given_pw == id_db[given_id]:
            return render_template('index.html', given_id = given_id)
        else:
            comment = "Please, check your ID and password again!"
            return render_template('login.html', comment = comment)

    return render_template('login.html')

# join.html
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        new_account = Member()
        new_id = request.form['nid']
        new_pw = request.form['npw']
        re_pw = request.form['rpw']

        if new_pw == re_pw and new_id not in id_db:
            new_account.set(new_id, new_pw)
            id_db[new_account.get_id()] = new_account.get_pw()
            comment = "Congrats! You've made a new ID"
        elif new_pw != re_pw:
            comment = "Please, check your password!"
        elif new_id in id_db:
            comment = "Please, use another ID"

        return render_template('join.html', comment = comment)
    return render_template('join.html')

# index.html
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filestream = file.read()
            upload_data = Photo()
            upload_data.photo = db.Blob(filestream)
            upload_data.put()

            url = url_for("shows", key=upload_data.key())
            exif_data = get_exif_data(StringIO(filestream))

            return render_template('index.html',
                original_path = url,
                exif_data = exif_data)
    return render_template('index.html')

@app.route('/show_list', methods=['GET', 'POST'])
def show_list():
    return render_template('show_list.html', all_list = Photo.all())

@app.route('/show/<key>', methods=['GET'])
def shows(key):
    uploaded_data = db.get(key)
    return app.response_class(uploaded_data.photo)