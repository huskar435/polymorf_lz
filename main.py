from data_processor import DataProcessor

def main():
    processor = DataProcessor('var4.csv')
    
    cash, cashless = processor.split_by_payment_type()
    
    stats_before = processor.get_stats()
    print("Статистика до удаления дубликатов:")
    print(f"Всего строк: {stats_before['total_rows']}")
    print(f"Наличные операции: {stats_before['cash_rows']}")
    print(f"Безналичные операции: {stats_before['cashless_rows']}")
    
    stats_after = processor.get_stats()
    print("\nСтатистика после удаления дубликатов:")
    print(f"Удалено дубликатов: {stats_after['removed_duplicates']}")
    print(f"Всего строк: {stats_after['total_rows']}")
    print(f"Наличные операции: {stats_after['cash_rows']}")
    print(f"Безналичные операции: {stats_after['cashless_rows']}")
    
    processor.split_by_payment_type()

if __name__ == "__main__":
    main()