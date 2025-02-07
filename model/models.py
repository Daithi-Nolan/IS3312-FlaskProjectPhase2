from db.extensions import db, bcrypt
from flask_login import UserMixin
from datetime import datetime


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
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(50), unique=True, nullable=False)
    first_name: str = db.Column(db.String(100), unique=False, nullable=False)
    last_name: str = db.Column(db.String(100), unique=False, nullable=False)
    email: str = db.Column(db.String(100), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(200), nullable=False)
    role: str = db.Column(db.String(20), default="customer", nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Method to set password
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Method to check password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username} - {self.role}>"


class Order(db.Model):
    """Order model to store transaction details."""
    id = db.Column(db.Integer, primary_key=True)  # Order ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable for guest orders
    total_price = db.Column(db.Float, nullable=False)  # Total amount of the order
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Time of order placement

    order_items = db.relationship('OrderItem', backref='order', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order {self.id} - Total: €{self.total_price:.2f}>"


class OrderItem(db.Model):
    """OrderItem model to store individual items within an order."""
    id = db.Column(db.Integer, primary_key=True)  # Unique item ID
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)  # Order reference
    product_id = db.Column(db.String(20), db.ForeignKey('product.id'), nullable=False)  # Product reference
    quantity = db.Column(db.Integer, nullable=False)  # Number of products
    unit_price = db.Column(db.Float, nullable=False)  # Price per unit

    product = db.relationship('Product')

    def __repr__(self):
        return f"<OrderItem {self.product_id} x{self.quantity}>"


class Cart(db.Model):
    """Model to store shopping cart items per user."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Links cart to a user
    product_id = db.Column(db.String(20), db.ForeignKey('product.id'), nullable=False)  # Links to a product
    quantity = db.Column(db.Integer, nullable=False, default=1)  # Number of items

    product = db.relationship('Product', backref='cart_items')

    def __repr__(self):
        return f"<Cart User:{self.user_id} Product:{self.product_id} Qty:{self.quantity}>"
