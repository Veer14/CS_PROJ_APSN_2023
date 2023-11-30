import mysql.connector
from sentiment import sentiment_analysis
from UI import SentimentDisplayApp, Review
from PyQt5.QtWidgets import QApplication
import sys
db_config = {
    "host": "localhost", 
    "user": "root",
    "password": "admin",
    "database": "text_analysis"
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

def get_next_input_id():
    cursor.execute("SELECT MAX(inputID) FROM user_entries")
    max_id = cursor.fetchone()[0]
    return max_id + 1 if max_id is not None else 1

def insert_user_input(text, sentiment):
    input_id = get_next_input_id()
    insert_query = "INSERT INTO user_entries (inputID, input, sentiment) VALUES (%s, %s, %s)"
    values = (input_id, text, sentiment)
    cursor.execute(insert_query, values)
    conn.commit()

def usermenu():
    print("Menu:")
    print("1. Enter comment")
    print("2. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        user_input = input("Enter the text you'd like to post: ")
        senti = sentiment_analysis(user_input)
        insert_user_input(user_input, senti)
        print("Text posted successfully!")
    elif choice == "2":
        print("Thank you for posting!")
    else:
        print("Invalid choice. Please choose again.")

usermenu()

app = QApplication(sys.argv)
window1 = SentimentDisplayApp()
window1.show()

window2 = Review()
window2.show()

sys.exit(app.exec_())