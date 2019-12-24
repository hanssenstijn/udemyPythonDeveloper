from flask import Flask, render_template, url_for
app = Flask(__name__)

# the html file will be searched by render_template in a template folder (thus move html file to template)
# have to give a name after the IP adress
@app.route('/<username>/<int:post_id>')
def hello_world(username=None,post_id=None):
    return render_template('index.html',name=username,post_id=post_id)

@app.route('/about.html')
def about():
    return render_template('about.html')

# create flavicon (icon on the tabbar)
# @app.route('/favicon.ico')
# def blog():
    # return 'These are my thoughts on blogs'

# create blog folder
@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs'

# create a dogs folder in 2020 within the blogs folder
@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'
