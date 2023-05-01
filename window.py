from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

TEXT_FIELD_WIDTH = 400
TEXT_FIELD_HEIGHT = 20

ENCRYPTION_BOX_Y_FACTOR = 0.05
DECRYPTION_BOX_Y_FACTOR = 0.35


RESULT_LABEL_HEIGHT = 70
RESULT_LABEL_Y_FACTOR = 0.18

DECRYPTION_LABEL_Y_FACTOR = 0.48

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 30

ENCRYPTION_BUTTON_Y_FACTOR = 0.10
DECRYPTION_BUTTON_Y_FACTOR = 0.40



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.initUI()

    def initUI(self):
        # Create a widget to hold the input box and self.encryp_btn

        # Create a label for the input box
        center_pos_x = SCREEN_WIDTH // 2
        # center_pos_y = SCREEN_HEIGHT // 2

        text_field_starting_y = 40

        # Create the encryption box
        encryption_text = QLabel(self)
        encryption_text.setFixedSize(TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)
        encryption_text.setText("Type the plaintext here")
        encryption_text.move(center_pos_x - TEXT_FIELD_WIDTH //2 , int(SCREEN_HEIGHT * ENCRYPTION_BOX_Y_FACTOR) - 20)

        self.encryption_box = QLineEdit(self)
        self.encryption_box.setStyleSheet("background-color: #ffffff; color: black;")
        self.encryption_box.setFixedSize(TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)
        self.encryption_box.move(center_pos_x - TEXT_FIELD_WIDTH // 2, int(SCREEN_HEIGHT * ENCRYPTION_BOX_Y_FACTOR))


        # Create the decryption box
        decryption_text = QLabel(self)
        decryption_text.setFixedSize(TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)
        decryption_text.setText("Type the ciphertext here")
        decryption_text.move(center_pos_x - TEXT_FIELD_WIDTH // 2, int(SCREEN_HEIGHT * DECRYPTION_BOX_Y_FACTOR) - 20)

        self.decryption_box = QLineEdit(self)
        self.decryption_box.setStyleSheet("background-color: #ffffff; color: black;")
        self.decryption_box.setFixedSize(TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)
        self.decryption_box.move(center_pos_x - TEXT_FIELD_WIDTH // 2, int(SCREEN_HEIGHT * DECRYPTION_BOX_Y_FACTOR))

        # Create Button
        self.encryp_btn = QPushButton("Encrypt", self)
        self.encryp_btn.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        self.encryp_btn.move(center_pos_x - BUTTON_WIDTH // 2, int(SCREEN_HEIGHT * ENCRYPTION_BUTTON_Y_FACTOR))
        self.encryp_btn.clicked.connect(self.handle_button_click)

        # Create Result
        self.encrypted_label = QLabel(self)
        self.encrypted_label.setFixedSize(TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)
        self.encrypted_label.move(center_pos_x - TEXT_FIELD_WIDTH//2, int(SCREEN_HEIGHT *  RESULT_LABEL_Y_FACTOR))

        # Create Button
        self.decrypted_btn = QPushButton("Decrypt", self)
        self.decrypted_btn.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        self.decrypted_btn.move(center_pos_x - BUTTON_WIDTH // 2, int(SCREEN_HEIGHT * DECRYPTION_BUTTON_Y_FACTOR))
        self.decrypted_btn.clicked.connect(self.handle_decrypt_btn_click)

        # Create Result
        self.decrypted_label = QLabel(self)
        self.decrypted_label.setFixedSize(TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)
        self.decrypted_label.move(center_pos_x - TEXT_FIELD_WIDTH//2, int(SCREEN_HEIGHT *  DECRYPTION_LABEL_Y_FACTOR))

    def handle_button_click(self):
        _text = self.encryption_box.text()
        self.encryption_box.setText("")
    
    def handle_decrypt_btn_click(self):
        _text = self.decryption_box.text()
        self.decryption_box.setText("")

    def update_encrypted_label(self, s):
        self.encrypted_label.setText(s)

    def update_decrypted_label(self, s):
        self.decrypted_label.setText(s)

    def clear_encrypted_result(self):
        self.encrypted_label.setText("")

    def clear_decrypted_result(self):
        self.decrypted_label.setText("")

