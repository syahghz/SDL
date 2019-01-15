from flask import *
app=Flask(__name__)

@app.route("/")
def heeloworld():
    return render_template("test.html")

if __name__== '__main__':

    app.run(port="80")
#er
