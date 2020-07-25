from flask import abort, make_response, request, jsonify
from flask_restful import Resource, reqparse, fields, marshal
from app import app, api

notes = [
    {
        'id': 1,
        'body': 'Buy car parts'
    },
    {
        'id': 2,
        'body': 'Learn Elastic better'
    }
]

note_fields = {
    'id': fields.String,
    'body': fields.String
}


# So nothing explodes when we don't find a note
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# Default route
@app.route('/')
def index():
    return "You're not looking for me...Use the api kid!"

# NotesMain class - Handles new notes and getting all notes
class NotesMain(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('body', type=str, default="", location='json')
        super(NotesMain, self).__init__()

    def get(self):
        return jsonify({'notes': notes})

    def post(self):
        if not request.json or not 'body' in request.json:
            abort(400)
        note = {
            'id': notes[-1]['id'] + 1,
            'body': request.json['body']
        }
        notes.append(note)
        return {'note': marshal(note, note_fields)}, 201

# NotesHandler class handles individual notes
class NotesHandler(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('body', type=str, default="", location='json')
        super(NotesHandler, self).__init__()
    
    def get(self, id):
        note = [note for note in notes if note['id'] == id]
        if len(note) == 0:
            return make_response(jsonify({'error': 'Not a valid ID'}), 404)
        return jsonify({'note': note[0]})
    
    def delete(self, id):
        note = [note for note in notes if note['id'] == id]
        if len(note) == 0:
            return make_response(jsonify({'error': 'Not a valid ID'}), 404)
        response = {'status': 'OK'}
        remove_note(id)
        response['message'] = 'Note removed!'
        return jsonify(response)

# Delete helper
def remove_note(note_id):
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            return True
    return False

# The API route defined
api.add_resource(NotesMain, '/api/notes', endpoint='notes')
api.add_resource(NotesHandler, '/api/notes/<int:id>', endpoint='task')
