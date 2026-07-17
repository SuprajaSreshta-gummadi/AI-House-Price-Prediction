import sqlite3


DATABASE_NAME = "predictions.db"


def create_table():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            gr_liv_area REAL NOT NULL,

            bedrooms INTEGER NOT NULL,

            bathrooms INTEGER NOT NULL,

            year_built INTEGER NOT NULL,

            predicted_price REAL NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    connection.commit()

    connection.close()


def save_prediction(

    gr_liv_area,

    bedrooms,

    bathrooms,

    year_built,

    predicted_price

):

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()

    cursor.execute(

        """
        INSERT INTO predictions (

            gr_liv_area,

            bedrooms,

            bathrooms,

            year_built,

            predicted_price

        )

        VALUES (?, ?, ?, ?, ?)

        """,

        (

            gr_liv_area,

            bedrooms,

            bathrooms,

            year_built,

            predicted_price

        )

    )

    connection.commit()

    connection.close()


def get_predictions():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(

        """
        SELECT *

        FROM predictions

        ORDER BY created_at DESC

        """

    )

    predictions = cursor.fetchall()

    connection.close()

    return predictions
def delete_prediction(prediction_id):

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM predictions
        WHERE id = ?
        """,
        (prediction_id,)
    )

    connection.commit()

    connection.close()
def get_all_predictions():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT

            id,

            gr_liv_area,

            bedrooms,

            bathrooms,

            year_built,

            predicted_price,

            created_at

        FROM predictions

        ORDER BY created_at DESC
        """
    )

    predictions = cursor.fetchall()

    connection.close()

    return predictions