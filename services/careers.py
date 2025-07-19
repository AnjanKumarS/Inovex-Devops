from flask import Blueprint, request, jsonify, current_app, render_template
from werkzeug.utils import secure_filename
import os
from .models import db, Application

careers_bp = Blueprint('careers', __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads')
UPLOAD_FOLDER = os.path.abspath(UPLOAD_FOLDER)

@careers_bp.route('/apply', methods=['POST'])
def apply():
    role = request.form.get('role')
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    resume = request.files.get('resume')

    if not name or not email or not resume:
        if request.is_json:
            return jsonify({'status': 'error', 'message': 'Missing required fields (name, email, resume)'}), 400
        else:
            return render_template('careers.html', error="Please fill all required fields.")

    if resume and resume.filename:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        filename = secure_filename(resume.filename)
        resume_path = os.path.join(UPLOAD_FOLDER, filename)
        resume.save(resume_path)
    else:
        if request.is_json:
            return jsonify({'status': 'error', 'message': 'Resume file not provided or invalid'}), 400
        else:
            return render_template('careers.html', error="Resume file not provided or invalid.")

    try:
        application = Application(role=role, name=name, email=email, message=message, resume_path=resume_path)  # date auto-set
        db.session.add(application)
        db.session.commit()
        if request.is_json:
            return jsonify({'status': 'success', 'message': 'Application submitted successfully'}), 201
        else:
            return render_template('careers.html', success="Your application has been submitted! We will contact you soon.")
    except Exception as e:
        db.session.rollback()
        if request.is_json:
            return jsonify({'status': 'error', 'message': str(e)}), 500
        else:
            return render_template('careers.html', error="Something went wrong. Please try again.")

@careers_bp.route('/admin/applications', methods=['GET'])
def admin_applications():
    applications = Application.query.all()
    application_list = []
    for app in applications:
        application_list.append({
            'id': app.id,
            'role': app.role,
            'name': app.name,
            'email': app.email,
            'message': app.message,
            'resume_path': app.resume_path,
            'date': app.date
        })
    return jsonify({'status': 'success', 'applications': application_list}), 200

@careers_bp.route('/admin/applications/<int:id>', methods=['DELETE'])
def delete_application(id):
    app = Application.query.get(id)
    if not app:
        return {'status': 'error', 'message': 'Application not found'}, 404
    try:
        db.session.delete(app)
        db.session.commit()
        return {'status': 'success', 'message': 'Application deleted'}
    except Exception as e:
        db.session.rollback()
        return {'status': 'error', 'message': str(e)}, 500

@careers_bp.route('/')
def careers_home():
    return "Careers Home" 