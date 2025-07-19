from flask import Blueprint, request, render_template_string, redirect, url_for, session
from functools import wraps
from .models import db, Contact, Application

admin_bp = Blueprint('admin', __name__)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "adminpass"

# Login required decorator

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("admin.admin_login"))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route("/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("admin.admin_dashboard"))
        else:
            return "Invalid credentials", 401
    return render_template_string("""
        <form method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    """)

@admin_bp.route("/logout")
def admin_logout():
    session.pop("logged_in", None)
    return redirect(url_for("admin.admin_login"))

@admin_bp.route("/")
@login_required
def admin_dashboard():
    contacts_data = Contact.query.all()
    careers_data = Application.query.all()
    return render_template_string("""
        <h1>Admin Dashboard</h1>
        <p><a href="/admin/logout">Logout</a></p>

        <h2>Contact Entries</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Message</th>
                </tr>
            </thead>
            <tbody>
                {% for contact in contacts_data %}
                <tr>
                    <td>{{ contact.name }}</td>
                    <td>{{ contact.email }}</td>
                    <td>{{ contact.message }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <h2>Career Applications</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Message</th>
                    <th>Resume Path</th>
                </tr>
            </thead>
            <tbody>
                {% for app in careers_data %}
                <tr>
                    <td>{{ app.name }}</td>
                    <td>{{ app.email }}</td>
                    <td>{{ app.message }}</td>
                    <td>{{ app.resume_path }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    """, contacts_data=contacts_data, careers_data=careers_data)

@admin_bp.route("/health")
def index():
    return "Admin service is up and running." 