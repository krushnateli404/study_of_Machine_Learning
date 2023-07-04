from flask import Flask,render_template,request
import pickle
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        model = pickle.load(open('lr_model.sav','rb'))
        PT = float(request.form.get('PT'))
        rpm = float(request.form.get('rpm'))
        Nm = float(request.form.get('Nm'))
        min = float(request.form.get('min'))
        TWF = float(request.form.get('TWF'))
        HDF = float(request.form.get('HDF'))
        PWF = float(request.form.get('PWF'))
        OSF = float(request.form.get('OSF'))
        RNF = float(request.form.get('RNF'))
        prediction = model.predict([[PT,rpm,Nm,min,TWF,HDF,PWF,OSF,RNF]])
        print(prediction)
    return render_template('predict.html',predict_text = prediction)

if __name__ == "__main__":
    app.run(debug=True)