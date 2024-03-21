'''
5. The Fitness Tracker

Objective:
The aim of this assignment is to create a program that tracks fitness activities and calories burned.

Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = 
[’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, 
Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.


Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, 
Total calories burned = Duration (in minutes)*3.5

Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.
'''

class FitnessTracker:
    def __init__(self):
        self.activities = {}

    def log_activity(self, activity, duration):
        if activity in self.activities:
            self.activities[activity] += duration
        else:
            self.activities[activity] = duration

    def estimate_calories_burned(self, activity, duration):
        return duration * 3.5  # Assuming a constant of 3.5 calories burned per minute

    def generate_summary(self):
        total_calories_burned = 0
        print("Fitness Activity Summary:")
        for activity, duration in self.activities.items():
            calories_burned = self.estimate_calories_burned(activity, duration)
            total_calories_burned += calories_burned
            print(f"{activity}: {duration} minutes, Calories Burned: {calories_burned}")
        print("Total Calories Burned for the day:", total_calories_burned)

def main():
    tracker = FitnessTracker()
    tracker.log_activity('Dancing', 10)
    tracker.log_activity('Swimming', 20)
    tracker.log_activity('Biking', 15)
    
    tracker.generate_summary()

if __name__ == "__main__":
    main()


main()