from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open('./flag.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = "File not found."
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)