from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from services.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inovex.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key'  # Set a strong secret key in production

db.init_app(app)

# Create tables at startup using application context (Flask 3.x compatible)
with app.app_context():
    db.create_all()

# Blueprint imports (after db is initialized)
from services.admin import admin_bp
from services.careers import careers_bp
from services.contact import contact_bp

# Register blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(careers_bp, url_prefix='/careers')
app.register_blueprint(contact_bp, url_prefix='/contact')

# Routes
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
