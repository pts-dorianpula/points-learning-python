# Import the csv library
import csv

# Open the 'llc-chapters.csv' file

    # Convert it to a csv_data structure

    # Loop through each of the rows

        # Compare the 'City' in the row with your city

            # Print a thank you message to your chapter lead(s)

with open('llc-chapters.csv') as chapters_file:
    chapters_data = list(csv.DictReader(chapters_file))
    print(chapters_data[0].keys())
    for chapter in chapters_data:
        if chapter['City'] == 'Toronto':
            print("Thank you " + chapter['Chapter Lead(s)'] + "!")
