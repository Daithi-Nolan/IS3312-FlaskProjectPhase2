from db.extensions import db


class Product(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(10000), nullable=False)
    coating = db.Column(db.String(50))
    materials = db.Column(db.String(100))
    embossing = db.Column(db.String(50))
    image_url = db.Column(db.String(200))
    description = db.Column(db.Text)
    country = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"


class User:
    def __init__(self, user_id, username, password, email, user_type="customer"):  # Creates user attributes
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.user_type = user_type

    def is_admin(self):
        return self.user_type == "admin"  # Checks whether user is an admin

    def __repr__(self):  # Returns string used for debugging
        return f"User({self.username}, {self.email}, Type: {self.user_type})"

