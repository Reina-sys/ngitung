from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculation1')
def calculation1():
    return render_template('calculation1.html')

@app.route('/calculation2')
def calculation2():
    return render_template('calculation2.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
