from habit import Habit


def main():
    habit = Habit()
    print("Starting...")

    habit.set_habit_name()
    habit.set_date()
    habit.set_habit_days()


    print(habit.get_habit_name())
    print(habit.get_date())

    habit.json_dump()

main()





