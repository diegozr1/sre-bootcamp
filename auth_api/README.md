# Implementation Checklist
- [X] API Code
- [X] Services Code
- [X] Unit-tests
- [X] Dockerfile
- [X] It Compiles
- [X] It runs

# Api Services
- Receives a valid username and password and returns a JWT.
- Returns protected data with a valid token, otherwise returns unauthenticated.


# Instructions to run manually

```

python -m venv env

source env/bin/activate

pip install -r requirements.txt

source .env.src

flask run --host=0.0.0.0 --port=8000

```

# run with docker

```
docker-compose up
```