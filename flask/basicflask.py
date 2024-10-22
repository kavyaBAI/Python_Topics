from flask import Flask, request, jsonify, render_template
from flask.views import MethodView
# from flask_cors import CORS
import api_methods
import dbApi
from config import db_connection
 
app = Flask(__name__)
# CORS(app)
###this for complete full stack application to run like this###
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

############################################################################
#to create a endpoint from backend to run the endpoint in postman 
from flask import Flask, make_response, jsonify, request, redirect, url_for, send_from_directory, send_file
from flask.views import MethodView
from flask_cors import CORS
app = Flask(__name__)
class UploadDocuments(MethodView):
    def get(self):
        """ Responds to GET requests """
        return "Responding to a GET request"
    def post(self):
        data_dict = request.form #when u r uploading any files or documents 
        data_dict = request.get_json() # to get the payload in dictinnary from json to dict 
        file_obj = request.files.get('file_obj')
        def_dict = fd.upload_documents(data_dict,file_obj)
        return def_dict 
        return jsonify(def_dict) #will convert dict to json 

app.add_url_rule("/InputChannel/UploadDocuments", view_func=UploadDocuments.as_view("UploadDocuments"))



