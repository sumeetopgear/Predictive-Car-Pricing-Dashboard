# CS 498 E2E Final Project (sp24) repo for NetID: sumeetj2

GitHub username at initialization time: sumeetj2

# Car Price Prediction Dashboard

In the automotive industry, pricing or judging the value of used cars accurately can be challenging due to a vast multitude of factors such as mileage, model year, vehicle condition and many more. The Used Car Price Prediction and Listing Dashboard seeks to alleviate this issue and is designed to assist car buyers or sellers make informed decisions when dealing with used cars. The dashboard uses a ML model to provide accurate predictions of car prices based on various parameters, to enable users to judge a fair pricing of a vehicle for themselves, by inputting their desired parameters. 

**Due to github space constraints**, this dashboard is basic and trained on a truncated dataset, but future improvements should include heavy training with much more complex parameters i.e Vehicle Model. If you wish to train it on the full dataset kindly download it at the below kaggle link.

### Context
This dashboard is a combination of 2 MPs and it utilizes a predictive model trained on historical car sales data(https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data?resource=download). A RandomForestRegressor was used as the model of choice to train a model on basic parameters such as vehicle manufacturer(eg. Honda, Ford etc), mileage(mi), vehicle age, and type(eg.sedan, pickup etc). The trained model (model.pkl) is stored in the models folder. 

Following this the used car listing and the prediction model is hosted on a interactive web dashboard, using Shiny. 

## Setup Instructions - Please follow these steps carefully to ensure the Prediction Dashboard runs properly!!
### Basic Steps
1. Clone the repository to your local machine.
2. Activate your venv
  ```
    source .venv/bin/activate
  ```
3. Install the required dependencies
```
   uv pip install -r requirements.txt.
```

### KEY STEPS
From folder **"src"** run the following files in this order:

4. Run _prepare_data.py_ --> Check that _**feature_names.csv**_ appears under **models** folder
   ```
   python ./src/prepare_data.py
   ```
5. Run _train_model.py_ --> Check that _**"model.pkl"**_ appears under **models** folder
   ```
   python ./src/train_model.py
   ```
6. Run _predict_price.py_ --> Fill in the below data
   ```
   python ./src/predict_price.py
   ```
   Upon running predict_price.py, you will be prompted to test if the prediction model is running. Enter the following values or similar (kindly follow a similar format):
   
       - Enter Car Year: 2020
       - Enter Mileage: 130000
       - Enter Manufacturer: Bmw
       - Enter Car Type: sedan

   You should be able to see a Predicted Car Price indicating the model is working. Great start!

7. Run the dashboard application using python app.py or Run Shiny app (with Shiny VSCode extension)
8. You may access the dashboard in your web browser at http://localhost:8050 or in the link provided

## Usage Examples
- Explore Used Car Listings: Browse through the available used car listings below to find vehicles of interest. You may wish to use the filter to view listings as desired.
- Utilize Prediction Tool: Use the Prediction Tool in the sidebar to estimate the price of a specific car based on its parameters, and compare it to the listing to judge if it's a fair valuation of the vehicle.
- Compare Predicted Prices: Compare predicted prices for different permutations, to identify potential bargains or overpriced listings.

## Dataset Obtained from:
- https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data?resource=download 
- Craigslist

### Screenshot of dashboard
![Example Image](screenshot.png)

Contributors:
Sumeet Jagtap - sumeetj2
