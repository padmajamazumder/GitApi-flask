import json
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("username")

        response = requests.get(f"https://api.github.com/users/{name}")

        if response.status_code == 200:
            data = response.json()
            return render_template("index.html", name=data.get("name"), profile_image=data.get("avatar_url"),
                                   bio=data.get("bio"), location=data.get("location"),
                                   followers=data.get("followers"), following=data.get("following"),
                                   link=data.get("html_url"), repos=data.get("public_repos"))
        else:
            return f'couldn not work with that status code: {response.status_code}'

    return render_template("index.html")

if __name__ == "__main":
    app.run()


# import json
# from flask import Flask, render_template, request
# import requests  # You were missing this import

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         name = request.form.get("username")

#         response = requests.get(f"https://api.github.com/users/{name}")

#         # Check the status code
#         if response.status_code == 200:
#             # Decode the JSON response
#             data = response.json()

#             # Render the template and pass data to it
#             return render_template("index.html", name=data.get("name"), profile_image=data.get("avatar_url"),
#                                    bio=data.get("bio"), location=data.get("location"),
#                                    followers=data.get("followers"), following=data.get("following"),
#                                    link=data.get("html_url"), repos=data.get("public_repos"))
#         else:
#             return f'Request failed with status code: {response.status_code}'

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run()
