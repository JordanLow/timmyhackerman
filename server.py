from flask import Flask, render_template
app = Flask(__name__, static_folder='static') 

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 5000))
