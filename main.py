import csv
import os

fieldnames = ["NAME", "COUNT"]
if os.path.exists("ranking.csv"):
    pass
else:
    with open("ranking.csv", "w", newline="") as rank_csv:
        writer = csv.DictWriter(rank_csv, fieldnames)
        writer.writeheader()


# ユーザーに名前を聞く
user_name = input("""
================================================
こんにちは！私はRobokoです。あなたの名前は何ですか？
Hello, I am Roboko. What is your name?
================================================
⇒ """)

# csvファイルにデータがあるか確認
with open("ranking.csv", "r", newline="") as rank_csv:
    reader = csv.DictReader(rank_csv)
    row_count = sum(1 for row in reader)
    if row_count >= 1:
        # レストランをおすすめする
        max_count = None
        for row in reader:
            count = int(row["COUNT"])
            if max_count is None or count > max_count:
                max_count = count
                osusume_name = row["NAME"]
            while True:
                osusume = input(f"""
                ================================================
                私のオススメのレストランは、{osusume_name}です。
                I recommend {osusume_name} restaurant.
    
                このレストランは好きですか？[Yes/No]
                Do you like it? [y/n]
                ================================================
                ⇒ """)
                answer = ["YES", "Yes", "yes", "Y", "y", "NO", "No", "no", "N", "n"]
                if osusume in answer:
                    break
                else:
                    print("正しい回答を入力してください")
    else:
        pass

# 好きなレストランを質問する
restaurant_name = input(f"""
================================================
{user_name}さん。どこのレストランが好きですか？
{user_name}, which restaurants do you like?
================================================
⇒ """)

restaurant_name = restaurant_name.title()
new_data = {"NAME": restaurant_name, "COUNT": 1}
# csvファイルに書き込む
with open("ranking.csv", mode='r', newline='') as rank_csv:
    reader = csv.DictReader(rank_csv)
    data = list(reader)

    for row in data:
        if row['NAME'] == new_data['NAME']:
            row['COUNT'] = str(int(row['COUNT']) + new_data['COUNT'])
            break
    else:
        data.append(new_data)

# 更新したデータを新しいCSVファイルに書き込む
with open("ranking.csv", mode='w', newline='') as rank_csv:
    writer = csv.DictWriter(rank_csv, fieldnames)
    # ヘッダーを書き込む
    writer.writeheader()
    # データを書き込む
    for row in data:
        writer.writerow(row)

# 処理を終了
print(f"""
================================================
Roboko: {user_name}さん。ありがとうございました。
Roboko: Thank you so much, {user_name}!

良い一日を！さようなら。
Have a good day!
================================================""")
