from flask import Flask, render_template
import datetime
import requests
app = Flask(__name__)


@app.route("/")
def homePage():
    Cyear = datetime.datetime.now().year
    return render_template("index.html", year=Cyear)

@app.route("/guess/<name>")
def guess(name):
    genderUrl = f"https://api.genderize.io?name={name}"
    Genderresponse = requests.get(genderUrl)
    gender_data = Genderresponse.json()
    gender = gender_data["gender"]
    ageURL = f"https://api.agify.io?name={name}"
    age = requests.get(ageURL).json()["age"]
    return render_template("guess.html", person_name=name, person_gender=gender, person_age=age)

@app.route("/blog")
def blogposts():
    blogURL = "https://api.npoint.io/f7f000cdc2dff746bc77"
    allposts = requests.get(blogURL).json()
    return render_template("blog.html", posts=allposts)
if __name__ ==  "__main__":
    app.run(debug=True)