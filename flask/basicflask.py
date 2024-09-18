from flask import Flask, request, jsonify, render_template
from flask.views import MethodView
# from flask_cors import CORS
import api_methods
import dbApi
from config import db_connection
 
app = Flask(__name__)
# CORS(app)
 
class home(MethodView):
    def get(self):
        # return "Welcome to the Home Page!!"
        # return "<h2>Welcome to the Home Page!!</h2>"
        return render_template("home.html")
    def post(self):
        return "Hey There! Welcome to the Home Page.."
app.add_url_rule("/home", view_func=home.as_view("home"))
 
 
if __name__ == "__main__":
    # app.run(debug=True, host='127.0.0.1:5000')
    app.run(debug=True) 