
from flask  import Flask, render_template, request
import pickle
import numpy as np
import sklearn
import jinja2


app = Flask(__name__,template_folder='templates')

model = pickle.load(open('KNN for Crystal Structure.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index1.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        V_A=float(request.form['V_A'])
        V_B=float(request.form['V_B'])
        radius_anion=float(request.form["radius_anion"])
        radius_A=float(request.form["radius_A"])
        radius_B=float(request.form["radius_B"])
        EN_A=float(request.form['EN_A'])
        EN_B=float(request.form['EN_B'])
        bond_length_AO=float(request.form['bond_length_AO'])
        bond_length_BO=float(request.form['bond_length_BO'])
        Electronegativity_radius = float(request.form["Electronegativity_radius"])
        tG = float(request.form["tG"])
        τ = float(request.form["τ"])
        μ = float(request.form["μ"])
        prediction=model.predict([[V_A,V_B,radius_anion,radius_A,radius_B,EN_A,EN_B,bond_length_AO,bond_length_BO,Electronegativity_radius,tG,τ,μ]])
        output=round(prediction[0],13)
        if output<0:
            return render_template('index1.html',pred="Sorry you cannot predict lowest distortion")
        else:
            pred = "The lowest distortion is {}".format(output)
            return render_template('index1.html',pred=pred)
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

