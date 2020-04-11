# import the Flask class from the flask module



from flask import Flask, render_template, request
from flask import send_file
# create the application object
app = Flask(__name__)




@app.route("/")

@app.route('/welcome')
@app.route('/home')

def welcome():
    return render_template('home.html')  # render a template

@app.route('/login')
def login():
    return render_template('login.html')  

@app.route('/register')
def register():
    return render_template('home.html') 

@app.route('/about')
def about():
    return render_template('about.html') 


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

import io

from flask import current_app as app
from flask import send_file

from myproject import Obj

@app.route('/logo.png')
def logo():
    """Serves the logo image."""

    obj = Obj.objects.get(title='Logo')

    return send_file(io.BytesIO(obj.logo.read()),
                     attachment_filename='logo.png',
                     mimetype='image/png')


if __name__ == "__main__":
    app.run()
