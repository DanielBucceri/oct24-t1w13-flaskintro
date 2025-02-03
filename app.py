from flask import Flask

app = Flask(__name__)

@app.route('/bleep')
def hello():
    return 'Hello!'

if __name__ == '__main__':
    app.run(debug=True)
