from flask import Flask, request, render_template 
import pickle 
import math
 
# Load model
model = pickle.load(open('Model/model.pkl', 'rb')) 
 
app = Flask(__name__) 
 
@app.route('/')  
def index():  
    return render_template("index.html")    
  
@app.route('/predict', methods=['POST']) 
def predict_result(): 
    try:
        city_names = {
            '0': 'Ahmedabad', '1': 'Bengaluru', '2': 'Chennai', '3': 'Coimbatore', '4': 'Delhi',
            '5': 'Ghaziabad', '6': 'Hyderabad', '7': 'Indore', '8': 'Jaipur', '9': 'Kanpur',
            '10': 'Kochi', '11': 'Kolkata', '12': 'Kozhikode', '13': 'Lucknow', '14': 'Mumbai',
            '15': 'Nagpur', '16': 'Patna', '17': 'Pune', '18': 'Surat'
        }

        crimes_names = {
            '0': 'Crime Committed by Juveniles', '1': 'Crime against SC', '2': 'Crime against ST',
            '3': 'Crime against Senior Citizen', '4': 'Crime against children',
            '5': 'Crime against women', '6': 'Cyber Crimes', '7': 'Economic Offences',
            '8': 'Kidnapping', '9': 'Murder'
        }

        population = {
            '0': 63.50, '1': 85.00, '2': 87.00, '3': 21.50, '4': 163.10, '5': 23.60, '6': 77.50,
            '7': 21.70, '8': 30.70, '9': 29.20, '10': 21.20, '11': 141.10, '12': 20.30,
            '13': 29.00, '14': 184.10, '15': 25.00, '16': 20.50, '17': 50.50, '18': 45.80 
        }

        # Extract and convert form data
        year = int(request.form['year'])  
        city_code = int(request.form["city"]) 
        crime_code = int(request.form['crime']) 
        pop = population[str(city_code)]  # convert back to string for the population dict


        # Adjust population by year difference (1% per year)
        year_diff = year - 2011
        pop = pop + 0.01 * year_diff * pop

        # Predict crime rate 
        crime_rate = model.predict([[year, city_code, pop, crime_code]])[0]


        # Get city and crime names
        city_name = city_names[str(city_code)]
        crime_type = crimes_names[str(crime_code)]

        # Classify crime level
        if crime_rate <= 1:
            crime_status = "Very Low Crime Area" 
        elif crime_rate <= 5:
            crime_status = "Low Crime Area"
        elif crime_rate <= 15:
            crime_status = "High Crime Area" 
        else:
            crime_status = "Very High Crime Area" 

        # Estimate number of cases
        cases = math.ceil(crime_rate * pop)

        return render_template('result.html',
            city_name=city_name,
            crime_type=crime_type,
            year=year,
            crime_status=crime_status,
            crime_rate=round(crime_rate, 2),
            cases=cases,
            population=round(pop, 2)
        )

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=False)
