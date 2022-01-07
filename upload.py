import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

print(os.path.join(os.path.dirname(__file__), "uploads"))
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(__file__), "uploads")
# app.config("MAX_CONTENT_PATH", 16 * 1024 * 1024)  # 16 MB


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/uploader", methods=["GET", "POST"])
def uploader():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        return "file uploaded successfully", 201


if __name__ == "__main__":
    app.run(debug=True)
