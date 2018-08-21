from flask import Flask, request, render_template
import sys
sys.path.append('..')
from ..MC_Contract import Contract, contracts 

# pass it in to help out flask
app = Flask(__name__)

# this basically renders two different templates given different URLS 
@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template('user.html',user=user)
    # string = 'This is the homepage\n'
    # return string+request.method



@app.route('/bacon',methods=['GET','POST'])
def bacon():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are probably using GET'


# flask is basically generating the HTML for us
@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html',name=name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'<h2>Post ID is {post_id} </h2>'

@app.route('/shopping')
def shopping():
    food = ['Cheese','Tuna','Beef']
    return render_template('shopping.html',food=food)



if __name__ == '__main__':
    app.run(debug=True) # when we're in developer mode 




























