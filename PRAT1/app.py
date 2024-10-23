from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = "joshua"

@app.route('/hello')
def index():
    flash("What's your name: ")
    return render_template('greet.html')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash('Hi ' + str(request.form['name']) + ', great to see you!')
    return render_template('greet.html')

if __name__ == "__main__":
    app.run(debug=True)