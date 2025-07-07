
from flask_wtf import FlaskForm
import pandas as pd

from wtforms import SelectField , DateField , TimeField , IntegerField ,SubmitField
from wtforms.validators import DataRequired
# getting the data

train = pd.read_csv("data/train (1).csv")
test = pd.read_csv("data/test.csv")
val = pd.read_csv('data/val.csv')
x_data = pd.concat([train , val] , axis=0).drop(columns="price")


class Inputform(FlaskForm) :

    airline = SelectField(
        label="Airlines",
        choices=x_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )

    date_of_journey = DateField(
        label="Date of Journey",
        validators=[DataRequired()]
    )

    source = SelectField(
        label="Terminal",
        choices=x_data.source.unique().tolist(),
        validators=[DataRequired()]
    )

    destination = SelectField(
        label="Destination",
        choices=x_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )

    arrival_time = TimeField(
        label="Arrival Time",
        validators=[DataRequired()]
    )

    dep_time = TimeField(
        label="Departure Time",
        validators=[DataRequired()]
    )

    duration = IntegerField(
        label="Journey Duration",
        validators=[DataRequired()]
    )

    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )

    additional_info = SelectField(
        label="Additional Information",
        choices=x_data.additional_info.unique().tolist(),           # here same nameof col as in the dataset to verify theuniqueness
        validators=[DataRequired()]
    )

    submit = SubmitField("Predict")
