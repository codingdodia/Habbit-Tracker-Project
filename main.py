from habit import Habit

habit = Habit()

def main():
    
    print("Starting...")

    print("Main Menu:")
    print("1. Add habit")
    print("2. Edit habit")
    print("3. Delete habit")

    choice = input()
    match choice:
        case '1':
            add_habit()
        case '2':
            print("Editing habit")
        case '3':
            habit.del_habit()
        case _:
            print("Invalid input")

    



def add_habit():
    habit.set_habit_name()
    habit.set_date()
    habit.set_habit_days()
    habit.json_dump()

main()






