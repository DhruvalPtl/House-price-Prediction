import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

 
data = pd.read_csv("house price prediction/house_price_prediction_dataset.csv")
# print(data.shape)

X = data[['num_bedrooms','num_bathrooms','square_footage','age_of_house']]
y = data["house_price"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

joblib.dump(model,"house price prediction/house_price_predic.pkl")
print("Model saved successfully!")
y_predict = model.predict(X_test)

mean_sq_error = mean_squared_error(y_test,y_predict)
r2_sco = r2_score(y_test,y_predict)
 
print("mean square error:",mean_sq_error)
print("r2 score(accuarcy):",r2_sco)

new_data = pd.DataFrame([[3,2,1500,20]],columns=['num_bedrooms','num_bathrooms','square_footage','age_of_house'])
print(model.predict([[3,2,1500,20]]))
print(model.predict(new_data))
print(data['num_bathrooms'].min())
print(data['num_bedrooms'].min())
print(data['square_footage'].min())
print(data['age_of_house'].min())
j = 0
for i in data['square_footage']:
    if i < 800:
        j += 1 
print(j)
print(data['house_price'].max())