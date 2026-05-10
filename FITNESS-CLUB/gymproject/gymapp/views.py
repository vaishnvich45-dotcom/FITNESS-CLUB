from django.shortcuts import render
from .models import FitnessData

def home(request):
    from django.shortcuts import render
from .models import FitnessData

def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "User")
        age = request.POST.get("age", 18)
        weight = float(request.POST.get("weight", 50))
        height = float(request.POST.get("height", 160)) / 100
        stress = int(request.POST.get("stress", 5))
        if stress > 10:
            stress = 10

        bmi = round(weight / (height ** 2), 2)

        # CATEGORY + PLAN
        if bmi < 18.5:
            category = "Underweight"
            diet = "High calorie diet (milk, nuts, eggs, rice)"
            exercises = [
                {"name": "Yoga for beginners", "link": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
                {"name": "Light strength training", "link": "https://www.youtube.com/watch?v=U0bhE67HuDY"},
            ]
        elif bmi < 25:
            category = "Normal"
            diet = "Balanced diet (fruits, vegetables, protein)"
            exercises = [
                {"name": "Cardio workout", "link": "https://www.youtube.com/watch?v=ml6cT4AZdqI"},
                {"name": "Full body workout", "link": "https://www.youtube.com/watch?v=UBMk30rjy0o"},
            ]
        elif bmi < 30:
            category = "Overweight"
            diet = "Low calorie diet, avoid junk food"
            exercises = [
                {"name": "Running cardio", "link": "https://www.youtube.com/watch?v=ml6cT4AZdqI"},
                {"name": "Cycling workout", "link": "https://www.youtube.com/watch?v=2pLT-olgUJs"},
            ]
        else:
            category = "Obese"
            diet = "Strict low calorie diet"
            exercises = [
                {"name": "Walking plan", "link": "https://www.youtube.com/watch?v=5Fh0oX7eYqU"},
                {"name": "Light cardio", "link": "https://www.youtube.com/watch?v=ml6cT4AZdqI"},
            ]

        goal = "Improve fitness, maintain healthy lifestyle, reduce stress"

        FitnessData.objects.create(
            name=name,
            age=age,
            weight=weight,
            height=height,
            bmi=bmi,
            category=category,
            workout="Auto-generated workout",
            diet=diet,
            stress_level=stress
        )

        return render(request, "result.html", {
            "bmi": bmi,
            "category": category,
            "diet": diet,
            "exercises": exercises,
            "goal": goal
        })

    return render(request, "home.html")