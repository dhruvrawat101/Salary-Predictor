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
    data1 = float(request.get_data('rating'))
    data2 = float(request.get_data('age'))
    data3 = request.get_data('a')
    data4 = request.get_data('b')
    data5 = request.get_data('c')
    data6 = request.get_data('d')
    data7 = request.get_data('e')
    data8 = request.get_data('f')
    data9 = request.get_data('g')
    data10 =request.get_data('h')

    if(data3=="DataScientist"):
        data3=1
        data4=0
        data5=0
        data6=0
    
    elif(data2=="DataAnalyst"):
        data3=0
        data4=1
        data5=0
        data6=0

    elif(data3=="DataEngineering"):
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
        if(data7=="on"):
            count=1
        if(data8=="on"):
            count=2
        if(data9=="on"):
            count=3
        if(data10=="on"):
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


