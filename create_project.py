import os
from flask import Flask

def create_project(project_name):
    # Create the project directory
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    # Create the app directory
    os.makedirs("app/static", exist_ok=True)
    os.makedirs("app/templates", exist_ok=True)

    # Create __init__.py file
    with open("app/__init__.py", "w") as f:
        f.write("from flask import Flask\n\napp = Flask(__name__)")

    # Create main_page.py file
    with open("app/main_page.py", "w") as f:
        f.write("""
from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")
        """)

    # Create results_page.py file
    with open("app/results_page.py", "w") as f:
        f.write("""
from app import app
from flask import render_template

@app.route("/results")
def results():
    return render_template("results.html")
        """)

    # Create index.html file
    with open("app/templates/index.html", "w") as f:
        f.write("<h1>Welcome to The Tracker - Main Page</h1>")

    # Create results.html file
    with open("app/templates/results.html", "w") as f:
        f.write("<h1>Welcome to The Tracker - Results Page</h1>")

    # Create requirements.txt file
    with open("requirements.txt", "w") as f:
        f.write("Flask==3.0.3")

    print(f"Project '{project_name}' created successfully!")

if __name__ == "__main__":
    project_name = "TheTracker"
    create_project(project_name)
