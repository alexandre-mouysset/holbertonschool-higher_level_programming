#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_file):
    list = []
    try:
        with open(csv_file, "r", encoding="UTF-8") as csv_filename:
            csv_Data = csv.DictReader(csv_filename)
            for row in csv_Data:
                list.append(row)

        with open("data.jason", "w", encoding="UTF-8") as csv_filename:
            json.dump(list, csv_filename)
            return True

    except FileNotFoundError:
        return False
