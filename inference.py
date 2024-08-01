from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import xgboost as xgb
import numpy as np
import google.generativeai as genai
import os
from dotenv import load_dotenv


def generatePrompt(input,output):
    return f"Given the following input: {input}, the model predicts a {output} credit score out of the following options: Poor, Standard, Good. Justify the prediction as to why the model predicted the credit score as {output} based on the given input features. Give a 3-6 line explanation. Do not format the text in anyway."

app = Flask(__name__)
CORS(app) 

load_dotenv()

GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

xgb_model = xgb.XGBClassifier()
xgb_model.load_model('model.json')

def classify(output):
    if output == 0:
        return "Poor"
    elif output == 1:
        return "Standard"
    elif output == 2:
        return "Good"
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        to_predict_list = request.json
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        
        final_array = np.array([to_predict_list])
        
        result = xgb_model.predict(final_array)       
        
        prediction = classify(int(result[0]))
        
        user_input = generatePrompt(request.json,prediction)
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(user_input)
        explanation = response.text        
        
            
        return jsonify({'prediction': prediction, 'explanation':explanation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)