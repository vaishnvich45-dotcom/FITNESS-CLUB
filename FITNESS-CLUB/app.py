from flask import Flask, render_template, request

app = Flask(__name__)

# BMI CALCULATION
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# EXERCISE PLAN
def get_exercises(category):

    plans = {

        "Underweight": [
            {"name": "Push-ups", "link": "https://www.google.com/search?q=pushups+exercise"},
            {"name": "Bodyweight Squats", "link": "https://www.google.com/search?q=squats+exercise"},
            {"name": "Strength Training", "link": "https://www.google.com/search?q=strength+training"}
        ],

        "Normal": [
            {"name": "Plank", "link": "https://www.google.com/search?q=plank+exercise"},
            {"name": "Jogging", "link": "https://www.google.com/search?q=jogging+exercise"},
            {"name": "Pull-ups", "link": "https://www.google.com/search?q=pullups"}
        ],

        "Overweight": [
            {"name": "Brisk Walking", "link": "https://www.google.com/search?q=brisk+walking+exercise"},
            {"name": "Cycling", "link": "https://www.google.com/search?q=cycling+exercise"},
            {"name": "Jumping Jacks", "link": "https://www.google.com/search?q=jumping+jacks"}
        ],

        "Obese": [
            {"name": "Slow Walking", "link": "https://www.google.com/search?q=walking+exercise"},
            {"name": "Chair Squats", "link": "https://www.google.com/search?q=chair+squat+exercise"},
            {"name": "Wall Push-ups", "link": "https://www.google.com/search?q=wall+pushups"}
        ]
    }

    return plans[category]


# DIET PLAN 
def diet_plan(category):

    diet = {

        "Underweight": "High protein diet including milk, banana, rice, paneer and nuts.",

        "Normal": "Balanced diet including vegetables, fruits and protein rich food.",

        "Overweight": "Low oil food with oats, fruits and fiber rich meals.",

        "Obese": "Light meals like soups, vegetables and fruits. Avoid oily food."
    }

    return diet[category]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    weight = float(request.form["weight"])
    height = float(request.form["height"])
    age = int(request.form["age"])
    stress = int(request.form["stress"])
    goal = request.form["goal"]

    bmi = calculate_bmi(weight, height)

    category = bmi_category(bmi)

    exercises = get_exercises(category)

    diet = diet_plan(category)

    return render_template(
        "result.html",
        bmi=bmi,
        category=category,
        goal=goal,
        exercises=exercises,
        diet=diet
    )


if __name__ == "__main__":
    app.run(debug=True)