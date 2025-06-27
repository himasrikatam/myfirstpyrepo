import pickle
from flask_pymongo import PyMongo
from flask import Flask
from pymongo import MongoClient
from flask import request,jsonify,redirect,url_for,request, render_template
from flask_cors import CORS
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
app.config["MONGO_URI"] = "mongodb://localhost:27017/diabetes"
mongo = PyMongo(app)
# client = MongoClient("mongodb://localhost:27017/")
# db = client['diabetes']
# db = PyMongo(app)
# collection = db['health_info']

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict', methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])[0]
    mongo.db.health_info.insert_one({
        'input': features,
        'prediction': int(prediction)
    })
    result = "High Risk" if prediction==1 else "Low Risk"
    return render_template('result.html', prediction=result)
if __name__ =='__main__':
    app.run(debug=True)