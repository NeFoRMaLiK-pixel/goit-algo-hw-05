import re

# Декоратор для обработки ошибок в функциях
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and number"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Not found"
    return inner

# Разбор пользовательского ввода на команду и аргументы
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
# Добавление нового контакта или обновление существующего
def add_contact(args, book):
    name, phone = args
    if name not in book:
        book[name] = []
    book[name].append(phone)
    return "Contact added/updated."

@input_error
# Изменение номера телефона для существующего контакта
def change_contact(args, book):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in book:
        book[name] = [phone]
        return "Contact updated successfully"
    else:
        raise KeyError

@input_error
# Получение номера телефона по имени
def phone_contact(args, book):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in book:
        return ", ".join(book[name])
    else:
        raise KeyError

@input_error
# Показать все контакты
def show_all(book):
    if not book:
        return "No contacts found"
    return "\n".join([f"{name}: {', '.join(phones)}" for name, phones in book.items()])

# Основная функция для запуска бота
def main():
    book = {}  # Словарь для хранения контактов
    print("Welcome to the assistant bot")
    while True:
        user_input = input("Please enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:  # Завершение работы
            print("Good bye")
            break
        elif command == "hello":  # Приветствие
            print("Hello! How can I help you today?")
        elif command == "add":  # Добавление контакта
            print(add_contact(args, book))
        elif command == "change":  # Изменение контакта
            print(change_contact(args, book))
        elif command == "phone":  # Поиск номера телефона
            print(phone_contact(args, book))
        elif command == "all":  # Показ всех контактов
            print(show_all(book))
        else:  # Неизвестная команда
            print("Invalid command")
            
contacts_bot = main()  # Запуск бота



