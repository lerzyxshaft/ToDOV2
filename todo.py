class Todo:

    def __init__(self):
        self.todos = []

    def add_todo(self):
        add_todo = input("Input todo name:")
        self.todos.append(add_todo)
        print(self.todos)

    def mark_as_done(self):
        if not self.todos:
            print("Your todos list is empty, nothing to mark as done.")
            return
        self.view_todos()
        try:
            index = int(input("Enter the number of the task to mark as done: ")) - 1
            if 0 <= index < len(self.todos):
                completed_task = self.todos.pop(index)
                print(f"'{completed_task}' has been marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def view_todos(self):
        if not self.todos:
            print("Your todos list is empty, firstly add a todo.")
        else:
            print("Your Current Todos:")
            for idx, todo in enumerate(self.todos, 1):
                print(f"{idx}. {todo}")

    def menu(self):
        while True:
            print("\nSelect what you want to do:")
            print("1. Print your ToDo's")
            print("2. Add todo")
            print("3. Mark as done")
            print("4. Exit")
            user_choice = input("Input number: ")
            if user_choice == "1":
                self.view_todos()
            elif user_choice == "2":
                self.add_todo()
            elif user_choice == "3":
                self.mark_as_done()
            elif user_choice == "4":
                print("Bye!")
                break
            else:
                print("Invalid choise please try again!")

if __name__ == "__main__":
    todo_app = Todo()
    todo_app.menu()
