import sys
def parse_log_line(line: str) -> dict:#для парсингу рядків логу.
    line = line.split()
    dict_of_lines = {}
    dict_of_lines['date'], dict_of_lines['time'], dict_of_lines['type'], dict_of_lines['information'] = line[0], line[1], line[2], ' '.join(line[3::])
    
    return dict_of_lines

def load_logs(file_path: str) -> list: #для завантаження логів з файлу.
    try:
        with open (file_path, 'r') as file:
            list_of_lines = []
            for line in file:
                list_of_lines.append(parse_log_line(line))
        return list_of_lines
    except Exception as e:
        print(f'There is an exception {e}')

def filter_logs_by_level(logs: list, level: str) -> list: #для фільтрації логів за рівнем.
    return list(filter(lambda log: log['type'].lower()==level.lower(),logs))


def count_logs_by_level(logs: list) -> dict: #для підрахунку записів за рівнем логування.
    count_dict = {}
    for log in logs:
        if log['type'] in count_dict.keys():
            count_dict[str(log['type'])] += 1
        else:
            count_dict[str(log['type'])] = 1
    return count_dict

def display_log_counts(counts: dict): #для виводу на екран записів
    result = f'''Рівень логування | Кількість
-----------------|----------
{list(counts.keys())[0]:17}| {counts[list(counts.keys())[0]]:<10} 
{list(counts.keys())[1]:17}| {counts[list(counts.keys())[1]]:<10}
{list(counts.keys())[2]:17}| {counts[list(counts.keys())[2]]:<10}
{list(counts.keys())[3]:17}| {counts[list(counts.keys())[3]]:<10}
'''
    return result

if __name__ == "__main__":
    try:
        print(display_log_counts(count_logs_by_level(load_logs(sys.argv[1]))))
        try:
            print(f'Деталі логів для типу {sys.argv[2]}:\n' + ''.join(map(lambda x: f'{x['date']} {x['time']} {x['information']}\n',filter_logs_by_level(load_logs('log.txt'),'error'))))
        except Exception as exc:
            print(f'There is an error: {exc}!')
    except Exception as exc:
            print(f'There is an error: {exc}!')