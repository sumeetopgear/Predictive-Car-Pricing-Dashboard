import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def load_and_preprocess_data(filepath):
    df = pd.read_csv('./data/cleaned_vehicles.csv')
    columns = ['price', 'year', 'manufacturer', 'odometer', 'type']
    df = df[columns]
    df.dropna(inplace=True)
    
    # one-hot encoding
    categorical_cols = ['manufacturer', 'type']
    df = pd.get_dummies(df, columns=categorical_cols)
    
    X = df.drop('price', axis=1)
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    feature_names = X_train.columns
    pd.Series(feature_names).to_csv('./models/feature_names.csv', index=False)
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_preprocess_data('cleaned_vehicles.csv')
    print("Data loaded")
