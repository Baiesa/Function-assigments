'''
3. The Grade Analyzer

Objective:
The aim of this assignment is to analyze a set of grades and provide statistics.

Task 1: Code a function to calculate the average grade.
Task 2: Implement a function to find the highest and lowest grade.
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
'''

class GradeAnalyzer:
    def __init__(self, grades):
        self.grades = grades

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def find_highest_grade(self):
        if self.grades:
            return max(self.grades)
        else:
            return None

    def find_lowest_grade(self):
        if self.grades:
            return min(self.grades)
        else:
            return None

    def categorize_grades(self):
        if not self.grades:
            print("No grades to categorize.")
            return

        letter_grades = []
        for grade in self.grades:
            if grade >= 90:
                letter_grades.append('A')
            elif grade >= 80:
                letter_grades.append('B')
            elif grade >= 70:
                letter_grades.append('C')
            elif grade >= 60:
                letter_grades.append('D')
            else:
                letter_grades.append('F')
        return letter_grades

def main():
    grades = [85, 92, 78, 90, 60, 70]
    analyzer = GradeAnalyzer(grades)
    
    average = analyzer.calculate_average()
    highest = analyzer.find_highest_grade()
    lowest = analyzer.find_lowest_grade()
    letter_grades = analyzer.categorize_grades()

    print("Grade Statistics:")
    print("Average Grade:", average)
    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)
    print("Letter Grades:", letter_grades)

if __name__ == "__main__":
    main()

main()