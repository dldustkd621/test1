from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url = request.form["urlBox"]
    return render_template('index.html', data = url)