from flask import *
app = Flask(__name__)

@app.route('/')
def getData():
    return render_template('form.html')

@app.route('/success', methods = ['GET', 'POST'])
def print():
    if request.method == 'POST':
        result = request.form
        return render_template('print.html', result=result)

if __name__ == '__main__':
    app.run(debug = True)