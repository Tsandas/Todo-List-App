import functions
import time

now = time.strftime("%B %D, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(f"{todo}\n")
        functions.write_todos(todos)

    elif  user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = f"{new_todo}\n"
            functions.write_todos(todos)
        except ValueError:
            print("Invalid number")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            todos = functions.get_todos()
            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)
            functions.write_todos(todos)
            print(f"Todo {todo_to_remove} was removed from the list")
        except IndexError:
            print("No such number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command")

print("Bye!")