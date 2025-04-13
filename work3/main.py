import sys
import os

#Парсит строку лога и возвращает словарь
def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=4)
    if len(parts) < 5:
        return None
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[4].strip()
    }

#Загружает лог-файл и возвращает список разобранных строк
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)
    return logs

#Фильтрует логи по указанному уровню логирования
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].upper() == level.upper()]

#Подсчитывает количество записей для каждого уровня логирования
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

#Форматирует и выводит статистику по уровням логирования
def display_log_counts(counts: dict):
    print("Уровень логирования | Количество")
    print("--------------------|-----------")
    for level, count in counts.items():
        print(f"{level:<20}| {count}")

#Выводит подробные записи логов
def display_logs(logs: list):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python main.py <путь_к_лог_файлу> [уровень_логирования]")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.isfile(log_file):
        print(f"Ошибка: Файл {log_file} не найден.")
        sys.exit(1)

    logs = load_logs(log_file)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДетали логов для уровня '{log_level.upper()}':")
        display_logs(filtered_logs)