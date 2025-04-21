import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path, encoding='utf-8')
        self.removed_duplicates = 0
    
    def type_of_calculation(self):
        cash_data = self.data[self.data['Вид расчета'] == 'наличный']
        cashless_data = self.data[self.data['Вид расчета'] == 'безналичный']
        cash_data.to_csv('cash_payments.csv', index=False, encoding='utf-8')
        cashless_data.to_csv('cashless_payments.csv', index=False, encoding='utf-8')
        
        return cash_data, cashless_data
    
    def __invert__(self):
        initial_count = len(self.data)
        self.data = self.data.drop_duplicates()
        self.removed_duplicates = initial_count - len(self.data)
        return self
    
    def get_stats(self):
        return {'total_rows': len(self.data), 'removed_duplicates': self.removed_duplicates, 'cash_rows': len(self.data[self.data['Вид расчета'] == 'наличный']), 'cashless_rows': len(self.data[self.data['Вид расчета'] == 'безналичный'])}