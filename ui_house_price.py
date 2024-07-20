import sys,os,joblib
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QSpacerItem, QSizePolicy, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator,QPixmap

class HousePricePredictor(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("House Price Predictor")
        self.setGeometry(300, 150, 1500, 900)
        self.setStyleSheet("background-color: white; color: black; font-size: 16px;")

        # image_path = "D:/Python/project 1/Pdfconverter/images/2.jpg"
        image_path = os.path.join(sys._MEIPASS,"2.jpg")
        background_label = QLabel(self)
        background_label.setPixmap(QPixmap(image_path))
        background_label.setGeometry(0, 0, 1500, 1000)

        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create central frame with a fixed size
        center_frame = QFrame()
        center_frame.setFixedSize(800, 600)
        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_frame.setLayout(center_layout)
        center_frame.setStyleSheet("background-color: white;")

        # Title
        self.title = QLabel('House Price Prediction', self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 22px; font-weight: bold;")

        # Number of bedrooms
        self.bedrooms_label = QLabel('Enter the number of bedrooms:')
        self.bedrooms_input = QSpinBox()
        self.bedrooms_input.setRange(1,10)
        self.bedrooms_layout = QVBoxLayout()
        self.bedrooms_layout.addWidget(self.bedrooms_label)
        self.bedrooms_layout.addWidget(self.bedrooms_input)

        # Number of bathrooms
        self.bathrooms_label = QLabel('Enter the number of bathrooms:')
        self.bathrooms_input = QSpinBox()
        self.bathrooms_input.setRange(1, 10)
        self.bathrooms_layout = QVBoxLayout()
        self.bathrooms_layout.addWidget(self.bathrooms_label)
        self.bathrooms_layout.addWidget(self.bathrooms_input)
        self.bathrooms_layout.setContentsMargins(0, 10, 0, 10)

        # Square footage
        self.square_footage_label = QLabel('Enter the square footage(min=800):')
        # self.square_footage_input = QLineEdit()
        # self.square_footage_input.setValidator(QIntValidator())
        self.square_footage_input = QSpinBox()
        self.square_footage_input.setRange(1, 5000)
        self.square_footage_layout = QVBoxLayout()
        self.square_footage_layout.addWidget(self.square_footage_label)
        self.square_footage_layout.addWidget(self.square_footage_input)
        self.square_footage_layout.setContentsMargins(0, 10, 0, 10)

        # Age of the house
        self.house_age_label = QLabel('Enter the age of the house:')
        # self.house_age_input = QLineEdit()
        # self.house_age_input.setValidator(QIntValidator())
        self.house_age_input = QSpinBox()
        self.house_age_input.setRange(1, 100)
        self.square_footage_input.setFixedWidth(750)
        self.house_age_layout = QVBoxLayout()
        self.house_age_layout.addWidget(self.house_age_label)
        self.house_age_layout.addWidget(self.house_age_input)
        self.house_age_layout.setContentsMargins(0, 10, 0, 10)

        # Prediction button
        self.predict_button = QPushButton('Predict House Price')
        self.predict_button.setStyleSheet("background-color: #007BFF; color: white; padding: 10px;")
        self.predict_button.clicked.connect(self.predict_price)

        # Prediction result
        self.result_label = QLabel('Predicted House Price: $0.00', self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("font-size: 18px;")

        # Add widgets to center layout
        center_layout.addWidget(self.title)
        center_layout.addLayout(self.bedrooms_layout)
        center_layout.addLayout(self.bathrooms_layout)
        center_layout.addLayout(self.square_footage_layout)
        center_layout.addLayout(self.house_age_layout)
        center_layout.addWidget(self.predict_button, alignment=Qt.AlignmentFlag.AlignCenter)
        center_layout.addWidget(self.result_label)

        # Add central frame to the main layout
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        main_layout.addWidget(center_frame, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Set main layout
        self.setLayout(main_layout)

    def predict_price(self):
        # Dummy prediction logic for demonstration purposes
        
        model_path = os.path.join(sys._MEIPASS, 'house_price_predic.pkl')
        model = joblib.load(model_path)
        bedrooms = self.bedrooms_input.value()
        bathrooms = self.bathrooms_input.value()
        square_footage = int(self.square_footage_input.text())
        house_age = int(self.house_age_input.text())

        # Example formula for prediction (replace with your model)
        price = model.predict([[bedrooms,bathrooms,square_footage,house_age]])
        print(price[0])
        self.result_label.setText(f'Predicted House Price: ${price[0]:,.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = HousePricePredictor()
    window.show()

    sys.exit(app.exec())
