from loadData import load_data
from dataVisual import create_listeners_plot
from growthAnalytics import calculate_growth

def main():

    print("Анализ популярности Red Hot Chili Peppers")
    print("=" * 50)
    print("Загрузка данных...")
    
    filename = "data.txt"
    years, listeners = load_data(filename)
    
    if years and listeners:

        growth = calculate_growth(listeners)
        
        print("\nЗагруженные данные:")
        print("-" * 40)
        print(f"{'Год':<8} {'Слушатели':<15} {'Прирост':<12}")
        print("-" * 40)
        
        for i in range(0, len(years)):
            print(f"{years[i]:<8} {listeners[i]:<15,} {growth[i]:<12,}")
    
        print(f"\nВсего загружено {len(years)} лет данных")
        create_listeners_plot(years, listeners, growth)
        

    else:
        print("Не удалось загрузить данные для анализа")

if __name__ == "__main__":
    main()