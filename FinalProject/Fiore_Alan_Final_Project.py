import random


class Course:
    def __init__(self, name, credit_hours, letter_grade):
        self.name = name
        self.credit_hours = credit_hours
        self.letter_grade = letter_grade

    def __str__(self):
        return f"{self.name}, {self.credit_hours} credits, Grade: {self.letter_grade}"  # returns string of name of
        # course, credit hours, and the grade


class Student:
    def __init__(self, full_name, email, major, project_info):
        self.full_name = full_name   # define instance variables
        self.email = email
        self.major = major
        self.project_info = project_info
        self.courses = []  # creates an empty list to store courses
        self.letter_grade_to_gpa_dictionary = {
            'A+': 4.0,
            'A': 4.0,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3.0,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2.0,
            'C-': 1.7,
            'D+': 1.3,
            'D': 1.0
        }  # associates letter grade with number grade

    def add_course(self, course):
        self.courses.append(course)  # adds courses to course list

    def letter_grade_to_gpa(self, letter_grade):
        return self.letter_grade_to_gpa_dictionary[letter_grade]  # returns number associated with inputted letter
        # grade

    def calculate_gpa(self):
        total_quality_points = 0  # initializes quality points
        total_credit_hours = 0  # initializes credit hours

        for course in self.courses:
            course_gpa = self.letter_grade_to_gpa(course.letter_grade)  # gets the number associated with GPA
            quality_points = course_gpa * course.credit_hours  # calculate quality points
            total_quality_points += quality_points  # add the quality points to total quality points
            total_credit_hours += course.credit_hours  # add the credit hours to total credit hours

        return total_quality_points / total_credit_hours  # divide the total quality points by total credit hours to
        # calculate overall gpa

    def print_student_gpa(self):
        overall_gpa = self.calculate_gpa()  # get the overall gpa
        print()
        print(f"{self.full_name}, {self.email}, {self.major}, {self.project_info}")  # prints name, email, and major
        print()
        print(f"COURSES:")

        for course in self.courses:  # prints the courses
            print(course)
        print()
        print(f"FINAL GPA: {overall_gpa:.2f}")  # prints final gpa


def calculate_student_gpa():
    student_info_string = input(
        "Enter full name, email, major and project info (separated by commas): ")
    student_info_list = student_info_string.split(",")  # creates a list of all the student information

    student_full_name = student_info_list[0].strip()  # splits list into respective inputs
    student_email = student_info_list[1].strip()
    student_major = student_info_list[2].strip()
    student_project_info = student_info_list[3].strip()

    my_student = Student(student_full_name, student_email, student_major, student_project_info)
    # calls Student object

    number_courses = input("How many courses do you want to add (2-6): ").strip()  # gets number of courses

    while not (number_courses.isdigit() and 2 <= int(number_courses) <= 6):  # validates if input is a number and
        # between 2 and 6
        number_courses = input("Invalid input. How many courses do you want to add (2-6): ").strip()

    number_courses = int(number_courses)  # converts string to number

    for i in range(number_courses):  # loop to call amount of courses the user wants to input
        course_info_string = input("Enter course name, credit hours, and letter grade separated by "
                                   "commas: ")  # ask for course input
        course_info_list = course_info_string.split(",")  # split using ","

        course_name = course_info_list[0].strip()  # create variables according to order in list
        course_credit_hours = float(course_info_list[1].strip())
        course_letter_grade = course_info_list[2].strip()

        course = Course(course_name, course_credit_hours, course_letter_grade)  # call Course object
        my_student.add_course(course)  # add these course to add course in student

    my_student.print_student_gpa()  # calls the print object to print student's gpa


def lottery_number_generator():
    minNumber = 1  # sets minimum number for first 5 random letters
    maxNumber = 69  # sets maximum number for first 5 random letters

    first_five_lottery_numbers_list = []

    for i in range(5):  # generates 5 numbers from 1-69 and puts them in a list
        randomNumber = random.randint(minNumber, maxNumber)
        while randomNumber in first_five_lottery_numbers_list:  # checks that the number is not a duplicate
            randomNumber = random.randint(minNumber, maxNumber)
        first_five_lottery_numbers_list.append(randomNumber)

    first_five_lottery_numbers_list.sort()  # sorts the five numbers in ascending order

    minNumber = 1  # sets minimum number for last random letter
    maxNumber = 26  # sets maximum number for last random letter

    last_lottery_number_list = []  # empty list for last number

    randomNumber = random.randint(minNumber, maxNumber)  # generates a random number between 1-26
    last_lottery_number_list.append(randomNumber)  # appends this number to the end of the list

    lottery_number = first_five_lottery_numbers_list + last_lottery_number_list  # merges lists together and creates
    # a list with 6 items, the first five in ascending order, and the last number is a random one from 1-26
    print("Your Powerball numbers: ", end="")
    print(*lottery_number)  # prints the list without brackets


def show_pig_latin():
    englishSentence = input("Enter a sentence: ").upper()  # asks user to enter a sentence
    englishSentenceList = englishSentence.split()  # splits the sentence by spaces

    pigLatinList = []  # initializes the list that will store converted words

    for eachItem in englishSentenceList:  # iterates through the english sentence list
        pigLatinWord = eachItem[1:] + eachItem[0] + "".join("AY")  # creates pig latin word through
        # index and join
        pigLatinList.append(pigLatinWord)  # adds each new pig latin word to the pig latin list

    print(*pigLatinList)  # prints out the pig latin sentence with no


def show_rock_paper_scissors_game():
    computerChoiceNumber = random.randint(1, 3)  # computer generates a random integer

    if computerChoiceNumber == 1:  # set computer integer to rock, paper, or scissor
        computerChoiceWord = "rock"
    elif computerChoiceNumber == 2:
        computerChoiceWord = "paper"
    else:
        computerChoiceWord = "scissors"

    playerChoiceWord = input("Enter rock, paper, or scissors: ").lower().strip()  # ask player to choose rock, paper
    # or scissors

    while playerChoiceWord not in ["rock", "paper", "scissors"]:  # validate input
        playerChoiceWord = input("Invalid choice. Enter rock, paper, or scissors: ").lower().strip()

    if playerChoiceWord == "rock":  # set rock, paper, or scissor to a number
        playerChoiceNum = 1
    elif playerChoiceWord == "paper":
        playerChoiceNum = 2
    else:
        playerChoiceNum = 3

    if playerChoiceNum == computerChoiceNumber:  # if computer number is the same as player number loop previous code
        print(f"Computer had {computerChoiceWord}. You chose {playerChoiceWord}. It's a tie! Play again.")
        show_rock_paper_scissors_game()  # calls the function to restart the game

    elif (playerChoiceNum == 1 and computerChoiceNumber == 3) or \
            (playerChoiceNum == 2 and computerChoiceNumber == 1) or \
            (playerChoiceNum == 3 and computerChoiceNumber == 2):  # checks conditions for you to win
        print(f"Computer had {computerChoiceWord}. You had {playerChoiceWord}. {playerChoiceWord.capitalize()} beats "
              f"{computerChoiceWord}. YOU WIN!")
    else:  # checks conditions for you to lose
        print(f"Computer had {computerChoiceWord}. You had {playerChoiceWord}. {computerChoiceWord.capitalize()} beats "
              f"{playerChoiceWord}. You Lost :(")


def main():
    menu = "------------------------------------------------\nWelcome to the final project.\nEnter 1 to Calculate " \
           "Student GPA" "\n""Enter 2 for Lottery Number Generator\n""Enter 3 for Pig Latin\n""Enter " \
           "4 for Rock, Paper, Scissors Game\n"
    print(menu)  # prints menu
    menuInput = input("Enter Menu option 1,2,3,4  9 to exit: ")  # asks for input

    optionList = ["1", "2", "3", "4", "9"]
    while menuInput not in optionList:  # input validation
        menuInput = input("Invalid input. Enter Menu option 1,2,3,4  9 to exit: ")

    menuInput = int(menuInput)  # converts the input to a number

    while menuInput != 9:  # while user doesn't input 9, the menu is printed and input is asked for

        if menuInput == 1:
            calculate_student_gpa()  # calls calculate_student_gpa() function
        elif menuInput == 2:
            lottery_number_generator()  # calls lottery_number_generator() function
        elif menuInput == 3:
            show_pig_latin()  # calls show_pig_latin() function
        else:
            show_rock_paper_scissors_game()  # calls show_rock_paper_scissors_game() function

        print(menu)  # prints the menu
        menuInput = input("Enter Menu option 1,2,3,4  9 to exit: ")  # asks for user input

        optionList = ["1", "2", "3", "4", "9"]
        while menuInput not in optionList:  # input validation
            menuInput = input("Invalid input. Enter Menu option 1,2,3,4  9 to exit: ")
        menuInput = int(menuInput)  # converts the input to a number

    print("You selected option 9. Exiting the program. Good-bye.")  # exits the program


if __name__ == "__main__":
    main()
