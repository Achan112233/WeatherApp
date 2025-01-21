# filepath: /c:/Users/antho/OneDrive/Documents/GitHub/WeatherApp/myproject/hello.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World this is flask!'

if __name__ == '__main__':
    app.run()