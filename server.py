import sys
from flask import *
app = Flask(__name__, static_folder='static') 

@app.route('/', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        print('Recieved from client: ')
        print(request.values)
        sys.stdout.flush()
    return render_template('index.html')

if __name__ == '__main__':
    from os import environ
    app.run(debug=True, host='0.0.0.0', port=environ.get("PORT", 5000))
