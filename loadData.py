def load_data(filename):

    years = []
    listeners = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            for line in lines[1:]:
                line = line.strip()
                if line:
                    year, listener_count = line.split(',')
                    years.append(int(year))
                    listeners.append(int(listener_count))
                    
        return years, listeners
        
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return None, None
