from datetime import datetime

class Transaction:
    def __init__(self, amount, category, note=""):
        self.amount = amount        # 金額
        self.category = category    # 分類 (食、衣、住、行)
        self.note = note            # 備註
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.date}] {self.category}: ${self.amount} ({self.note})"
    
class FinanceManager:
    def __init__(self):
        self.records = []  # 暫時存放在記憶體中，進階可改用 SQLite 資料庫

    def add_record(self, amount, category, note):
        # 邏輯判斷：確保金額是數字
        try:
            amount = float(amount)
            new_record = Transaction(amount, category, note)
            self.records.append(new_record)
            print("儲存成功！")
        except ValueError:
            print("錯誤：金額必須是數字。")

    def get_total_balance(self):
        # 計算總餘額邏輯
        return sum(r.amount for r in self.records)

    def show_all(self):
        for r in self.records:
            print(r)
import sqlite3

# 1. 連接資料庫（如果檔案不存在，會自動建立）
conn = sqlite3.connect('finance.db')

# 2. 建立「游標」，它是你在資料庫裡的「手」，負責執行指令
cursor = conn.cursor()

# 3. 建立資料表邏輯 (CREATE TABLE)
# 如果表還沒建立，就建立一個名為 records 的表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL
    )
''')

# 4. 寫入資料邏輯 (INSERT)
def save_to_db(amount, category, date):
    # 使用 ? 作為佔位符是為了防止「SQL 注入攻擊」（安全性考慮）
    cursor.execute("INSERT INTO records (amount, category, date) VALUES (?, ?, ?)", 
                   (amount, category, date))
    
    # 重要：一定要 commit（提交），否則資料只會在暫存區，不會真的寫入硬碟
    conn.commit()

# 5. 關閉連接
# 程式結束前要記得關閉，釋放電腦資源
# conn.close()
