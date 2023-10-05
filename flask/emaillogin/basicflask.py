from flask import Flask, render_template,request,redirect, url_for, session
import os 
#from  dbApi import get_users
import  dbApi
from config import db_str_mysql

app = Flask(__name__)

def addUser(data_dict):
    if not data_dict.get("fullname"):
        return{"p_responseMessage": "Please enter the full name"}
    if not data_dict.get("Email",""):
        return{"p_responseMessage": "Please enter the email"}
    if not data_dict.get('Password',""):
        return{"p_responseMessage": "Please enter the Password"}
    users = dbApi.get_users(db_str_mysql)
    all_users = [i[0] for i in users]

    fullname, email, password = data_dict['fullname'],data_dict['Email'],data_dict['Password']
    if email in all_users:
        return{"p_responseMessage": "user already existed"}
    args = [fullname, email, password]
    print(args)
    res = dbApi.insertuser(db_str_mysql,args)
    return {"p_responseMessage":res}


@app.route('/',methods=["GET","POST"])

def index():
    if request.method == 'POST':
        Username = request.form['name']
        email=request.form['Email']
        passwd=request.form['Passwd']
        data_dict = {"fullname":Username,'Email':email,'Password':passwd}
        resp_dict = addUser(data_dict)
        return render_template('verify.html',dea = resp_dict)
        
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port = 5003)
