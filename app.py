from flask import Flask, render_template, request
import pickle
import numpy as np
from logger import Logger
from database import *
from flask_cors import CORS, cross_origin
from logger import Logger
from database import Connector
import warnings
warnings.filterwarnings('ignore')

 

app = Flask(__name__)
model = pickle.load(open('extratreemodel.sav', 'rb'))
print("Inside model")
# scalar = pickle.load(open('./Scaler/Scalar.pkl', 'rb'))
# print("inside scalar")
logging.info('INFO', 'Pickle Model Loaded')
logging = Logger('logFiles/test.log')

@cross_origin()
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@cross_origin()
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        logging.info('INFO', 'Requested method : POST')

        age = int(request.form['age'])

        edu = (request.form['education'])
        if edu == 'Higher Studies':
            edu = 0
        elif edu == 'Bachelors':
            edu = 1
        elif edu == 'Associate':
            edu = 2
        elif edu == 'Prof-School':
            edu = 3
        elif edu == 'Diploma':
            edu = 4
        else:
            edu = 5

        gain = (request.form['gain'])
        if gain == 'Yes':
            gain = 1
        else:
            gain = 0

        loss = (request.form['loss'])
        if loss == 'Yes':
            loss = 0
        else:
            loss = 1

        wrk_cls = (request.form['workclass'])
        if wrk_cls == 'Private':
            wrk_cls = 0, 0, 0
        elif wrk_cls == 'Government':
            wrk_cls = 0, 0, 1
        elif wrk_cls == 'SelfEmployeed':
            wrk_cls = 0, 1, 0
        else:
            wrk_cls = 1, 0, 0

        status = (request.form['maritialstatus'])
        if status == 'Married':
            status = 0
        else:
            status = 1

        race = (request.form['race'])
        if race == 'White':
            race = 0, 0
        elif race == 'Brown':
            race = 1, 0
        else:
            race = 0, 1

        gen = (request.form['gender'])
        if gen == 'Male':
            gen = 1
        else:
            gen = 0

        hours = (request.form['hours'])
        if hours == 'ideal':
            hours = 0, 0
        elif hours == 'over':
            hours = 1, 0
        else:
            hours = 0, 1

        country = (request.form['country'])

        if country == 'US':
            country = 1
        else:
            country = 0

        col = ([[age, edu, gain, loss, *wrk_cls, status, *race, gen, *hours, country]])
        
        # scaled_col = scalar.transform(col)
        # print(scaled_col)
        prediction = model.predict(col)
        print(prediction)

        
        if prediction == np.array(1):
            logging.info('INFO', 'Output displayed!')
            return render_template('predict.html', Prediction_text = "The Salary of an Individual is More than 50K")
        else:
            logging.info('INFO', 'Output displayed!')
            return render_template('predict.html', Prediction_text = "The Salary of an Individual is Less than 50K")

    else:
        return render_template('index.html')


@app.route("/DatabasePage", methods = ['GET','POST'])
def test():
    heading = ("age", "education", "gain", "loss","workclass","maritialstatus", "race", "gender", "country", "hours")
    data = Connector()
    return render_template('databasedata.html', heading=heading, data=data.getData())



if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")