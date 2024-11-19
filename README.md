# House Price Prediction with GUI

🏡 **House Price Prediction with GUI** is a Python-based desktop application that uses machine learning to predict house prices. The application features a sleek, user-friendly interface built with PyQt6, making it easy for users to input details and receive accurate predictions.

## Features
- **Custom GUI**: Developed with PyQt6 for a modern, responsive interface.
- **Predictive Model**: Trained ML model to estimate house prices based on:
  - Number of bedrooms
  - Number of bathrooms
  - Square footage
  - House age
- **Real-Time Predictions**: Instant price calculations displayed in a clean format.
- **Dynamic Inputs**: Spinbox inputs for easy user interaction.

## Technology Stack
- **Programming Language**: Python
- **Libraries Used**:
  - PyQt6: For GUI development
  - Scikit-learn: For the ML model
  - Pandas & NumPy: For data manipulation
  - Joblib: For model persistence
- **Trained Model**: Serialized and loaded using `joblib`.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/house-price-predictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd house-price-predictor
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python ui_house_price.py
   ```

## Screenshots
![Screenshot (273)](https://github.com/user-attachments/assets/e39eb3d2-b081-4d85-b5a8-c035503a530f)

## Project Workflow
1. **Data Collection**: Data was cleaned and prepared for training.
2. **Model Training**: Built using Scikit-learn.
3. **GUI Design**: Developed a PyQt6-based interface for user interaction.
4. **Integration**: Connected the ML model with the GUI for real-time predictions.
