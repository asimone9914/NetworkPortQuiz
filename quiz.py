"""
Title:    Network Port Quiz
Author:   Alex Simone
Date:     1-18-2023
Version:  2.0

Purpose:  This program will read values from a .csv file with
          data for network ports and their corresponding service.
          
          This data will be used to formulate questions and answers 
          to which the user will respond in a CLI environment.

"""

import csv
import pathlib
import random

# Set the location of the csv file
csv_file = pathlib.Path("ports.csv")


# Open csv file, return a dictionary with the values
def build_dict(csv_file):

    answer_dict = {}

    with open(csv_file, "r") as ports_file:
        c = csv.reader(ports_file)
        
        for row in c:
            answer_dict.update({row[0]:row[1::]})

    return answer_dict


# Main function
def main():

    # build the dictionary and assign keys (ports) to a list in order to index and randomly select them
    ports_dict = build_dict(csv_file)
    ports_list = []
    [ports_list.append(i) for i in ports_dict.keys()]
    
    # define loop control variable and sentinel value to exit loop
    running = True
    QUIT = "EXIT"
    
    print(f"\n=======================\n|| Network Port Quiz ||\n=======================\n\nType {QUIT} at any time to quit.\n")
    
    while running:
        # randomly select a port to quiz the user on
        port = ports_list[random.randint(0, len(ports_list) - 1)]
        prompt = f"\nWhat service belongs to port(s) {port}?: "
        
        # get the answer from the user
        user_answer = input(prompt).lower()
        
        # create a list for multiple correct answers
        correct_answers = []
        [correct_answers.append(i.lower()) for i in ports_dict.get(port)] 
        
        # decision structure for checking answers or exiting program
        if user_answer == QUIT or user_answer == QUIT.lower():
            print("\nExiting program...\n")
            running = False
        else:
            if user_answer in correct_answers:
                print(f"\n\nCorrect! :)\n\nPort {port} is associated with the service: ")
                [print("  " + service) for service in ports_dict.get(port)]
                print("\n")
            else:
                print(f"\nSorry, that is incorrect!\n\nCorrect answer(s): ")
                [print("  " + service) for service in ports_dict.get(port)]
                print("\n")


if __name__ == "__main__":
    if csv_file.exists():
        main()
    else:
        print(f"[ERROR] File {csv_file} not found!\nExiting program...")

