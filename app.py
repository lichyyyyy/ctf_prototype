from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("<helllllo and welcome to my webserver!>")

if __name__ == '__main__':
    app.run(debug=True)