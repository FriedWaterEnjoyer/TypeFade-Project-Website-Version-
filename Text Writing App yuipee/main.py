#|||| Imports ||||#


from flask import Flask, render_template
import os
from dotenv import load_dotenv
import datetime as dt


#|||| App initialization + .env load ||||#


load_dotenv()

app=Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("API_KEY")

da_year = dt.datetime.now().year


#|||| Website Routes ||||#


@app.route("/")
def main_page():

    return render_template("index.html", year=da_year)


@app.route("/type")
def type_page():

    return render_template("type.html")



if __name__ == '__main__':

    app.run(debug=True)
