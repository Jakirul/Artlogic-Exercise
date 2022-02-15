# -*- coding: utf-8 -*-
#!/usr/bin/env python
import csv
import pandas as pd


def rows_to_csv(filepath, rows, columns=["Artist","ID","Stock number","Title","Dimensions"]):
    """
    Takes list of dictionaries and filepath and outputs a spreadsheet
    Params:
        rows(list):
            A list of dictionaries

        columns(list):
            A list of the key in the rows that you want to export in the csv file
            by defult it will display all

    """
    # list of dicts from the function below
    info = csv_to_rows(rows)

    # dataframe takes in the list of dicts
    df = pd.DataFrame(info)
    # converts it into a csv with all the columns specified
    df.to_csv(filepath, index=False, columns=columns)


def csv_to_rows(filepath):
    """
    Converts csv file to list of dicts.
    """
    dict_list = []
    with open(filepath, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        dict_list = list(reader)
        
    return dict_list


# rows_to_csv("new_file.csv", "data/artworks.csv", ["Artist", "ID"])

