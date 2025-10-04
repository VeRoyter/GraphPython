import matplotlib.pyplot as plt

def create_listeners_plot(years, listeners, growth):

    listeners_millions = [count / 1000000 for count in listeners]

    # Создаем фигуру с увеличенной высотой для лучшего отображения
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
    
    # === ПЕРВЫЙ ГРАФИК: Динамика слушателей ===
    ax1.plot(years, listeners_millions, 
             marker='o', linewidth=3, markersize=8, 
             color='#E41A1C', label='Количество слушателей', 
             markerfacecolor='white', markeredgewidth=2)
    
    ax1.set_title('Динамика роста слушателей Red Hot Chili Peppers', 
                  fontsize=16, fontweight='bold', pad=20)
    ax1.set_xlabel('Год', fontsize=12)
    ax1.set_ylabel('Количество слушателей', fontsize=12)
    
    # Настройка оси X чтобы показывала все годы
    ax1.set_xticks(years)  # Принудительная установка всех годов на оси X
    ax1.tick_params(axis='x', rotation=45)  # Наклон подписей
    
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.legend(loc='upper left', framealpha=0.9, shadow=True)
    
    # === ВТОРОЙ ГРАФИК: Годовой прирост ===
    bars = ax2.bar(years, growth, 
                  color='#377EB8', alpha=0.7, 
                  label='Годовой прирост слушателей',
                  edgecolor='darkblue', linewidth=1)
    
    ax2.set_xlabel('Год', fontsize=12)
    ax2.set_ylabel('Прирост слушателей', fontsize=12)
    
    # Настройка оси X для второго графика
    ax2.set_xticks(years)
    ax2.tick_params(axis='x', rotation=45)
    
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.legend(loc='upper left', framealpha=0.9, shadow=True, fontsize=11)
    
    print("Отображаем график...")
    plt.show()
