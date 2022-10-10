from flask import *
from flask_sqlalchemy import *
from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from forms import LoginForm
import click
import os
import sys

name = "jch"
li =[1,2,3,4,5]

app = Flask(__name__)
app.secret_key = 'secret string'
#db = SQLAlchemy(app)



'''
@app.cli.command()
def hello():
    click.echo("Hello World")
'''
@app.route('/')
def hello_world():  # put application's code here
    return render_template('page.html',list = li, name = name)


@app.route('/test')
def testview():
    form = LoginForm()
    return render_template('test.html',form=form)

@app.route('/login')
def logind():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'



if __name__ == '__main__':
    app.run()

'''
with app.test_request_context():
    print(url_for('logind'))
    #print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
'''





