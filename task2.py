def sum_profit(text, func):
    all_numbers = func(text)
    return sum(all_numbers)

def generator_numbers(text):
    text = text.split()
    for i in text:
        try:
            float(i)
            yield float(i)
        except:
            pass

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 , 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
