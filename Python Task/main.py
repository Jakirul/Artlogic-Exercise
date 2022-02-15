#!/usr/bin/env python
import csv
from lib.csvfile import rows_to_csv
import pandas as pd 

def create_new_stock_numbers():
    rows_to_csv("stock_number.csv", "data/artworks.csv", ["Artist", "Stock number"])
    """
    Exercise 2
    Write something here which describes what you want your function to do.
    This will help you when creating it...

    It will take in the 'stock_number.csv' which is loaded using the 'row_to_csv' function

    It will then drop all empty fields

    After it will drop any stock format numbers without a specified format (such as AB/ABC 123/1234) and then save it to the 'stock_numbers' csv

    It looks over the stock numbers csv and checks if a prefix exists. If it doesnt, it appends it into an array and at the end, saves it into the
    new_stock_numbers.csv
    
    """

    # drops all empty values and stores it back into the stock_number csv
    df = pd.read_csv("stock_number.csv")
    df = df.dropna()
    df = pd.DataFrame(df)
    df.to_csv("stock_number.csv", index=False)
    
    # Drops all stock numbers without the format of 'AB/ABC 123/1234'
    df = df[df['Stock number'].str.split().str.len().ge(2)]
    df.to_csv("stock_number.csv", index=False)
    

    artist_prefix = {}
    dict_val = {}
    artist_list = []
    lists = []

    # Opens the recently changed stock_number csv file
    with open("stock_number.csv", "r") as read_csv:
        # Treats it as a dictionary rather than array format
        reader = csv.DictReader(read_csv)

        # Loops over each value in the csv
        for line in reader:
            # Splits the name into an array
            artist_split = line['Artist'].split(" ")
            # Appends all artists into a list
            artist_list.append(line['Artist'])
            
            # If the artist only has one name, then it will use the first two letters as the initial
            if len(artist_split) == 1:
                prefix = ''.join([x[0:2].upper() for x in line['Artist'].split(' ')])
            # If it has two names, then it will use the first letter from each name as the initials
            elif len(artist_split) == 2:
                prefix = ''.join([x[0].upper() for x in line['Artist'].split(' ')])
            # If the name has more than 2 names, it will use the first letter of the first name and first letter of the last word as the initials
            else:
                prefix = artist_split[0][0] + artist_split[len(artist_split) - 1][0]
               
            value = 0
            val = False
            # If the initial is inside the artist prefix...
            if prefix in artist_prefix:
                # If the prefix isnt equal to the artist name...
                if artist_prefix[prefix] != line['Artist']:
                    # val will be true if one persons prefix doesnt match another persons prefix
                    while val is not True:
                        # Creates a prefix where the value will increase each time to make sure we get a unique prefix
                        temp_prefix = artist_split[0][0].upper() + artist_split[len(artist_split) - 1][value].upper()
                        
                        # If the prefix isnt in the artist_prefix list, then append artist_prefix dict with that artist name and prefix
                        if temp_prefix not in artist_prefix:
                            
                            artist_prefix[temp_prefix] = line['Artist']
                            prefix = artist_split[0][0].upper() + artist_split[len(artist_split) - 1][value].upper()
                            # val gets set to True to exit out of the while loop
                            val = True

                        else:
                            # Increments value to keep checking for a unique value
                            value+=1

            else:
                # Appends the artist prefix dict with the artist name 
                artist_prefix[prefix] = line['Artist']

            number = line['Stock number'].split(" ")
            
            # if a stock number has 4 values (like KD 0002), it will cut the first 0 out to make it 002
            if (len(number[1]) > 3):
                number[1] = number[1][1:len(number[1])]
            # Appends the list array with the prefix followed by the stock numbers
            lists.append(f"{prefix} {number[1]}")
           
        
        # Appends the dictionary with the artist name and new stock number
        dict_val['Artist'] = artist_list
        dict_val['Stock number'] = lists

        # Turns it into a dataframe
        df = pd.DataFrame(dict_val)
        # Creates a new csv with the artist name and stock number seperated with a tab with no index
        df.to_csv("new_stock_numbers.csv", index=False, sep="\t")
            



create_new_stock_numbers()
