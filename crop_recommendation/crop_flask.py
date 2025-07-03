import pickle
from flask_pymongo import PyMongo
from flask import Flask
from flask import request, render_template

app = Flask(__name__)
model, le = pickle.load(open('model_pickle', 'rb'))
app.config["MONGO_URI"] = "mongodb://localhost:27017/cropsDB"
mongo = PyMongo(app)
@app.route('/')
def home():
    return render_template('crop.html')
@app.route('/result', methods=['POST'])
def result():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])[0]
    predicted_crop = le.inverse_transform([prediction])[0]
    mongo.db.crop_info.insert_one({
        'input': features,
        'prediction': predicted_crop
    })
    return render_template('predict.html',prediction = predicted_crop)
if __name__ == '__main__':
 app.run(debug=True)
# go to  http://127.0.0.1:5000 to see the output