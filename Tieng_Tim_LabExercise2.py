# Course: IST-652 Scripting For Data Analysis
# Student: Tim Tieng
# Lab Number: 2
# Due Date: April 21, 2023

# Lab 2 Prompt:
# Use the NBA-Attendance-2015.txt and the 2-4-1ReadingFiles jupyter program as a starting point to read in the data. Then for each line, create a string using string and number formatting that puts the team, total attendance, average attendance, and capacity into a formatted string. Each line should look something like:
# ‘The overall attendance at Atlanta was 13,993, average attendance was 9,456 and the capacity was 102.06%’

NBAAttendanceFile = open ('/Users/timtieng/Library/CloudStorage/OneDrive-Personal/Desktop/Masters in Applied Data Science/IST-652 Scripting For Data Analysis/Week 2 - Booleans and Dictionairs/nba-attendance-2015.txt', 'r')

# Data Columns = Team Rank (0), Team Name (1), Total Attendance(2), Average Attendance(3), Percent Capacity(4)

# Itereate through the file 

numberOfTeams = 0
NBATeams = []

for line in NBAAttendanceFile:
    # increment numberOfTeams by 1
    numberOfTeams += 1
    # Strip the newline
    textLine = line.strip()
    # strip on the whitespaces
    singleTeam = textLine.split()
    # Append to NBATeams
    NBATeams.append(singleTeam)

# Test by Printing
# print(NBATeams)

for team in NBATeams:
    print(f"The overall attendance for the {team[1]} in the year 2015 was {team[2]}. The average attendance was {team[3]}, and the capacity was {team[4]}")