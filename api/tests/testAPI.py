from flask import json
from app import app

# Run this in the api/ dir with
# python -m pytest --rootdir=`pwd` tests/api-test.py -v


def test_add_note():
    response = app.test_client().post(
        "/api/v1.0/notes",
        data=json.dumps({"body": "Thnk of more test notes!"}),
        content_type="application/json",
    )

    assert response.status_code == 201


def test_get_one_note():
    response = app.test_client().get("/api/v1.0/notes/1")

    assert response.status_code == 200


def test_get_one_note_bad():
    response = app.test_client().get("/api/v1.0/notes/10")

    assert response.status_code == 404


def test_get_all_notes():
    response = app.test_client().get("/api/v1.0/notes")

    assert response.status_code == 200


def test_delete_note():
    response = app.test_client().delete("/api/v1.0/notes/1")

    assert response.status_code == 200
