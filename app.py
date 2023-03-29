from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "static/user_photo"


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/photos')
def photo():
    return render_template('photos.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        f = request.files['file']
        if f:

            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            return render_template("car_ops.html")
        else:

            return render_template("photos.html")


@app.route('/op_upload', methods=["POST"])
def op_upload():
    op_list = request.form.getlist('car_op')
    print(op_list)
    return render_template("result.html")


if __name__ == '__main__':
    app.run()
