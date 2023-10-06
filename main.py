import csv

user_name = input("""
================================================
こんにちは！私はRobokoです。あなたの名前は何ですか？
Hello, I am Roboko. What is your name?
================================================
⇒ """)

restaurant_name = input(f"""
================================================
{user_name}さん。どこのレストランが好きですか？
{user_name}, which restaurants do you like?
================================================
⇒ """)

print(f"""
================================================
Roboko: {user_name}さん。ありがとうございました。
Roboko: Thank you so much, {user_name}!

良い一日を！さようなら。
Have a good day!
================================================""")