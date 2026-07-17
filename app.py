from flask import (
    Flask,
    render_template,
    request,
    redirect,
    Response
)

import joblib

import pandas as pd

from db import (
    create_table,
    save_prediction,
    get_predictions,
    delete_prediction,
    get_all_predictions
)

app = Flask(__name__)


# Create database table
create_table()


# Load trained Machine Learning model
model = joblib.load(
    "house_price_model.pkl"
)


# Load feature columns used during training
feature_columns = joblib.load(
    "feature_columns.pkl"
)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


@app.route("/contact")
def contact():

    return render_template(
        "contact.html"
    )


@app.route("/dashboard")
def dashboard():

    predictions = get_predictions()

    return render_template(

        "dashboard.html",

        predictions=predictions

    )
@app.route(
    "/delete/<int:prediction_id>",
    methods=["POST"]
)
def delete(prediction_id):

    delete_prediction(
        prediction_id
    )

    return redirect(
        "/dashboard"
    )
@app.route("/export")
def export():

    predictions = get_all_predictions()


    csv_data = (

        "ID,Living Area,Bedrooms,"
        "Bathrooms,Year Built,"
        "Predicted Price,Date\n"

    )


    for prediction in predictions:

        csv_data += (

            f"{prediction[0]},"
            f"{prediction[1]},"
            f"{prediction[2]},"
            f"{prediction[3]},"
            f"{prediction[4]},"
            f"{prediction[5]},"
            f"{prediction[6]}\n"

        )


    return Response(

        csv_data,

        mimetype="text/csv",

        headers={

            "Content-Disposition":
            "attachment; filename=predictions.csv"

        }

    )


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        # Get values from form
        gr_liv_area = float(
            request.form["GrLivArea"]
        )

        bedroom_abv_gr = int(
            request.form["BedroomAbvGr"]
        )

        full_bath = int(
            request.form["FullBath"]
        )

        year_built = int(
            request.form["YearBuilt"]
        )


        # Create an empty input row
        input_data = pd.DataFrame(

            0,

            index=[0],

            columns=feature_columns

        )


        # Add the four user input values
        if "GrLivArea" in input_data.columns:

            input_data.loc[
                0,
                "GrLivArea"
            ] = gr_liv_area


        if "BedroomAbvGr" in input_data.columns:

            input_data.loc[
                0,
                "BedroomAbvGr"
            ] = bedroom_abv_gr


        if "FullBath" in input_data.columns:

            input_data.loc[
                0,
                "FullBath"
            ] = full_bath


        if "YearBuilt" in input_data.columns:

            input_data.loc[
                0,
                "YearBuilt"
            ] = year_built


        # Make prediction
        prediction = model.predict(
            input_data
        )


        predicted_price = round(

            prediction[0],

            2

        )


        # Save prediction to database
        save_prediction(

            gr_liv_area,

            bedroom_abv_gr,

            full_bath,

            year_built,

            predicted_price

        )


        # Display prediction
        return render_template(

            "index.html",

            prediction=predicted_price

        )


    except Exception as error:

        return render_template(

            "index.html",

            error=str(error)

        )


if __name__ == "__main__":

    app.run(

        debug=True

    )