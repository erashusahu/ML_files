from flask import Flask,jsonify,render_template,request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application =Flask(__name__)

app=application

# import ridge regressor and standard pickel

ridge_model=pickle.load(open(r"ProjectRegression\Ridge.pkl","rb"))
standard_sclaer=pickle.load(open(r"ProjectRegression\scaler.pkl","rb"))


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
        if request.method=='POST':
            try:
                field1 = request.form.get('field1')
                field2 = request.form.get('field2')
                field3 = request.form.get('field3')
                field4 = request.form.get('field4')
                field5 = request.form.get('field5')
                field6 = request.form.get('field6')
                field7 = request.form.get('field7')
                field8 = request.form.get('field8')
                field9 = request.form.get('field9')
                fields = [field1, field2, field3, field4, field5, field6, field7, field8, field9]
                if any(f is None or f.strip() == '' for f in fields):
                    return render_template("home.html", results="Please fill all fields.")
                field1 = float(field1)
                field2 = float(field2)
                field3 = float(field3)
                field4 = float(field4)
                field5 = float(field5)
                field6 = float(field6)
                field7 = float(field7)
                field8 = float(field8)
                field9 = float(field9)
                new_data = np.array([[field1, field2, field3, field4, field5, field6, field7, field8, field9]])
                result = ridge_model.predict(new_data)
                return render_template("home.html", results=result[0])
            except Exception as e:
                return render_template("home.html", results=f"Error: {str(e)}")
        else:
           return render_template("home.html", results=None)

if __name__ == "__main__":
    app.run(debug=True)