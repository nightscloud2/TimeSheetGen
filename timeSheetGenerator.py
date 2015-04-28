#Version 1.4 script now automatically edits the imacro script.

#Planned updates for Version 1.5, replace hard coded time with datetime objects.
#from datetime import date
#date = date.today() initializes a datetime obj with current date

month = 4  #replace with month = date.strftime("%m").lstrip("0") consider type casting into an int
startDate = 6 #replace with startDate = date.strftime("%d").lstrip("0")
year = 2015 #replace with year = 
count = 0 
week = ["mon","tue","wed","thr","fri"] #consider using datetime object to return week instead of building it manually here.
day = 0 #very arbitrary value used to track which day of week as week[day] consider using datetime object.
outputList = [] #consider opening file in the begining and writing lines as they're created, maybe more efficent than writing all at the end.
#consider importing calendar and using a calendar function call to return the last day of the month, would remove next 6 lines of code.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    monthEndDate = 31
else:
    monthEndDate = 30
   
if month == 2:
    monthEndDate = 28
 
while count < 10:
    date = str(month) + "_" + str(startDate) + "_" + str(year) #remove type cast to string, unless casted at declaration
    outputList.append("TAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInHour1" + date + " CONTENT=%08:30\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInAMPM1" + date + " CONTENT=%AM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutHour1" + date + " CONTENT=%12:30\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutAMPM1" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInHour2" + date + " CONTENT=%12:30\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInAMPM2" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutHour2" + date + " CONTENT=%01:00\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutAMPM2" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:svcName2" + date + " CONTENT=%1_0_1972\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:svcName1" + date + " CONTENT=%0_0_1974\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInHour3" + date + " CONTENT=%01:00\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInAMPM3" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutHour3" + date + " CONTENT=%05:00\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutAMPM3" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:svcName3" + date + " CONTENT=%0_0_1974\n")
 
    if week[day] == "fri": #if the whole "week" list is only used to calculate which day you're on, consider using datetime object. look for function that returns the day, when given a datetime object.
        startDate +=3
        day = -1
    else:
        startDate += 1 #will need to type cast startDate into an int to add 1
 
    if startDate > monthEndDate:
        startDate = startDate - monthEndDate #cast into int
        month +=1 #cast into int
        
    day += 1
    count += 1

file = open("#Current.iim","w") #consider creating a file with command line- touch file.iim instead of using #current. 
file.writelines(outputList)
file.close()
