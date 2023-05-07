from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def myhomepage():
    return render_template('myhomepage.html')


@app.route('/myschedule')
def myschedule():
    return render_template('myschedule.html')


@app.route('/mygallery')
def mygallery():
    return render_template('mygallery.html')


@app.route('/guestbook')
def guestbook():
    return render_template('guestbook.html')


if __name__ == '__main__':
    app.run(debug=True, port="5000")
