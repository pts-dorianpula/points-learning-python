import csv


def solution_1():
    with open('llc-workshop-data.csv') as csv_file:
        csv_data = csv.DictReader(csv_file)

        num_sign_ups = 0

        for row in csv_data:
            if 'National Learn to Code Day' in row['Event Name']:
                attendees = int(row['Quantity'])
                num_sign_ups += attendees

        message = 'Number of attendees for National Learn to Code Day events: '
        message += str(num_sign_ups)
        print(message)


def solution_2():
    with open('llc-workshop-data.csv') as csv_file:
        csv_data = csv.DictReader(csv_file)

        num_sign_ups = 0

        for row in csv_data:
            if 'Kids Learning Code' in row['Event Name'] or \
                'Girls Learning Code' in row['Event Name']:
                attendees = int(row['Quantity'])
                num_sign_ups += attendees

        message = 'Number of attendees for: '
        message += str(num_sign_ups)
        print(message)


def solution_3():
    with open('llc-workshop-data.csv') as csv_file:
        csv_data = csv.DictReader(csv_file)

        attendee_sign_ups = 0
        mentor_sign_ups = 0

        for row in csv_data:
            if 'Girls Learning Code' in row['Event Name']:
                if 'mentor' in row['Ticket Type'] or 'Volunteer' in row['Ticket Type']:
                    mentor_sign_ups += int(row['Quantity'])
                else:
                    attendee_sign_ups += int(row['Quantity'])

        print('Number of attendees: ' + str(attendee_sign_ups))
        print('Number of mentors: ' + str(mentor_sign_ups))
        print('Ratio of mentor to attendee: ' + str(
            mentor_sign_ups / attendee_sign_ups))


def write_to_file():
    with open('llc-workshop-data.csv') as csv_file:
        csv_data = csv.DictReader(csv_file)

        with open('filtered-data.csv', 'w') as filtered_csv:
            write_csv = csv.DictWriter(filtered_csv, csv_data.fieldnames)
            write_csv.writeheader()

            for row in csv_data:
                if 'Girls Learning Code' in row['Event Name']:
                    if row['How did you hear about this event?']:
                        write_csv.writerow(row)


def find_types_from_filtered():
    with open('filtered-data.csv') as csv_file:
        csv_data = csv.DictReader(csv_file)

        heard_in_tally = dict()
        for row in csv_data:
            heard_in = row['How did you hear about this event?']
            if heard_in in heard_in_tally.keys():
                heard_in_tally[heard_in] += 1
            else:
                heard_in_tally[heard_in] = 1

        for item in heard_in_tally.keys():
            print(item + ": " + str(heard_in_tally[item]))
