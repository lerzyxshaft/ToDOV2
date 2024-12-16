class Todo():

    def __init__(self):
        self.job_todos = []
        self.work_todos = []
        self.home_todos = []

    def add_todo(self):
        add_todo = input("Input todo name:")
        category = input('Choose category(1-3): \n1)Job todos. \n2)Work todos. \n3)Home todos.\n')
        if category == "1":
            self.job_todos.append(add_todo)
            print(self.job_todos)
        elif category == "2":
            self.work_todos.append(add_todo)
            print(self.work_todos)
        elif category == "3":
            self.home_todos.append(add_todo)
            print(self.home_todos)

    def mark_as_done(self):
        if not self.job_todos and not self.work_todos and not self.home_todos:
            print("Your todos list is empty, nothing to mark as done.")
            return
        self.view_todos()
        try:
            t_category = input('Choose category(1-3): \n1)Job todos. \n2)Work todos. \n3)Home todos.\n')
            if t_category == "1":
                self.view_todos()
                job_index = int(input("Enter the number of the task to mark as done: ")) - 1
                if 0 <= job_index < len(self.job_todos ):
                    completed_task = self.job_todos.pop(job_index)
                    print(f"'{completed_task}' has been marked as done.")
            elif t_category == "2":
                self.view_todos()
                work_index = int(input("Enter the number of the task to mark as done:"))
                if 0 <= work_index < len(self.work_todos ):
                    completed_task = self.work_todos.pop(work_index)
                    print(f"'{completed_task}' has been marked as done.")
            elif t_category == "3":
                self.view_todos()
                home_index = int(input("Enter the number of the task to mark as done:"))
                if 0 <= home_index < len(self.work_todos ):
                    completed_task = self.work_todos.pop(home_index)
                    print(f"'{completed_task}' has been marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def view_todos(self):
        if not self.job_todos and not self.work_todos and not self.home_todos:
            print("Your todos list is empty, firstly add a todo.")
        else:
            print("Your Current Todos:")
            for job_idx, job_todo  in enumerate( self.job_todos, 1):
                print(f"Your job todos:\n{job_idx}. {job_todo}")
            for work_idx, work_todo in enumerate(self.work_todos, 1):
                print(f"Your work todos:\n{work_idx}. {work_todo}")
            for home_idx, home_todo in enumerate(self.home_todos, 1):
                print(f"Your home todos:\n{home_idx}. {home_todo}")

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
