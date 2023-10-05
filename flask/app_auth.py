from flask import Flask, make_response, jsonify, request, redirect, url_for
from flask.views import MethodView
import db_api
from config import db_connection

app = Flask(__name__)

class add_user(MethodView):

     def get(self):
         return "responds to get a requests"

     def post(self):
         data_dict=request.get_json()
         doc_id = data_dict.get("id")
         full_name  = data_dict.get("full_name")
         Email = data_dict.get("email")
         passwd = data_dict.get("password")
         s = db_api.create_info(db_connection, doc_id, full_name, Email, passwd)
         res = db_api.get_info(db_connection,Email)
         #m = db_api.update_user_info(db_connection,doc_id)
         #db_api.delete_info (db_connection,doc_id)
         res1 = {"status": "value updated"}
         return jsonify(res)

app.add_url_rule("/add_user",view_func=add_user.as_view("add_user"))


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port = 3306)
    app.run(debug=True, host='0.0.0.0', port = 5000)
