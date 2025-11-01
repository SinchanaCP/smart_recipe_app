from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

# Nutrition tips list
TIPS = [
    "Stay hydrated – drink at least 8 glasses of water daily!",
    "Add a variety of colors to your plate for balanced nutrition.",
    "Don’t skip breakfast – it boosts metabolism!",
    "Opt for grilled instead of fried food for fewer calories.",
    "Include protein in every meal to build muscle and stay full longer.",
    "Cut down on added sugars for better heart health.",
    "Try meal prepping on weekends to stay on track during busy days!"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        api_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredients}"
        response = requests.get(api_url)
        data = response.json()
        recipes = data.get("meals")
        tip = random.choice(TIPS)
        return render_template('result.html', recipes=recipes, ingredients=ingredients, tip=tip)
    return render_template('index.html')

@app.route('/details/<meal_id>')
def details(meal_id):
    api_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(api_url)
    data = response.json()
    meal = data["meals"][0]
    return render_template('details.html', meal=meal)

if __name__ == '__main__':
    app.run(debug=True)
