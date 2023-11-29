# Import the Flask class and necessary modules from the Flask package
from flask import Flask, render_template, request

# Create a Flask web application instance
app = Flask(__name__)

# Function to convert height to meters based on the selected unit
def convert_to_meters(height, unit):
    if unit == 'ft':
        return height * 0.3048  # Convert feet to meters (1 foot = 0.3048 meters)
    else:
        return height

# Function to categorize BMI into different health categories
def categorize_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight (Bad)'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight (Good)'
    elif 25 <= bmi < 29.9:
        return 'Overweight (Bad)'
    elif bmi >= 30:
        return 'Obese (Bad)'

# Route decorator for the default route ('/')
@app.route('/')
def index():
    # Render the HTML template for the index page
    return render_template('index.html')

# Route decorator for the '/calculate' endpoint with POST method
@app.route('/calculate', methods=['POST'])
def calculate():
    # Extract user input from the submitted form
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    unit = request.form['unit']

    # Convert height to meters if the unit is feet
    height_in_meters = convert_to_meters(height, unit)

    # Calculate BMI
    bmi = round(weight / (height_in_meters ** 2), 2)

    # Categorize BMI
    bmi_category = categorize_bmi(bmi)

    # Render the HTML template with calculated BMI and category
    return render_template('index.html', bmi=bmi, bmi_category=bmi_category)

# Check if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
