from flask import Flask, render_template, url_for, request, redirect, jsonify
from werkzeug.utils import secure_filename
import pickle


app = Flask(__name__)
model = "Model Example" #pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)

    output = "Pneumonia" #round(prediction[0], 2)
    og_image = "https://prod-images-static.radiopaedia.org/images/157210/332aa0c67cb2e035e372c7cb3ceca2_jumbo.jpg"

    return render_template('index.html', prediction_text='You have {} with 85% probability'.format(output), img_src = og_image)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(port=12000, debug=True)