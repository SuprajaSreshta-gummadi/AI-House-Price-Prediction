## Your project: AI House Price Prediction

"My project is an AI-based House Price Prediction web application. I built it using Python and Machine Learning. The main purpose of the project is to predict the estimated price of a house based on input features such as the number of bedrooms, bathrooms, living area, location, and other property details.

I trained a Machine Learning model using house price data. After training, I saved the model as a .pkl file using Joblib. Then I created a Flask web application where users can enter the house details. The Flask application loads the trained model and uses the input values to predict the estimated house price.

I also created HTML pages using Flask templates and CSS for the user interface. Finally, I deployed the application online using Render."

# How your project works:The flow like this:#

User enters house details
          ↓
       Flask app
          ↓
   Data is prepared
          ↓
   Trained ML model
          ↓
   Price prediction
          ↓
  Result shown on website

Test it web service link: https://ai-house-price-prediction-tqdr.onrender.com
# What technologies did you use?

"I used Python for programming, Pandas and NumPy for data processing, Scikit-learn for machine learning, Joblib for saving and loading the trained model, Flask for creating the web application, HTML and CSS for the frontend, and Render for deployment."

Python
Pandas
NumPy
Scikit-learn
Joblib
Flask
HTML
CSS
Render
# What is Machine Learning in your project?
Machine Learning helps the computer learn patterns from previous house price data. After training on existing data, the model can estimate the price of a new house based on its features."
# What model did you use?
"I used Random Forest Regressor because house price prediction is a regression problem. The model uses multiple decision trees and combines their predictions to produce a more reliable result."
# What is the .pkl file?
## house_price_model.pkl
"After training the model, I saved it as a .pkl file using Joblib. This allows me to load the already-trained model in my Flask application without training it again every time a user makes a prediction."
# Why did you use Flask?

"I used Flask because it is a lightweight Python web framework. It allowed me to connect my machine learning model with a web interface."

Simple flow:

HTML Form
    ↓
Flask
    ↓
Python Model
    ↓
Prediction
    ↓
HTML Result



#In simple way:
"I developed an AI-based House Price Prediction web application using Python, Machine Learning, and Flask. I trained a Random Forest Regression model to predict house prices based on property features. I saved the trained model using Joblib and connected it to a Flask web application. Users can enter house details through the website and receive a predicted price. I used HTML and CSS for the frontend and deployed the application using Render. Through this project, I learned how to connect a machine learning model with a real web application and deploy it online."

Data → Train Model → Save Model → Flask → User Input → Prediction → Website Result
