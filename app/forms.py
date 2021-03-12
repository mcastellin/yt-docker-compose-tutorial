from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, TextAreaField


class RecipeForm(FlaskForm):
    name = StringField(
        "Name", validators=[validators.required(), validators.length(max=256)]
    )
    ingredients = TextAreaField("Ingredients", validators=[validators.optional()])
    directions = TextAreaField("Directions", validators=[validators.optional()])
    submit = SubmitField("Save")
