"""
Title:    Network Port Quiz
Author:   Alex Simone
Date:     1-24-2023
Version:  2.10

Purpose:  This program will read values from a .csv file with
          data for network ports and their corresponding service.
          
          This data will be used to formulate questions and answers 
          to which the user will respond in a CLI environment.

"""

import csv
import pathlib
import random
import sys
import subprocess


class NetworkPortQuiz():

    # constructor method, set custom values here
    def __init__(self):
        # CSV file with port numbers and answers
        self.ports_csv_file = pathlib.Path("ports.csv")

        # Title, border design, separator decorations
        self.TITLE = "Network Port Quiz"
        self.HORZ_BORDER = "=" * (len(self.TITLE) + 6)
        self.VERT_BORDER = "||"
        self.SEPARATOR = "--" * 24

        # Used to quit during quiz game
        self.QUIT = "EXIT"

        # Start the program
        self.running = True
        self.options_menu()

    # Clear the terminal screen
    def clear_screen(self):
        if sys.platform == "win32":
            subprocess.run("cls", shell=True)
        else:
            subprocess.run("clear", shell=True)

    # Create a dictionary for ports and services from the .csv file
    def build_answer_dict(self):
        # keys = ports, values = possible answers
        self.answer_dict = {}
        self.valid_input = True

        if self.ports_csv_file.exists():
            with open(self.ports_csv_file, "r") as ports_file:
                try:
                    c = csv.reader(ports_file)

                    for row in c:
                        self.answer_dict.update({row[0]: row[1::]})

                except IndexError:
                    print(
                        "\n\n[ ERROR! ]\nSomething went wrong while reading your .csv file.\n\nPlease check that it is formatted correctly and try again.\n")
                    self.valid_input = False
                    self.running = False
        else:
            print(
                f"\n\n[ ERROR! ]\n.csv file: \"{self.ports_csv_file}\" not found!\n\nExiting program...")
            self.valid_input = False
            self.running = False

    # Options menu start screen
    def options_menu(self):
        self.section_1 = "Start quiz game"
        self.section_2 = "About the game"
        self.section_3 = "Exit the game"

        while self.running:
            try:
                print(f"\n[ {self.TITLE} Options Menu ]\n")
                print(
                    f"1.) {self.section_1}\n2.) {self.section_2}\n3.) {self.section_3}")

                user_input = int(input("\nEnter a selection (1-3): "))

                if 0 < user_input <= 3:
                    if user_input == 1:
                        self.start_quiz()

                    if user_input == 2:
                        self.about_quiz()

                    if user_input == 3:
                        print("\nExiting game...")
                        self.running = False
                else:
                    self.clear_screen()
                    print("Please enter a value between 1 and 3!\n")

            except ValueError:
                self.clear_screen()
                print("Please enter a number!\n")

    # Additional info about the program
    def about_quiz(self):
        self.clear_screen()

        print(f"\n[ {self.section_2} ]\n")

        print(
            "\nThis is a simple quiz game designed to help with memorizing network ports and their corresponding service",
            f"\n\nThe quiz currently is reading data from a file located at: \n  \"{self.ports_csv_file.absolute()}\"\n")

        print("This file can be modified to add new ports/services, or modify or remove existing ones.\n\n" +
              "The file is in .csv (comma-separated values) format. Typically, you should not place spaces after the commas, \n" +
              "however if you do, this program will remove them and it will not affect the integrity of the port or answer.\n")

        print(self.SEPARATOR)

    # Start quiz game
    def start_quiz(self):

        # build the ports/answers dictionary
        self.build_answer_dict()

        if self.valid_input == True:

            # ports list used to index and randomly select port numbers
            ports_list = []
            [ports_list.append(i) for i in self.answer_dict.keys()]

            # counter for total questions, questions correct
            self.question_counter = 1
            self.questions_correct = 0

            # main loop
            while self.running:

                # clear screen before every question
                self.clear_screen()

                # Display a pretty title graphic
                print(f"\n{self.HORZ_BORDER}\n{self.VERT_BORDER} {self.TITLE} {self.VERT_BORDER}\n{self.HORZ_BORDER} \n\nType {self.QUIT} at any time to quit.\n")

                # Display the question counter
                print(
                    f"\n{self.SEPARATOR}\n Question #{self.question_counter}\n{self.SEPARATOR}")

                # randomly select a port to quiz the user on
                port_number = ports_list[random.randint(
                    0, len(ports_list) - 1)]

                # ask the question and get user input
                prompt = f"\nWhat service belongs to port(s) {port_number}?: "
                user_answer = input(prompt).lower()

                # create a list for multiple correct answers for the current question
                correct_answers = []
                [correct_answers.append(i.lower().strip())
                    for i in self.answer_dict.get(port_number)]

                # selection structure for handling user input
                if user_answer == self.QUIT or user_answer == self.QUIT.lower():
                    self.question_counter -= 1
                    print("\nExiting quiz...\n")
                    self.running = False
                else:
                    self.question_counter += 1

                    # if answer is correct
                    if user_answer in correct_answers:
                        self.questions_correct += 1

                        print(
                            f"\n\nCorrect! :)\n\nPort {port_number} is associated with the service: ")
                        [print("  " + answer)
                            for answer in self.answer_dict.get(port_number)]
                        print(self.SEPARATOR)

                        # need to find an alternative to this, but this will do for now...
                        input("\nPress Enter to continue...")

                    # if answer is incorrect
                    else:
                        print(f"\nSorry, that is incorrect!\n\nCorrect answer(s): ")
                        [print("  " + answer)
                            for answer in self.answer_dict.get(port_number)]
                        print(self.SEPARATOR)

                        # need to find an alternative to this, but this will do for now...
                        input("\nPress Enter to continue...")

            # print questions correct out of total after loop ends
            print(
                f"You answered {self.questions_correct} out of {self.question_counter} questions correctly!")


if __name__ == "__main__":
    QuizGame = NetworkPortQuiz()
