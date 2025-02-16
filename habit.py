import re
import json
from datetime import date
import random
import sys
import os
import streamlit as st

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

    def check_if_habit_exists(self, name = None) -> bool:
        
        data = None
        with open('habit.json', 'r') as f:
            content = f.read()
            if re.search(r'^\s*$', content):
                return True
            f.seek(0)
            data = json.load(f)
        
        for keys in data.keys():
            if(keys == self.get_habit_name()):
                return False
        if(name != None):
            for keys in data.keys():
                if(keys == name):
                    return False
        return True
    


            

    def set_habit_name(self,name: str = None) -> bool:
        
        if(name == ""):
            print("Habit name cannot be empty")
            st.error("Habit name cannot be empty")
            return False
        

        elif(not self.check_if_habit_exists(name)):
            print("Habit already exists, please enter a new habit")
            st.error("Habit already exists, please enter a new habit")
            return False
        else:
            self.habit["habit_name"] = name


    
    def set_date(self, date) -> bool:       
            
            self.habit["date"] = date.strftime("%Y-%m-%d")
            print(f'Date set: {self.get_date()}')


    def get_date(self) -> str:
        return self.habit.get("date")
    
    def get_habit_name(self) -> str:
        return self.habit.get("habit_name")

    def set_habit_days(self,days_arr: list[str]) -> bool:

        if(days_arr == []):
            print("Must Select at least one day")
            return False
        else:
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
                        self.errors.append(f"Error: ${days_str} is not a valid day")
                        return False
            return True
    
    def json_dump(self):

        with open('habit.json', 'r+') as f:

            content = f.read()
            name = self.get_habit_name()

            if re.search(r'^\s*$', content): # Checks to see if the file is empty if so, write the first line
                f.write("{\n")
                f.write("\t\"" + name + "\"" + ' :')
                f.write(json.dumps(self.habit))
            else: # If the file is not empty, write the habit object to the file with the correct syntax
                f.seek(0,2)
                f.seek(f.tell() - 1, os.SEEK_SET)
                f.write(", \n")
                f.write("\t\"" + name + "\"" + ' :')
                f.write(json.dumps(self.habit))

            last_line = f.readline(f.seek(0,2))
            
            if(last_line != "}"):
                f.writelines("\n}")
    
    def del_habit(self):

        with open('habit.json', 'r+') as f:

            data = json.load(f)
            print("Enter the habit you want to delete: ")
            habit_name = input()
            while(True):
                if habit_name in data.keys():
                    print(f"Deleting habit \"{habit_name}\"")
                    del data[habit_name]
                    with open('habit.json', 'w') as f:
                        if(len(data) == 0):
                            f.write("")
                        else:
                            f.write(json.dumps(data, indent=0))
                        break

                else:
                    print("Habit not found")
                    print("Enter the habit you want to delete: ")
                    habit_name = input()
    
    def display(self):
        st.title("Habit Tracker")
        add_button = st.button("Add habit")
        add_success = None
        if add_button:
            add_success = self.add_habit_display()
        if(add_success == True):
            st.write("Habit added successfully")
    
    
    @st.dialog("Add habit")
    def add_habit_display(self) -> bool:

        with st.form("Add habit", border = False):
            name = st.text_input("Enter the start date of your habit")
            
            # date = st.date_input("Enter the end date:", format = "YYYY-MM-DD")
            days: list[str] = st.pills("Days", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], selection_mode = "multi")
            submit_button = st.form_submit_button("Submit")
        
        days = [day.lower() for day in days]

        if submit_button:
            if(self.set_habit_name(name) == False):
                #st.error("Habit name cannot be empty")
                return False
            
            elif(self.set_habit_days(days) == False):
                st.error("Must select at least one day")
                return False
                
            print(days)
            self.json_dump()
            st.rerun()
            return True
        return True
            

        



                    
        
