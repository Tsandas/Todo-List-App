import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

sg.theme("DarkAmber")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do",key="todo")
add_button = sg.Button(size=2,image_source="images/add.png",tooltip="Add to-do",key="Add")
list_box = sg.Listbox(values=functions.get_todos(),key="todos",
                      enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=10,image_source="images/complete.png",key="Complete",tooltip="Complete to-do")
exit_button = sg.Button("Exit")

window =  sg.Window("My To-Do App",
                    layout=[[clock],
                            [label],
                            [input_box,add_button],
                            [list_box,edit_button,complete_button],
                            [exit_button]
                            ],
                    font=("Helvetica",20))

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window["todos"].update(values=todos)

            except IndexError:
                print("No item selected")
                sg.popup("No item selected",font=("Helvetica",20))

        case "Complete":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)

                window["todos"].update(values=todos)
                window["todo"].update(value="")

            except IndexError:
                print("No item selected")
                sg.popup("No item selected",font=("Helvetica",20))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])



window.close()