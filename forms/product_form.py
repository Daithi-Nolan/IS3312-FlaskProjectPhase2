from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, NumberRange, URL


# Fields for entry - all attributes except ID
class ProductForm(FlaskForm):
    name = StringField("Product Name")
    brand = StringField("Brand")
    price = DecimalField("Price (€)")
    coating = StringField("Coating")
    materials = StringField("Materials")
    embossing = StringField("Embossing")
    image_url = StringField("Image URL")
    description = StringField("Description")
    country = StringField("Country")

    submit = SubmitField("Save Product")

