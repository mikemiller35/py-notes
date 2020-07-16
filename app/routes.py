from flask import abort, make_response, request
from flask.json import jsonify
from app import app

notes = [
    {
        'id': 1,
        'body': 'Buy car parts'
    },
    {
        'id': 2,
        'title': 'Learn Elastic better'
    }
]


# So nothing explodes when we don't find a note
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# Default route
@app.route('/')
def index():
    return "You're not looking for me...Use the api kid!"


# API Goodness
# Get ALL notes
@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify({'notes': notes})


# Get a particular note
@app.route('/api/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = [note for note in notes if note['id'] == note_id]
    if len(note) == 0:
        return make_response(jsonify({'error': 'Not a valid ID'}), 404)
    return jsonify({'note': note[0]})


# Adding a note
@app.route('/api/notes', methods=['POST'])
def add_note():
    if not request.json or not 'body' in request.json:
        abort(400)
    note = {
        'id': notes[-1]['id'] + 1,
        'body': request.json['body']
    }
    notes.append(note)
    return jsonify({'note': note}), 201
