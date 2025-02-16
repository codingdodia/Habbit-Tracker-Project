# from habit import Habit
# import streamlit as st


# class AddHabit:
#     def __init__(self, habit: Habit):
#         self.name = None
#         self.date = None
#         self.days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#         self.habit = habit


#     def name_input(self):
#         self.name = st.text_input("Enter your habit: ")
        
#     def date_input(self):
#         date_opt = st.checkbox("End at a date")
#         if date_opt:
#             self.date = st.date_input("Enter the start date: ")
    
#     def days_input(self):
        
#         every_day = st.checkbox("Everyday") 
#         if not every_day:
#             selection = st.pills("Days", self.days, selection_mode = "multi")

#         self.habit.set_habit_days(selection)

#     def submit_button(self):
        
#         if(st.button("Submit")):
#             st.rerun()
        

#     def display(self):
#         self.name_input()
#         self.date_input()
#         self.days_input()
#         self.submit_button()
        

