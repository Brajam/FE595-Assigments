##Import flask
from flask import Flask

##definition of the REST API
app = Flask(__name__)
@app.route('/hello', methods=['GET'])

##Function hello
def hello_world():
        return "Hello, world!"

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080)
