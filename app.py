from flask import *
from db.extensions import db, migrate, login_manager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database before importing models
db.init_app(app)
migrate.init_app(app, db)

from model.models import Product, User  # Import after initializing db


# Import models after initializing db to avoid circular imports
@app.route('/')
def customer_home():
    products = Product.query.all()
    selected_products = [products[1], products[4], products[5], products[8]]
    return render_template('customer-home.html', products=selected_products)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/all-products', methods=['GET'])
def all_products():
    # Fetch all products from the database
    products = Product.query.all()

    # Extract unique country names for the dropdown filter
    countries = sorted(set(product.country for product in products))

    # Get sorting/filtering parameters from the request
    selected_country = request.args.get('country', '')
    selected_sort = request.args.get('sort', 'default')
    selected_price_sort = request.args.get('price_sort', 'default')

    # Apply country filtering
    if selected_country:
        products = Product.query.filter_by(country=selected_country).all()

    # Apply sorting (alphabetically)
    if selected_sort == 'a-z':
        products.sort(key=lambda x: x.name)
    elif selected_sort == 'z-a':
        products.sort(key=lambda x: x.name, reverse=True)

    # Apply price sorting
    if selected_price_sort == 'low-high':
        products.sort(key=lambda x: x.price)
    elif selected_price_sort == 'high-low':
        products.sort(key=lambda x: x.price, reverse=True)

    # Pass data to template
    return render_template(
        'all-products.html',
        products=products,
        countries=countries,
        selected_country=selected_country,
        selected_sort=selected_sort,
        selected_price_sort=selected_price_sort
    )


@app.route('/featured-products')
def featured_products():
    products = Product.query.all()
    featured = products[5:8]
    return render_template('featured-products.html', products=featured)


@app.route('/product-details/<string:product_id>')
def product_details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product-details.html', product=product)


# Initialise Flask-Login
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirects users to login page if not authenticated
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "warning"


# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Loads user by ID


# Renders privacy policy page
@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')


# Renders t's & c's page
@app.route('/terms-conditions')
def terms_conditions():
    return render_template('terms-conditions.html')


@app.errorhandler(401)
def invalid_authorisation(e):
    return render_template("401.html"), 401


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
