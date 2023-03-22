curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "username", "password": "password"}' \
  http://0.0.0.0:8000/token/

curl -X GET\
  -H "Authorization: Bearer <your token>" \
  http://0.0.0.0:8000/documents/

  curl -X GET\
  -H "Authorization: Bearer <your token>" \
  http://0.0.0.0:8000/documents/<id>/


curl -X GET\
    -H "Authorization: Bearer <your token>" \
    -F 'item_count=<count>' -F 'sorting_column=<column name>'  http://0.0.0.0:8000/documents/file/<id>/