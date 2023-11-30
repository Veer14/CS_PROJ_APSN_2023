import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "admin",
    "database": "text_analysis"
}

class SentimentDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.load_positive_comments()
        
    def load_positive_comments(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        select_query = "SELECT input FROM user_entries WHERE sentiment = 'p'"
        cursor.execute(select_query)
        positive_comments = cursor.fetchall()
        
        for comment in positive_comments:
            comment_label = QLabel(comment[0])
            self.layout.addWidget(comment_label)

        cursor.close()
        conn.close()


class Review(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Review board")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.load_review_board()


    def load_review_board(this):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        select_query = "SELECT input FROM user_entries WHERE sentiment = 'r'"
        cursor.execute(select_query)
        positive_comments = cursor.fetchall()
        
        for comment in positive_comments:
            comment_label = QLabel(comment[0])
            this.layout.addWidget(comment_label)

        cursor.close()
        conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = SentimentDisplayApp()
    window1.show()

    window2 = Review()
    window2.show()

    sys.exit(app.exec_())