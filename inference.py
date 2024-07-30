import xgboost as xgb
import numpy as np

xgb_model = xgb.XGBClassifier()
xgb_model.load_model('model.json')

def classify(output):
    if output == 0:
        return "Poor"
    elif output == 1:
        return "Standard"
    elif output == 2:
        return "Good"
    
def predict():
    features_array = ["Annual_Income","Monthly_Inhand_Salary","Outstanding_Debt","Monthly_Balance","Interest_Rate","Delay_from_due_date","Num_Credit_Inquiries","Amount_invested_monthly","Num_of_Delayed_Payment","Total_EMI_per_month","Changed_Credit_Limit","Credit_Mix"]
    input_array = []
    try:
        for feature in features_array:
            feature = feature.replace('_',' ')
            value = input(f"Enter the following feature - {feature}: ")
            if feature in ["Interest_Rate","Delay_from_due_date","Credit_Mix"]:
                value = int(value)
            else:
                value = float(value)
            input_array.append(value)

        features = np.array([input_array])  

        prediction = xgb_model.predict(features)
        output = classify(prediction[0])
        print(f"Predicted credit score: {output}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    predict()
