# Irish Hills Website
# Copyright (C) 2019 Connor Monahan
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import pandas
import os

file = os.path.join(os.path.dirname(__file__), 'rates.xlsx')

with open(file, 'rb') as f:
    arr = pandas.read_excel(f)

with open(os.path.join(os.path.dirname(__file__), 'theme/templates/_list.md'), 'w') as out: 
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

with open(os.path.join(os.path.dirname(__file__), 'theme/templates/_summer.html'), 'w') as out: 
    arr = arr.sort_values(by=['summer'])
    for index, row in arr.iterrows():
        beds = row['beds']
        summer = row['summer']
        print(f"<tr><td class=\"rate-1\">{beds}</td><td class=\"rate-2\">${summer}</td></tr>", file=out)

with open(os.path.join(os.path.dirname(__file__), 'theme/templates/_winter.html'), 'w') as out: 
    arr = arr.sort_values(by=['winter'])
    for index, row in arr.iterrows():
        beds = row['beds']
        winter = row['winter']
        print(f"<tr><td class=\"rate-1\">{beds}</td><td class=\"rate-2\">${winter}</td></tr>", file=out)
