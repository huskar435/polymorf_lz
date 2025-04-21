import pandas as pd

class Data_Processor:
    def __init__(self, data):
        self.data = data

    def type_of_calculation(self):
        cash_data = self.data[self.data['Вид расчета'] == 'наличный']
        cashless_data = self.data[self.data['Вид расчета'] == 'безналичный']
        cash_data.to_csv('cash_payments.csv', index=False)
        cashless_data.to_csv('cashless_payments.csv', index=False)
        return cash_data, cashless_data

    def __invert__(self):
        initial_rows = len(self.data)
        duplicate_counts = self.data.duplicated().sum()
        cleaned_data = self.data.drop_duplicates()
        removed = initial_rows - len(cleaned_data)
        
        print(f"Количество повторяющихся строк в наборе данных: {duplicate_counts}")
        print(f"Количество удаленных дубликатов: {removed}")
        return Data_Processor(cleaned_data)

def main():
    data = pd.read_csv('var4.csv')
    processor = Data_Processor(data)
    processor.type_of_calculation()
    ~processor

if __name__ == "__main__":
    main()




