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






if __name__ == "__main__":
    app.run()
