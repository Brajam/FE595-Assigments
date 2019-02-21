##Import flask
from flask import Flask
from flask import render_template
import request


##definition of the REST API
app = Flask(__name__)
@app.route('/hello_updated', methods=['GET'])

##Function
def hello_updated():
#        get_request = requests.get('https://theyfightcrime.org/')
        return render_template('index.html', title='Hola Mundo')


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080)
