import datetime

# 1. 取得現在的時間，格式化成漂亮的樣子
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. 問你想紀錄什麼
idea = input("現在腦袋裡有什麼宏大的想法？請輸入：")

# 3. 把時間加內容寫進一個叫做 "my_ideas.txt" 的檔案裡
with open("my_ideas.txt", "a", encoding="utf-8") as f:
    f.write(f"[{now}] {idea}\n")

print("\n✅ 記錄成功！你可以去看看 my_ideas.txt 了。")
