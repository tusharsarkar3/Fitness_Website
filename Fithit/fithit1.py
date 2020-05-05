from flask import Flask,request,render_template,session,redirect,url_for,flash
import math

app = Flask(__name__)
app.secret_key="hey"

#@app.route("/home")
@app.route("/")
def home ():
    return render_template("fitness_page.html")

@app.route("/bodyfat", methods = ["GET","POST"])
def bodyfat():
    if request.method == "POST":
        gender = request.form["Gender"]
        session["Gender"] = gender
        height = int(request.form["Height"])
        session["Height"] = height
        waist = int(request.form["Waist"])
        session["Waist"] = waist
        neck = int(request.form["Neck"])
        session["Neck"] = neck
        hip = int(request.form["Hip"])
        session["Hip"] = hip
        if gender == "male":
            bf = (495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height))) - 450
            flash(f"your body fat is: {bf}","info")
            return render_template("bodyfat.html")

        elif gender == "female":
            bf = 495/((1.29579 - 0.35004 * math.log10(waist+hip-neck) + 0.22100 * math.log10(height))) - 450
            flash(f"your body fat is: {bf}", "info")
            return render_template("bodyfat.html")

    else:
        flash("Enter values in all the fields", "info")
        return render_template("bodyfat.html")

@app.route("/bmi", methods =["GET","POST"])
def bmi():
    if request.method == "POST":
        height1 = int(request.form["Height"])
        session["Height"] = height1
        height = float(height1/100)
        weight = int(request.form["Weight"])
        session["Weight"] = weight
        bmi = (weight/math.pow(height,2))
        flash(f"your BMI is: {bmi}", "info")
        return render_template("bmi.html")
    else:
        flash("Enter values in all the fields", "info")
        return render_template("bmi.html")


@app.route("/motivation")
def motivation():
    return render_template("motivation.html")

@app.route("/ideas")
def ideas():
    if request.method == "POST":
        flash("Your idea has been taken", "info")
    return render_template("ideas.html")

@app.route("/gym")
def gym():
    return render_template("gym.html")

@app.route("/gym/beginner")
def beginner():
    return render_template("beginner.html")

@app.route("/gym/inter")
def inter():
    return render_template("inter.html")

@app.route("/gym/advanced")
def advanced():
    return render_template("advanced.html")

@app.route("/home")
def homeworkout():
    return render_template("home.html")

@app.route("/diet", methods=["GET","POST"])
def diet():
    if request.method == "POST":
        weight = int(request.form["Weight"])
        session["Weight"] = weight
        calorie = (int(2.205 * weight * 21))
        protein = (int(1.7 * weight))
        procalories = 4 * protein
        fatcal = int(calorie / 5)
        fat = int(fatcal / 9)
        carbs = (int)((calorie - procalories - fatcal) / 9)
        flash(f"Your total calorie intake should be : {calorie} calories", "info")
        flash(f"Your total protein intake should be: {protein} gms","info")
        flash(f" Your total carbohydates intake should be: {carbs} gms","info")
        flash(f" Your total fat intake should be: {fat} gms","info")
        return render_template("diet.html")
    else:
        flash("Enter your weight", "info")
        return render_template("diet.html")


if __name__ == "__main__":
    app.run(debug=True)