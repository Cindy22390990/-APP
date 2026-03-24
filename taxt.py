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
