from flask import Flask, render_template

# This is the instance of Flask object, that has come kind og methods
app = Flask(__name__)

# this will be our router - tells your where to go, a route. It manages routes paths.
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
# debug = True allows refreshing of content. So you do not have to keep 'killing' the server.







