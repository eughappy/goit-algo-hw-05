def sum_profit(text, func):
    all_numbers = func(text)
    return sum(all_numbers)

def generator_numbers(text):
    text = text.split() # Розбиваємо текст за пробілами
    for i in text: # Перебираємо кожний еелмент тексту
        try: 
            float(i) # Намагаємось елемент перетворити у влофт- дійсне число
            yield float(i)
        except:
            pass # Якщо не можливо - пропускаємо елемент

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
