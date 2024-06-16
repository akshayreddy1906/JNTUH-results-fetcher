# Fetching JNTUH Results through CLI
#### Video Demo:  <https://youtu.be/Tn_3HDS0xtQ>
#### Description:
This is a command-line interface (CLI) application that fetches and displays results from the Jawaharlal Nehru Technological University Hyderabad (JNTUH) API.

## Features

- Fetch academic results using a student's hall ticket number
- Display total GPA
- Show detailed semester-wise subject results
- Display semester-wise CGPA and credits

## Requirements

- Python 3.x
- `requests` library
- `tabulate` library

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:
pip install requests tabulate

## Usage

Run the script using Python:
python project.py


Follow the prompts to:

1. Enter the student's hall ticket number.
2. Choose from the following options:
   - Display total GPA
   - Display semester details
   - Display semester CGPA and credits
   - Exit the program

For semester details and CGPA/credits, you can enter specific semesters (e.g.,"2-1" ) or group of semesters  (e.g.,"1-1 1-2") or "ALL" for all semesters.

## Functions

- `main()`: The main function that handles user input and API requests.
- `display_total_gpa(data)`: Displays the total GPA.
- `display_semester_details(data)`: Shows detailed results for selected semesters.
- `display_cgpa_credits(data)`: Displays CGPA and credits for selected semesters.

## API

This script uses the JNTUH Results API:
https://jntuhresults.up.railway.app/api/academicresult?htno=<HALLTICKET_NUMBER>


## Note

This script is for educational purposes and depends on the availability and structure of the JNTUH Results API. Make sure you have permission to access and use the data.
