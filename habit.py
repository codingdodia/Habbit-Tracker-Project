import re
import json
from datetime import date

class Habit:
    def __init__(self):
        
        self.days: dict[str,int] = {
            "Mon": 0,
            "Tue": 0,
            "Wed": 0,
            "Thu": 0,
            "Fri": 0,
            "Sat": 0,
            "Sun": 0
        }

        self.habit = {
            "habit_name": "",
            "date": "",
            "days": self.days
        }

    def set_habit_name(self):
        print("Enter your habit: ")
        self.habit["habit_name"] = input()
        print("Your habit is: ", self.get_habit_name())
    
    def set_date(self) -> bool:

        print("What date should this habit end? If none, type 'none'")
        print("Enter the date in the format: yyyy-mm-dd")
        pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        input_date = input()

        if(input_date == "none"):
            print("No date selected")
            return False
        
        while(pattern.match(input_date) == None):
            print("Invalid date format")
            print("Enter the date in the format: yyyy-mm-dd")
            input_date = input()
            
        try:
            self.habit["date"] = date.fromisoformat(input_date)
            print(f'Date set: {self.get_date()}')
        except:
            print
        
        print("The date you want to end your habit is: ", self.get_date())
    
    def get_date(self) -> str:
        return self.habit.get("date")
    
    def get_habit_name(self) -> str:
        return self.habit.get("habit_name")

    def set_habit_days(self):
        print("What days of the week would you like to be reminded of your habit?")
        print("Enter the days in following format: \n Mon, Tue, Wed, Thu, Fri, Sat, Sun")
        days_arr = []
        print("How many days do you want? If none write \"none\"")
        days_count = input()

        def check_for_none_days(input_str: str) -> bool:
            print("No days selected")
            return False
        
        check_for_none_days(days_count)
        
        while(not days_count.isdigit() and days_count not in range(0,7)):
            print("Invalid input")
            print("How many days do you want? If none write \"none\"")
            days_count = input()
            if(check_for_none_days(days_count)):
                return False
            
        days_count = int(days_count)

        for i in range(days_count):
            print("Enter the day: ")
            days_arr.append(input())

        for days_str in days_arr:
            match days_str:
                case "Mon":
                    self.habit.update({'Mon': 1})
                case "Tue":
                    self.days.update({'Tue': 1})
                case "Wed":
                    self.days.update({'Wed': 1})
                case "Thu":
                    self.days.update({'Thu': 1})
                case "Fri":
                    self.days.update({'Fri': 1})
                case "Sat":
                    self.days.update({'Sat': 1})
                case "Sun":
                    self.days.update({'Sun': 1})
                case _:
                    print("Invalid day")
    
    def json_dump(self):
        with open('habit.json', 'w'):
            json.dump(self.habit)
