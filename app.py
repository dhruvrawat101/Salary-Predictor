from flask import Flask, render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
#app = Flask(__name__, template_folder="template")


@app.route('/')
def gh():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.get_data('rating')
    data2 = request.get_data('age')
    data3 = request.get_data('role1')
    data4 = request.get_data('role2')
    data5 = request.get_data('role3')
    data6 = request.get_data('role4')
    data7 = request.get_data('skill1')
    data8 = request.get_data('skill2')
    data9 = request.get_data('skill3')
    data10 =request.get_data('skill4')

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



#second way
#return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)


