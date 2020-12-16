import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    data1 = request.form.get('rating')
    data2 = request.form.get('age')
    data3 = request.form.get('role1')
    data4 = request.form.get('role2')
    data5 = request.form.get('role3')
    data6 = request.form.get('role4')
    data7 = request.form.get('skill1')
    data8 = request.form.get('skill2')
    data9 = request.form.get('skill3')
    data10 =request.form.get('skill4')

    if(data3=="Data Scientist"):
        data3=1
        data4=0
        data5=0
        data6=0
    
    elif(data2=="Data Analyst"):
        data3=0
        data4=1
        data5=0
        data6=0

    elif(data3=="Data Engineering"):
        data3=0
        data4=0
        data5=1
        data6=0
    
    else:
        data3=0
        data4=0
        data5=0
        data6=1


    count=0
    for x in range(4):
        if(data7=="python_job"):
            count=1
        if(data8=="excel_job"):
            count=2
        if(data9=="sql_job"):
            count=3
        if(data10=="tableau_job"):
            count=4
    
    if(count==1):
        data7=1
        data8=0
        data9=0
        data10=0
    
    if(count==2):
        data7=1
        data8=1
        data9=0
        data10=0

    if(count==3):
        data7=1
        data8=1
        data9=1
        data10=0

    if(count==4):
        data7=1
        data8=1
        data9=1
        data10=1

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)