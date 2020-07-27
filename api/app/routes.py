from flask import abort, make_response, request, jsonify
from flask_restx import Resource, fields, marshal
from app import app, api

notes = [{"id": 1, "body": "Buy car parts"}, {"id": 2, "body": "Learn Elastic better"}]

notes_fields = api.model("Resource", {"id": fields.Integer, "body": fields.String})


# So nothing explodes when we don't find a note
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


# Default route
# Not in use right now, see below link - Applises to flask-restx too
# https://github.com/noirbizarre/flask-restplus/issues/247
# @api.route("/")
# class Index(Resource):
#     def get(self):
#         return "You're not looking for me...Use the api kid!"


# NotesMain class - Handles new notes and getting all notes
@api.route("/notes")
class NotesMain(Resource):
    @api.doc("list all notes")
    def get(self):
        return jsonify({"notes": notes})

    @api.expect(notes_fields)
    @api.doc(responses={201: "Created", 400: "Validation Error"})
    def post(self):
        if not request.json or not "body" in request.json:
            abort(400)
        note = {"id": notes[-1]["id"] + 1, "body": request.json["body"]}
        notes.append(note)
        return {"note": marshal(note, notes_fields)}, 201


# NotesHandler class handles individual notes
@api.route("/notes/<int:id>")
@api.response(404, "ID Not Found")
class NotesHandler(Resource):
    def get(self, id):
        note = [note for note in notes if note["id"] == id]
        if len(note) == 0:
            return make_response(jsonify({"error": "Not a valid ID"}), 404)
        return jsonify({"note": note[0]})

    @api.doc("delete a specific note")
    def delete(self, id):
        note = [note for note in notes if note["id"] == id]
        if len(note) == 0:
            return make_response(jsonify({"error": "Not a valid ID"}), 404)
        response = {"status": "OK"}
        remove_note(id)
        response["message"] = "Note removed!"
        return jsonify(response)


# Delete helper - Need to move this out of routes!
def remove_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return True
    return False
