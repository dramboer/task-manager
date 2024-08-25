import datetime
from taskManager import TaskManager
from colored import Fore, Back, Style, stylize_interactive


def colored_input(prompt=""):
    print(Fore.GREEN)
    user_input = input(prompt)
    print(Style.RESET)
    return user_input


def print_options():
    print("- - - - - - - - - - - - - - - -")
    print(f"{Fore.rgb(100, 150, 255)}" + "Task Manager" + f"{Style.RESET}")
    print("1. View Pending Tasks")
    print("2. View Completed Tasks")
    print("3. Add Task")
    print("4. Mark Task as Completed")
    print("5. " + f"{Fore.RED}" + "Exit" + f"{Style.RESET}")
    print("- - - - - - - - - - - - - - - -")


def check_if_valid_option(user_input):
    try:
        if int(user_input) <= 5 and int(user_input) >= 0:
            return True
    except:
        return False


def check_if_valid_date(input_date):
    try:
        datetime.date = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
        return True
    except:
        return False


def main():
    """
    Main function that runs the Task Manager application.

    TODO:
    - Instantiate a TaskManager object.
    - Create a simple text-based menu to interact with the user.
    - Allow the user to add tasks, view pending tasks, view completed tasks, and mark tasks as completed.
    - Make sure the application runs in a loop until the user decides to exit.
    """
    manager = TaskManager()
    while True:
        print_options()
        user_input = colored_input()
        while not check_if_valid_option(user_input):
            print(f"{Fore.RED}" + "Invalid Entry. Please Try Again." + f"{Style.RESET}")
            print_options()
            user_input = colored_input()
        user_input = int(user_input)
        if user_input == 1:
            pending_tasks = manager.get_pending_tasks()
            if len(pending_tasks) == 0:
                print("There are no pending tasks")
            for task in pending_tasks:
                print(task)
        if user_input == 2:
            completed_tasks = manager.get_completed_tasks()
            if len(completed_tasks) == 0:
                print("There are no completed tasks")
            for task in completed_tasks:
                print(task)
        if user_input == 3:
            print("Enter the name of the new task:")
            task_name = colored_input()
            print("Enter a description:")
            task_description = colored_input()
            print("Enter due date for task (YYYY-MM-DD):")
            task_due_date = colored_input()
            while not check_if_valid_date(task_due_date):
                print(
                    f"{Fore.RED}" + "Invalid Date. Please Try Again." + f"{Style.RESET}"
                )
                print("Enter due date for task (YYYY-MM-DD):")
                task_due_date = colored_input()
            task_due_date: datetime.date = datetime.datetime.strptime(
                task_due_date, "%Y-%m-%d"
            ).date()
            manager.add_task(task_name, task_description, task_due_date)
        if user_input == 4:
            pending_tasks = manager.get_pending_tasks()
            if len(pending_tasks) == 0:
                print("All tasks are completed")
                continue
            for index, task in enumerate(pending_tasks):
                print(f"{index + 1} - {task.title}")
            task_index = colored_input(
                "Enter the number that corresponds to the task you would like to mark as completed: "
            )
            manager.mark_task_completed(int(task_index) - 1)

        if user_input == 5:
            break


if __name__ == "__main__":
    main()
