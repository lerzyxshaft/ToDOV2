class Todo:

    def __init__(self):
        self.todos = []

    def add_todo(self):
        todos = [None]
        add_todo = input("Input todo name:")
        todos.append(add_todo)
        print(todos)

    def mas_todo(self):
        print(self.todos)
        mark_as_done = input('Choose which todo you want to delete:')
        self.todos.remove(mark_as_done)

    def menu(self):
        print("Hello and welcome to your todo project!")
        user_choice = input("Select what you want to do: \n1.Print your ToDo's \n2.Add todo\n3.Mark as done\n(input letter)")
        if user_choice == 1:
            if not self.todos:
                print("Your todos list is empty, firstly add todo")
                return
            else:
                print(self.todos)
                return

        elif user_choice == 2:
            self.add_todo()
            return
        elif user_choice == 3:
            self.mas_todo()
            return


        print(self.todos)


if __name__ == "__main__":
    todo_app = Todo()
    todo_app.menu()
