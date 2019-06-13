from flask import Flask, render_template
app = Flask(__name__, static_folder='static') 

@app.route('/index.html')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data():
    print('Recieved from client: {}'.format(request.data))
    return Response('We recieved something…')

if __name__ == '__main__':
    from os import environ
    app.run(debug=False, host='0.0.0.0', port=environ.get("PORT", 5000))
