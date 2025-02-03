from db.extensions import db, bcrypt
from flask_login import UserMixin


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


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)  # Stores encrypted password
    role = db.Column(db.String(20), default="customer", nullable=False)  # Admin or Customer
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Method to set password
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Method to check password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username} - {self.role}>"
