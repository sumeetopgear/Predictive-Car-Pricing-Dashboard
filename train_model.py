import pickle
from prepare_data import load_and_preprocess_data
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_and_save_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    with open('./models/model.pkl', 'wb') as file:
        pickle.dump(model, file)

    print("Model trained and saved successfully!")

def evaluate_model(X_test, y_test):
    with open('./models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_preprocess_data('cleaned_vehicles.csv')
    train_and_save_model(X_train, y_train)
    evaluate_model(X_test, y_test)
