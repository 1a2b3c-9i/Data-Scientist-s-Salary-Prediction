from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Define a function to predict salary
def predict_salary(company_rating, company_founded, company_sector, company_ownership):
    # Replace this with your salary prediction logic
    # Example: Calculate salary based on input features
    salary = (company_rating * 10000) + (company_founded * 50)
    return salary

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the JSON request
    data = request.json

    # Extract relevant features from the JSON data
    company_rating = data['company_rating']
    company_founded = data['company_founded']
    company_sector = data['company_sector']
    company_ownership = data['company_ownership']

    # Call the predict_salary function
    predicted_salary = predict_salary(company_rating, company_founded, company_sector, company_ownership)

    # Return the predicted salary as JSON response
    return jsonify({"predicted_salary": predicted_salary})

if __name__ == '__main__':
    app.run(debug=True)
