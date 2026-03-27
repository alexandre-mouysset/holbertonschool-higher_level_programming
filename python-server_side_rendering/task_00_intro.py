#!/usr/bin/python3
# Verif
def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("template must be a string")
        return
    if template == "":
        print("template must not be empty")
        return

    if not isinstance(attendees, list):
        print("attendees must be a list")
        return
    if len(attendees) == 0:
        print("attendees must not be empty")
        return

    for element in attendees:
        if not isinstance(element, dict):
            print("attendees must be a list of dictionaries")
            return

    # generation
    count = 1
    for attendee in attendees:
        new_template = template

        name = attendee.get("name")
        if (name is None):
            name = "N/A"
        new_template = new_template.replace("{name}", name)

        event_title = attendee.get("event_title")
        if (event_title is None):
            event_title = "N/A"
        new_template = new_template.replace("{event_title}", event_title)

        event_date = attendee.get("event_date")
        if (event_date is None):
            event_date = "N/A"
        new_template = new_template.replace("{event_date}", event_date)

        event_location = attendee.get("event_location")
        if (event_location is None):
            event_location = "N/A"
        new_template = new_template.replace("{event_location}", event_location)

        filename = f"output_{count}.txt"
        with open(filename, 'w') as file:
            file.write(new_template)
        count += 1
