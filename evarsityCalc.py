#calculates required hours to make attendance atleast 75% and number of hours to bunk if attendance is greater than 75%

from bs4 import BeautifulSoup
from urllib.request import urlopen

#CONFIGURE 'loc' 'start' 'end' VARIABLES AS PER REQUIRMENT

#CHANGE 'loc' TO DIRECTORY WHERE WEBPAGE IS DOWNLOADED
loc = "file:///C:/Users/Abhishek/Downloads/Home%20Page4.html"

#CHANGE THE 'start' AND 'end' VARIABLES ACCORDING TO WEBPAGE
start = 101  #starting point of Attendance data retrived from soup.find_all mehthod
end = 172   #endng point of attendance data

#Function to calculate Attendance Status
def attendance_status(total, present):
    a=1
    perc = present / total * 100
    perc2 = perc
    #print(perc)
    if(perc < 75):
        index=0
        b = present
        c = total
        while(perc2 < 75):
            index = index + 1
            b = b+a
            c = c + a
            perc2 = b / c * 100
        return index
    else:
        index=0
        b = present
        c = total
        while(perc2 > 75):
            c = c+a
            perc2 = b / c * 100
            #print(perc2)
            index = index+1
        return index-1
#List with all subjects
sublist = ["THEORY OF COMPUTATION", "OPERATING SYSTEMS", "MULTI DISCIPLINARY DESIGN", "MINOR PROJECT - I", "INDUSTRIAL TRAINING", "DATABASE MANAGEMENT SYSTEMS", "MOBILE APPLICATION DEVELOPMENT", "DISCRETE MATHEMATICS", "BASIC APTITUDE - II"]

#indexing variables
i = 0
j=0
k=0
count = 0
flg = 0

#accessing data from webpage:


#relevent data is only after intervals of 7  with sub-interval of 4 datapoints
for x in range(start, end):
    if(i <7):   #interval 1
        if(j < 4 and count == 0 and flg == 0):  #interval 2
            page = urlopen(loc)
            soup = BeautifulSoup(page, "html.parser")
            data = soup.find_all('td')[x].get_text()
            #print(data)
            if(j==2):
                total = data
            if(j==3):
                present = data
                count = 1
                present = int (present)
                total = int (total)
                print(sublist[k])   #print the subject name from sublist
                k = k+1
                print("Total Hours = ",total)
                print("Present Hours = ",present)
                perc = present / total * 100    #percentage of attendance
                x = attendance_status(total , present)
                print("Total Percentage = ", perc)
                if(perc > 75):
                    print("Available to take leave = ", x)
                if(perc < 75):
                    print("Hours Required for Minimum Attendance = ",x)
                sub = sub +1
            j = j+1
            if(j == 4):
                j=0
        if(j<4 and count != 0):
            page = urlopen(loc)
            soup = BeautifulSoup(page, "html.parser")
            data = soup.find_all('td')[x].get_text()
            flg = flg+1
            if(flg == 5):
                flg = 0
                count = 0
                print("________________________________________________________")
        i = i+1
        if(i == 7):
            i = 0
#Abhishek Anand
#github.com/ra753
