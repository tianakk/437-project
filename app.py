#source : https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b
import os
from flask import Flask
import DriverClass

app = Flask(__name__)

@app.route("/")
def generate_buzz():

    return 'Hello world'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

