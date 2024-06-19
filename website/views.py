from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from flask import request, flash
from .models import Note
from . import db
import json
from sqlalchemy.exc import IntegrityError

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            existing_note = Note.query.filter_by(data=note, user_id=current_user.id).first()
            if existing_note:
                flash('Note already exists.', category='error')
            else:
                try:
                    new_note = Note(data=note, user_id=current_user.id)
                    db.session.add(new_note)
                    db.session.commit()
                    flash('Note added!', category='success')
                except IntegrityError as e:
                    db.session.rollback()
                    flash('Error: Unable to add note.', category='error')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)  # this function expects a JSON from the INDEX.js file
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
