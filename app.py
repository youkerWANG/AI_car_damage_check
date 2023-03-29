from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/photos')
def photo():
    return render_template('photos.html')

@app.route('/help')
def help():
    return render_template('help.html')


if __name__ == '__main__':
    app.run()
