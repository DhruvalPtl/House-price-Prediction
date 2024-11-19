# House Price Prediction Application

🏡 **House Price Prediction Application** is a project that predicts house prices using a trained machine learning model. It includes both a **Streamlit Web App** for online use and a **PyQt Desktop GUI** for offline functionality, offering flexibility for various user preferences.

---

## Features
- **Streamlit Web App**:
  - Accessible via a web browser for seamless interaction.
  - Input fields for bedrooms, bathrooms, square footage, and house age.
  - Instant predictions with a user-friendly interface.
- **PyQt GUI**:
  - Desktop application with a clean and modern design.
  - Spin boxes for inputs and dynamic predictions.
- **Machine Learning Model**:
  - Trained using Linear Regression on housing data.
  - Accurate predictions based on user inputs.

---

## Technology Stack
- **Programming Language**: Python
- **Libraries**:
  - **Streamlit**: For web application development.
  - **PyQt6**: For desktop GUI development.
  - **Scikit-learn**: For machine learning model training.
  - **Pandas** and **NumPy**: For data processing.
  - **Joblib**: For saving and loading the model.

---

## Installation
### Clone the Repository
```bash
git clone https://github.com/DhruvalPtl/house-price-prediction.git
cd house-price-prediction
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. Streamlit Web App
1. Ensure the trained model file `house_price_predic.pkl` is in the same directory as `app.py`.
2. Run the app:
   ```bash
   streamlit run app.py
   ```
3. Open the app in your browser at the URL provided by Streamlit.

### 2. PyQt Desktop GUI
1. Ensure the trained model file `house_price_predic.pkl` is in the same directory as `ui_house_price.py`.
2. Run the PyQt app:
   ```bash
   python ui_house_price.py
   ```

---

## Dataset
The model is trained on a dataset with the following features:
- **Number of Bedrooms**
- **Number of Bathrooms**
- **Square Footage**
- **Age of the House**
- **House Price** (target)

---

## Results
- **Model Performance**:
  - Mean Squared Error: [Add MSE Value]
  - R² Score: [Add R² Value]

---

## Screenshots
**Web App**

![Screenshot (275)](https://github.com/user-attachments/assets/b93f5b53-0572-4764-9864-2aa334ea2b84)

**Desktop App**

![Screenshot (273)](https://github.com/user-attachments/assets/e39eb3d2-b081-4d85-b5a8-c035503a530f)

