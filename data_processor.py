import pandas as pd

class Data_Processor:
    def __init__(self, input_data):
        self.raw_data = input_data.copy()
      

    def type_of_payment(self):
        cash_payments = self.raw_data[self.raw_data['Вид расчета'] == 'наличный']
        cashless_payments = self.raw_data[self.raw_data['Вид расчета'] == 'безналичный']
        cash_payments.to_csv('cash_transactions.csv', index=False)
        cashless_payments.to_csv('cashless_transactions.csv', index=False)
        return cash_payments, cashless_payments

    def __invert__(self):
        initial_count = len(self.raw_data)
        duplicate_count = self.raw_data.duplicated().sum()
        cleaned_data = self.raw_data.drop_duplicates()
        self.duplicate_info = {'total_duplicates': duplicate_count, 'removed_count': initial_count - len(cleaned_data)}
        
        print(f"Количество повторяющихся строк в наборе данных: {duplicate_count}")
        print(f"Количество удаленных дубликатов: {self.duplicate_info['removed_count']}")
        return Data_Processor(cleaned_data)

def main():
    transaction_data = pd.read_csv('var4.csv')
    data_processing = Data_Processor(transaction_data)
    data_processing.type_of_payment()
    ~data_processing

if __name__ == "__main__":
    main()

  




