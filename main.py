from flask import Flask, render_template,request
import uuid
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER="uploads"
ALLOWED_EXTENSION={"txt","pdf","png","jpg","jpeg","gif"}
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
@app.route("/")
def home():
    return render_template("index.html")





@app.route("/create", methods=['GET', 'POST'])
def create():

    uuid1 = str(uuid.uuid4())

    if request.method == "POST":

        res_id = request.form.get("uuid")
        desc = request.form.get("text")

        folder_path = os.path.join(
            app.config['UPLOAD_FOLDER'], res_id
        )

        os.makedirs(folder_path, exist_ok=True)

        for key, value in request.files.items():

            file = request.files[key]

            if file and file.filename:

                filename = secure_filename(file.filename)

                file.save(os.path.join(folder_path, filename))
        with open(os.path.join(app.config['UPLOAD_FOLDER'],res_id,"desc.txt"),"w") as f:
            f.write(desc)        

    return render_template("create.html", myid=uuid1)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)