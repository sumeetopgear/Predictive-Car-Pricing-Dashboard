import pickle
import numpy as np
import pandas as pd
from datetime import datetime

def load_model():
    with open('./models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def prepare_input(data_dict, feature_columns):
    input_df = pd.DataFrame([data_dict])

    # one-hot encoding
    # df = pd.get_dummies(df)
    categorical_cols = ['manufacturer', 'type']  
    input_df = pd.get_dummies(input_df, columns=categorical_cols)

    
    # matching training df
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    input_df = input_df[feature_columns]

    return input_df

def predict_price(model, input_features):
    price_prediction = model.predict(input_features)
    return price_prediction[0]

if __name__ == "__main__":
    model = load_model()
    
    example_car = {
        'year': int(input("Enter Car Year: ")),
        'odometer': float(input("Enter Mileage: ")),
        'manufacturer': input("Enter Manufacturer: "),
        'type': input("Enter Car Type: "),
    }
    
    #feature_columns = ['year', 'manufacturer', 'odometer', 'type']
    feature_columns = pd.read_csv('./models/feature_names.csv').squeeze().tolist()
    input_features = prepare_input(example_car, feature_columns)
    
    # current_year = datetime.now().year
    # car_age = current_year - example_car['year']
    # print(f"Vehicle Age: {car_age} years")

    predicted_price = predict_price(model, input_features)
    print(f"Predicted Car Price: ${predicted_price:.2f}")


    
