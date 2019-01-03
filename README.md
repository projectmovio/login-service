# Pre requirements

* python3.7
* pip install -r requirements.txt

# Start server

* python run_flask.py
* API base URL: `http://localhost:5000/`

# API docs

For api docs go to http://localhost:5000/apidocs

# Running in docker

* docker build -t login-service:1.0 .
* docker run -p 5000:5000 -d -t login-service:1.0

