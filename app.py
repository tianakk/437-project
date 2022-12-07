#source : https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b

from flask import Flask, request, render_template
import DriverClass

app = Flask(__name__)

@app.route("/")
def generate_buzz():

        # return DriverClass.mainMenu()
        # page = '<html><body><h1>'
        # page += DriverClass.mainMenu()
        # page += '</h1></body></html>'
        # return page
        return '</h1></body></html>'

if __name__ == "__main__":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
        # # return "<h1>DriverClass.mainMenu()<h1>"
        # # return DriverClass.mainMenu