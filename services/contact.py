from flask import Blueprint, request, jsonify, redirect, url_for, flash, render_template
from .models import db, Contact

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['POST'])
def contact():
    if request.is_json:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

    if not name or not email or not message:
        if request.is_json:
            return jsonify({'status': 'error', 'message': 'Missing fields'}), 400
        else:
            return render_template('contact.html', error="Please fill all fields.")

    try:
        contact = Contact(name=name, email=email, message=message)  # date auto-set
        db.session.add(contact)
        db.session.commit()
        if request.is_json:
            return jsonify({'status': 'success', 'message': 'Contact form submitted successfully'}), 201
        else:
            return render_template('contact.html', success="Thank you for contacting us!")
    except Exception as e:
        db.session.rollback()
        if request.is_json:
            return jsonify({'status': 'error', 'message': str(e)}), 500
        else:
            return render_template('contact.html', error="Something went wrong. Please try again.")

@contact_bp.route('/admin/contacts', methods=['GET'])
def admin_contacts():
    # In a real application, this should be login-protected
    contacts = Contact.query.all()
    contact_list = []
    for contact in contacts:
        contact_list.append({
            'id': contact.id,
            'name': contact.name,
            'email': contact.email,
            'message': contact.message,
            'date': contact.date
        })
    return jsonify({'status': 'success', 'contacts': contact_list}), 200

@contact_bp.route('/admin/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return {'status': 'error', 'message': 'Contact not found'}, 404
    try:
        db.session.delete(contact)
        db.session.commit()
        return {'status': 'success', 'message': 'Contact deleted'}
    except Exception as e:
        db.session.rollback()
        return {'status': 'error', 'message': str(e)}, 500

@contact_bp.route('/')
def contact_home():
    return "Contact Home" 