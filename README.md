Sending a POST Request to Create a User:
```bash
curl -X POST "http://localhost:8000/create_user" -H "Content-Type: application/json" -d '{
    "login": "example@example.com",
    "password": "password123",
    "project_id": "project_id",
    "env": "prod",
    "domain": "regular"
}'
```
Sending a GET Request to Get All Users:
```bash
curl -X GET "http://localhost:8000/get_users"
```
Sending a POST Request to Acquire Lock for a User:
```bash
curl -X POST "http://localhost:8000/acquirejock" -H "Content-Type: application/json" -d '{
    "user_id": "user_id_to_lock"
}'
```
Sending a POST Request to Release Lock for a User:
```bash
curl -X POST "http://localhost:8000/releasejock" -H "Content-Type: application/json" -d '{
    "user_id": "user_id_to_release"
}'
```