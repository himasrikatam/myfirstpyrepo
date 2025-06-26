import pymongo
from flask import Flask
from flask_pymongo import PyMongo
from flask import request,jsonify,redirect,url_for,request, make_response
from flask_cors import CORS
from bson.json_util import dumps
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient['mydatabase']
# mycul = mydb['new_db']
app = Flask(__name__)
# cors = CORS(app)
# app.config["CORS_HEADERS"] = "Content-Type"
# @app.route('/success/<name>') # http://127.0.0.1:5000/success/himasri
# def success(name):
#     return "hello %s" %name
# @app.route('/login',methods=['POST','GET'])
# def login():
#     if request.method =='POST':
#         user = request.form['nm']
#         return redirect(url_for('success',name=user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success',name=user))
# if __name__ == '__main__':
    # app.run() # output => hello himasri
app.config["MONGO_URI"] = "mongodb://localhost:27017/new_db"
# db = PyMongo(app).db
mongo = PyMongo(app)
# @app.route("/")
# def hello_world():
#     # db.students.insert_one({"name":"Prasanna"})
#     A = list(db.students.find({},{"_id":0,"name":1}))
#     for i in range(len(A)):
#         print(f"Name of {i+1}th document: ", A[i])
#     return "Hello World!"
# @app.route("/name")
# def getNames():
#     B = db.students.find({},{"_id":0,"name":1})
#     names=[]
#     i=1
#     for stu in B:
#         if "name" in stu: 
#          names.append(f"Name of the {i}th document: {stu['name']}")
#          i+=1
#     return names
# @app.route("/delete/<name>")
# def deleteName(name):
#    db.students.delete_one({"name": name})
#    return getNames()
# POST
@app.route('/add',methods=['POST'])
def add_doc():
  _json = request.json
  _name = _json['name']
  _age = _json['age']
  _salary = _json['salary']
  if _name and _age and _salary and request.method=='POST':
    id = mongo.db.students.insert_one({"name":_name, 'age':_age, "salary":_salary })
    return make_response(jsonify(message="Document successfully inserted"), 200)
  else:
    return not_found()
@app.errorhandler(404)
def not_found(error=None):
  message ={
    'status': 404,
    'message':"Not Found" + request.url
  }
  resp = jsonify(message)
  resp.status_code = 404
  return resp
# GET
@app.route('/studentNameList')
def getAllStudents():
  stuList = mongo.db.students.find({},{"name":1,"_id":0}) # returns only student names
  resp = dumps(stuList)
  return resp
@app.route('/student/<id>')
def getStudentDetails(id):
  stuDetails = mongo.db.students.find_one({"_id": ObjectId(id)}) # returns doucument of that particular student
  resp = dumps(stuDetails)
  return resp
# DELETE
@app.route('/delete/<id>',methods=['DELETE'])
def deleteStudent(id):
  mongo.db.students.delete_one({"_id": ObjectId(id)})
  return make_response(jsonify(message='Student deleted successfully!'), 200)
# PUT
@app.route('/updateStudent/<id>', methods=['PUT'])
def updateStudentDetails(id):
  _id = id
  _json = request.json
  _name = _json['name']
  _age = _json['age']
  _salary = _json['salary']
  if _name and _age and _salary and request.method=='PUT':
    mongo.db.students.update_one({"_id":ObjectId(id)}, { '$set':{"name":_name, "age":_age}})
  return make_response(jsonify(message='Student details are updated successfully!'), 200)

#   else:
#     return not_found()

if __name__ == "__main__":
 app.run(debug=True)