#!/bin/bash

echo "Get all Notes"
curl http://127.0.0.1:5000/api/v1.0/notes
echo "Add a note"
curl -H "Content-Type: application/json" -X POST -d '{"body":"Add the ability to remove notes!"}' http://localhost:5000/api/v1.0/notes
echo "Get all Notes"
curl http://127.0.0.1:5000/api/v1.0/notes
echo "Delete a Note"
curl -XDELETE http://127.0.0.1:5000/api/v1.0/notes/2
echo "Get all Notes"
curl http://127.0.0.1:5000/api/v1.0/notes
echo "Delete a fake Notes"
curl -XDELETE http://127.0.0.1:5000/api/v1.0/notes/5
