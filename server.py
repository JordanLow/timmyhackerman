from flask import *
app = Flask(__name__, static_folder='static') 

@app.route('/', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        print('Recieved from client: {}'.format(request.data))
        return Response('We recieved something…')

if __name__ == '__main__':
    from os import environ
    app.run(debug=True, host='0.0.0.0', port=environ.get("PORT", 5000))
