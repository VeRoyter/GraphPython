def calculate_growth(listeners):
    growth = [0]
    for i in range(1, len(listeners)):
        growth.append(listeners[i] - listeners[i-1])
    return growth