"""
File:         p1.py
Author:       Seth Chu
Date:         10/26/2022
Lab Section:  31
Email:        li22854@umbc.edu
Description:  Function will parse through given lists within dataEntry.py
              and display different details of each list. Function will
              display, first student that swiped into class, students who
              were late to class, a list of all times that were checked
              in, list of all times checking in or out, and students who
              were not in class
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''

def list_students_not_in_class(roster, attend):
    """
    Compare the swipe log with the given course roster. Place those students that
    did not show up for class into a list.
    :param roster: given list of student names 
    :param attend: list of complete attendance information
    :return: list of students that were not in class
    """
    #splits attend_ls into each individual item of information
    split_item(attend)
    names_attended = get_names(attend)
    absent_ls = []
    
    for name in roster:
        if name not in names_attended:
            #append student name to absent_ls if the studetn name is not in the names_attended list
            absent_ls.append(name)

    #splits item to prevent buggy output
    split_item(absent_ls)
    
    return absent_ls

def list_all_times_checking_in_and_out(name, attend):
    """
    Looking at the swiping log, this function will list all in and outs for a
    particular Student. Please note, as coded in the p1.py file given, this
    function was called three times with different student values. 
    :param name: name of student that user wants to check attendance data for
    :param attend: list of complete attendance data
    :return: students swipe in and out information
    """
    #gets students name
    swipe_info = []
    names_attended = get_names(attend)
        
    #looks for student in the attend list
    for i in range(len(names_attended)):
        #if student is in the attend list
        if name in names_attended[i]:
            swipe_info.append(attend[i])
    
    #return student swipe data
    return swipe_info

def list_all_times_checked_in(attend):
    """
    This function returns a list of when all student(s) FIRST swipe in. 
    :param attend: complete list of attendance data 
    :return: list of check in data
    """    
    check_in = []
    check_name = []
    name_ls = get_names(attend)

    
    for i in range(len(attend)):
        #adds name to check_name if current indexed name list is not in check_name
        #will also add the check in info for whoever to check_in
        if name_ls[i] not in check_name:
            check_name.append(name_ls[i])
            check_in.append(attend[i])
    
    return check_in

def list_students_late_to_class(ontime, attend):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in.
    :param time: indicates when the class starts 
    :param attend: list of complete attendance data
    :return: a list of students late to class
    """
    check_in_ls = list_all_times_checked_in(attend)
    late_ls = []
    time_ls = []
    
    #converts the class starting time to seconds
    on_time = ontime.split(':')
    for i in range(len(on_time)):
        on_time[i] = int(on_time[i])
        if i == 0:
            on_time[i] *= (60**2)
        if i == 1:
            on_time[i] *= 60
    ontime_sum = sum(on_time)
    
    #splits times in list and converts to seconds
    time_ls = split_time(time_ls, check_in_ls)
    
    #if any time in time_ls is greater than the class starting time
    #append the complete data to the late_ls
    for i in range(len(time_ls)):
        if time_ls[i] > ontime_sum:
            late_ls.append(check_in_ls[i])

    return late_ls

def get_first_student_to_enter(attend):
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter.
    :param attend: list of complete attendance data
    :return: a print statement with the first student to enter
    """
    time_ls = []
    first_student = 0
    
    time_ls = split_time(time_ls, attendData)
    #sets early to the first item in the list
    early = time_ls[0]
    
    #compares early with every other time in the list
    #if early is less than or equal to another time on the list
    #then early gets set to that time
    for sec in range(len(time_ls)):
        if time_ls[sec] <= early:
            early = time_ls[sec]
            first_student = sec

    #returns print statement showing which student arrived first
    return "{}, {}".format(attend[first_student][0], attend[first_student][1])

def printList(ls):
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param ls: desired list to print 
    :return: ls
    """
    if len(ls) > 0:
        for i in ls:
            print(','.join(i))
    elif len(ls) == 0:
        print("********************************")

def split_item(attend):
    ls_len = len(attend)
    #splits each entry into lastName, firstName, swipeTime, date
    for item in range(ls_len):
        student_str = str(attend[item])
        attend[item] = student_str.split(",")
    return attend
    
def split_time(time, attend):
    """
    Splits just the time of complete attendance data into separate integers and converts time to seconds
    :param time: list of times separated by hour, minute, second
    :param attend: list of complete attendance data
    :return: updated time list of times converted to seconds
    """
    ls_len = len(attend)
    #splits time into hours, minutes, seconds
    for sect in range(ls_len):
        time_sep = attend[sect][2].split(':')
        time.append(time_sep)
    
    #casts each hour, min, sec to an integer
    for typ in range(len(time)):
        for l in range(len(time[typ])):
            time_int = int(time[typ][l])
            time[typ][l] = time_int
            
        #converts hours to seconds
        time[typ][0] = time[typ][0] * (60**2)
        #converts minutes to seconds
        time[typ][1] = time[typ][1] * 60
        
        #sum each sublist
        time[typ] = sum(time[typ])
    
    return time

def get_names(user_list):
    """
    Gets just the last and first name from a list (or just list[i][0] and list[i][1])
    :param user_list: a list given specified in the function call
    :return: list[i][0] (last name) +  list[i][1] (first name) in a full list of names
    """
    holder_ls = []
    names_ls = []
    
    #appends to a holder list the last name and first name in of each student that attended
    for i in range(len(user_list)):
        holder_ls.append(user_list[i][0])
        holder_ls.append(user_list[i][1])
    
    #joins together the names of the attended students (lastname, firstname) and adds the new element to a list
    for i in range(0, len(holder_ls), 2):
        names_ls.append(holder_ls[i] + "," + holder_ls[i + 1])
    
    return names_ls

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class    
    
    # load class roster here into a list
    classRoster = fill_roster()

    #figure out which attendance data file to load here
    
    #load data
    attendData = fill_attendance_data()
    
    #use different tests 
    # make sure roster was filled 
    #printList(classRoster)
    # make sure attendance data was loaded
    #printList(attendData)
    
    #list all those missing
    print("****** Students missing in class *************")    
    printList(list_students_not_in_class(classRoster, attendData))
    #list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))  
    #display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))  
    #display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    #display first student to enter class
    print("******* Get 1st student to enter class ****************")    
    print(get_first_student_to_enter(attendData))
    
''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''
