# NetworkPortQuiz
This is a CLI-based quiz game for learning basic network ports for the CompTIA A+ and Network+ exams.

The program is written in Python and uses a separate .csv file to store data for port numbers and their corresponding service for scalibility and ease of use.

## Some Notes
- There can be multiple answers for a single port, such as the acronym or the entire thing spelled out. All values after the first in each csv row are valid.
- All of the ports/services included are from the CompTIA A+ Exam objectives from the last two exam series (1001-1002 & 1101-1102).


## Recent Changes
- Added variables for quiz title and border decorations
- Changed a line to strip spaces from beginning/end of answers from .csv file
    - helps with accidental spacing after commas in csv file
    - does not modify the file itself