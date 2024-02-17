def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such user in contacts!"
        except IndexError:
            return "Index if out of range!"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):   
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):      
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact changed."
    else:
        return "No such contact in dictionary!"

@input_error
def show_phone(args, contacts):
    name = ''.join(args)
    return f"Phone: {contacts[name]}"

@input_error
def show_all(contacts):
    return contacts 

@input_error    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))                   
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
