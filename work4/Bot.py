import re

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

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, book):
    name, phone = args
    if name not in book:
        book[name] = []
    book[name].append(phone)
    return "Contact added/updated."

@input_error
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
def phone_contact(args, book):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in book:
        return ", ".join(book[name])
    else:
        raise KeyError

@input_error   
def show_all(book):
    if not book:
        return "No contacts found"
    return "\n".join([f"{name}: {', '.join(phones)}" for name, phones in book.items()])

def main():
    book = {}  # Используем обычный словарь вместо AddressBook
    print("Welcome to the assistant bot")
    while True:
        user_input = input("Please enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye")
            break
        elif command == "hello":
            print("Hello! How can I help you today?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(phone_contact(args, book))
        elif command == "all":
            print(show_all(book))
        else:
            print("Invalid command")
            
contacts_bot = main()



