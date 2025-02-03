from flask import *
from flask_login import login_user, logout_user, login_required
from db.extensions import db, migrate, login_manager
from forms.registration_form import RegistrationForm
from forms.login_form import LoginForm
from forms.password_reset_form import PasswordResetForm, PasswordResetRequestForm
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature

app = Flask(__name__)

app.config['SECRET_KEY'] = 'WeatherWaySecretKey123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Token Serializer (Used for generating password reset links)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Initialize database before importing model
db.init_app(app)
migrate.init_app(app, db)

from model.models import Product, User  # Import after initializing db


# Import model after initializing db to avoid circular imports
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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Login successful!", "success")
            return redirect(url_for("customer_home"))  # Redirect to home page

        else:
            flash("Invalid email or password. Please try again.", "danger")

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Hash the user's password
        hashed_password = User()
        hashed_password.set_password(form.password.data)

        # Create new user
        new_user = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password_hash=hashed_password.password_hash,  # Store hashed password
            role="customer"  # Default role is "customer"
        )

        # Add user to the database
        db.session.add(new_user)
        db.session.commit()

        flash("Your account has been created! You can now log in.", "success")
        return redirect(url_for("login"))  # Redirect to login page

    return render_template("register.html", form=form)


@app.route("/password-reset", methods=["GET", "POST"])
def password_reset():
    form = PasswordResetRequestForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            # Generate a secure token for password reset
            token = serializer.dumps(user.email, salt='password-reset-salt')
            reset_url = url_for('password_reset_token', token=token, _external=True)

            # Display a clickable link
            flash(f'Follow this link to reset your password: <a href="{reset_url}">{reset_url}</a>', "info")

        else:
            flash("No account found with that email.", "danger")

        return redirect(url_for("login"))

    return render_template("password-reset.html", form=form)


@app.route("/password-reset/<token>", methods=["GET", "POST"])
def password_reset_token(token):
    try:
        # Try to decode the token
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except SignatureExpired:
        flash("The reset link has expired. Please request a new one.", "danger")
        return redirect(url_for("password_reset"))
    except BadSignature:
        flash("Invalid or tampered reset link. Please try again.", "danger")
        return redirect(url_for("password_reset"))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash("No account found with this email.", "danger")
        return redirect(url_for("password_reset"))

    form = PasswordResetForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)  # Hashes and sets the new password
        db.session.commit()
        flash("Your password has been reset! You can now log in.", "success")
        return redirect(url_for("login"))

    return render_template("password-reset-confirm.html", form=form)


@app.route("/logout")
@login_required  # Ensure only logged-in users can access this route
def logout():
    logout_user()  # Flask-Login method to clear user session
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))  # Redirect to login page


@app.route("/checkout")
@login_required
def checkout():
    return render_template("checkout.html")


@app.route("/shopping-cart")
@login_required
def shopping_cart():
    return render_template("shopping-cart.html")


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


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("404.html"), 405


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
