from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'Welcome, %s!' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')
        if user:
            return redirect(url_for('success', name=user))
        else:
            return render_template('index.html', error='Please provide a username.')
    else:
        user = request.args.get('nm')
        if user:
            return redirect(url_for('success', name=user))
        else:
            return render_template('index.html', error='Please provide a username.')

@app.route("/")
def index():
    return render_template("index.html")

if __name__== '__main__':
    app.run(debug=True)