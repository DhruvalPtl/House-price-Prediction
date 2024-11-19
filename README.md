# House Price Prediction with GUI

🏡 **House Price Prediction with GUI** is a Python-based desktop application that predicts house prices using a trained machine learning model. The project includes a clean and interactive GUI built with PyQt6, paired with a predictive model trained using Linear Regression.

## Features
- **Machine Learning Model**:
  - Built using a dataset of housing features like the number of bedrooms, bathrooms, square footage, and house age.
  - Trained using Linear Regression, achieving accurate predictions.
- **Custom GUI**:
  - Developed with PyQt6 for a user-friendly interface.
  - Inputs include spin boxes for easy interaction and a button to predict house prices in real time.
- **Dynamic Predictions**:
  - Takes user inputs such as bedrooms, bathrooms, square footage, and house age to predict prices instantly.

## Technology Stack
- **Programming Language**: Python
- **Libraries**:
  - **For Model Training**: Pandas, NumPy, Scikit-learn, Joblib
  - **For GUI**: PyQt6
- **Model**: Linear Regression (trained using Scikit-learn)

## Project Workflow
### 1. Model Training
- **Dataset**: `house_price_prediction_dataset.csv` with features such as:
  - Number of bedrooms
  - Number of bathrooms
  - Square footage
  - Age of house
- **Training Process**:
  - Split data into training and testing sets (80:20 ratio).
  - Train the model using Scikit-learn's `LinearRegression`.
  - Evaluate performance with metrics like Mean Squared Error (MSE) and R² score.
  - Save the trained model as `house_price_predic.pkl` using Joblib.

### 2. GUI Integration
- **PyQt6 GUI**:
  - Provides an intuitive interface for user inputs.
  - Displays the predicted house price instantly.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/DhruvalPtl/House-price-Prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd House-price-Prediction
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. To train the model:
   ```bash
   python house_price_predi_gui.py
   ```
5. To run the application:
   ```bash
   python ui_house_price.py
   ```

## How It Works
1. The GUI collects input values: bedrooms, bathrooms, square footage, and house age.
2. These inputs are passed to the saved model (`house_price_predic.pkl`).
3. The model returns a predicted price, which is displayed on the GUI.

## Results
- **Model Performance**:
  - Mean Squared Error: [Add MSE Value]
  - R² Score: [Add R² Score]

## Future Enhancements
- Add support for additional features like location-based adjustments.
- Enhance the GUI with better visualization tools.
- Explore advanced machine learning models for improved accuracy.

## Screenshots
![Screenshot (273)](https://github.com/user-attachments/assets/e39eb3d2-b081-4d85-b5a8-c035503a530f)
