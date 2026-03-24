# Требуется найти в тексте все вхождения даты и времени в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС.
# Учитываются только года из 21 века. Корректно должны распознаваться месяца, дни, часы, минуты и секунды.
import re
from datetime import datetime

def find_datetime(text):
    pattern = r'\b(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\s+([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\b'
    matches = []

    for match in re.finditer(pattern, text):
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        hour = int(match.group(4))
        minute = int(match.group(5))
        second = int(match.group(6))

        try:
            datetime(year, month, day, hour, minute, second)
            matches.append(match.group())
        except ValueError:
            continue

    return matches

if __name__ == "__main__":
    test_text = """
    Сегодня 2023-12-25 14:30:45 - это корректная дата.
    Вчера было 2023-02-28 23:59:59 - тоже корректно.
    А вот 2024-02-29 12:00:00 - корректная дата (високосный год).
    Неправильные даты:
    2023-02-30 10:15:30 - не существует,
    2023-13-01 08:00:00 - неверный месяц,    
    2023-12-41 08:00:00 - неверный день,
    2023-12-01 28:00:00 - неверное время,    
    2023-12-32 24:00:00 - неверный день и час,
    1995-12-31 23:59:59 - год не из 21 века,
    2099-12-31 23:59:59 - корректная дата.
    Еще одна корректная: 2025-07-15 09:45:30
    """

    print("Найденные даты и время:")
    for dt in find_datetime(test_text):
        print(f"  {dt}")
