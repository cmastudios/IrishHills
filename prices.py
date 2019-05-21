import pandas
import os

file = os.path.join(os.path.dirname(__file__), 'rates.xlsx')

with open(file, 'rb') as f:
    arr = pandas.read_excel(f)

with open(os.path.join(os.path.dirname(__file__), 'content/_list.md'), 'w') as out: 
    arr = arr.sort_values(by=['id'])
    for index, row in arr.iterrows():
        cottage = row['cottage']
        path = row['path']
        image = row['image']
        people = row['people']
        beds = row['beds']
        summer = row['summer']
        winter = row['winter']
        print(f"|[{cottage}](cottage/{path}.html) ![Exterior]({{static}}/images/{path}/{image}.JPG)|{people}|{beds}|${summer}|${winter}|", file=out)

with open(os.path.join(os.path.dirname(__file__), 'content/_summer.md'), 'w') as out: 
    arr = arr.sort_values(by=['summer'])
    for index, row in arr.iterrows():
        beds = row['beds']
        summer = row['summer']
        print(f"|{beds}|${summer}|", file=out)

with open(os.path.join(os.path.dirname(__file__), 'content/_winter.md'), 'w') as out: 
    arr = arr.sort_values(by=['winter'])
    for index, row in arr.iterrows():
        beds = row['beds']
        winter = row['winter']
        print(f"|{beds}|${winter}|", file=out)
