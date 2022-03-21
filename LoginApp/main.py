from flask import *
app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/success', methods = ['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if password != 'jtp':
            return redirect(url_for('error'))
        else:
            res = make_response(render_template('success.html', email = email))
            res.set_cookie('email', email)
            return res

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/profile')
def profile():
    email = request.cookies.get('email')
    res = make_response(render_template('profile.html', email = email))
    return res
    

if __name__ == '__main__':
    app.run(debug=True)