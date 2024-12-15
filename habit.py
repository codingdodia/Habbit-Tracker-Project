import re
import json
from datetime import date
import random
import sys
import os

class Habit:
    def __init__(self):
        
        self.days: dict[str,int] = {
            "mon": 0,
            "tue": 0,
            "wed": 0,
            "thu": 0,
            "fri": 0,
            "sat": 0,
            "sun": 0
        }

        self.habit = {
            'habit_name': None,
            'date': None,
            "days": self.days
        }

        with(open('habit.json', 'a')) as f:
            f.seek(0)

    def check_if_habit_exits(self) -> bool:
        
        data = None
        with open('habit.json', 'r') as f:
            content = f.read()
            if re.search(r'^\s*$', content):
                return True
            f.seek(0)
            data = json.load(f)
        
        for keys in data.keys():
            if(keys == self.habit['habit_name']):
                return False
        return True

            

    def set_habit_name(self):
        print("Enter your habit: ")
        self.habit["habit_name"] = input()
        while(not self.check_if_habit_exits()):
            print("Habit already exists, please enter a new habit")
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
            
            self.habit["date"] = input_date
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
        print("How many days do you want? If none write \"none\"")
        
        days_arr = []
        days_count = input()

        def check_for_none_days(input_str: str) -> bool:
            if(input_str == "none"):
                print("No days selected")
                return True
            return False

        if(check_for_none_days(days_count)): return False
        
        while(not days_count.isdigit() or int(days_count) not in range(1,7)):
            print("Invalid input")
            print("How many days do you want? Must be within 1 and 7 \nIf none write \"none\"")
            days_count = input()
            print(days_count)
            if(check_for_none_days(days_count)):
                return False
            
        days_count = int(days_count)

        for i in range(days_count):
            
            print("Enter the day: ")
            day = input().lower()
            while(True):
                if(day not in self.days.keys()):
                    print("Invalid Input, TRY AGAIN!")
                    day = input().lower()
                else:
                    break
            days_arr.append(day)

        

        for days_str in days_arr:
            match days_str:
                case "mon":
                    self.days.update({'mon': 1})
                case "tue":
                    self.days.update({'tue': 1})
                case "wed":
                    self.days.update({'wed': 1})
                case "thu":
                    self.days.update({'thu': 1})
                case "fri":
                    self.days.update({'fri': 1})
                case "sat":
                    self.days.update({'sat': 1})
                case "sun":
                    self.days.update({'sun': 1})
                case _:
                    print("Invalid Input, TRY AGAIN!")
    
    def json_dump(self):
        random_id = random.randint(0, sys.maxsize)

        with open('habit.json', 'r+') as f:

            content = f.read()
            name = self.get_habit_name()

            if re.search(r'^\s*$', content):
                f.write("{\n")
                f.write("\t\"" + name + "\"" + ' :')
                f.write(json.dumps(self.habit))
            else:
                f.seek(0,2)
                f.seek(f.tell() - 1, os.SEEK_SET)
                f.write(", \n")
                f.write("\t\"" + name + "\"" + ' :')
                f.write(json.dumps(self.habit))

            last_line = f.readline(f.seek(0,2))
            
            if(last_line != "}"):
                f.writelines("\n}")
            
