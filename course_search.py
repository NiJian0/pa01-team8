'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''
#Lu Lu likes this project

from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
enrolled (filter by enrollment)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
            
            
                 
#         course  -- filter by subject/coursenumber
        #title -- filter by phrase in the title
        elif command == 'title':
            option = input("enter the phrase that you want to search in the title")
            schedule = schedule.title(option)
        #description -- filter by phrase in the description
        elif command == 'description':
            option = input("enter the phrase that you want to search in the description")
            schedule = schedule.description(option)
#         Create your own filter (each team member creates their own)


        #instructor -- filter by instructor email or lastname
        elif command in ['i','instructor']:
            option = input("enter 'email' or 'lastname' to continue:")
            if option in ['e', 'email']:
                instructor = input("enter an instructor's email:")
                schedule = schedule.email([instructor])
                
            elif option in ['l', 'lastname']:
                instructor = input("enter an instructor's lastname:")
                schedule = schedule.lastname([instructor])
            else:
                print('command',command,'is not supported')
                continue
        #days -- filter by the days
        elif command in ['d', 'digit']:
            digit = input ("enter the the number that the code starts with")

            schedule = schedule.code_start_with_num(digit)
<<<<<<< HEAD
<<<<<<< HEAD
        #course -- filter by courses
        elif command in ['c','course']:
            subject = input('enter subject ')
            schedule = schedule.subject[subject]
        #title -- filter by phrases in title
        elif command in ['t','title']:
            title = input('enter phrase ')
            schedule = schedule.title(title)
        #description -- filter by phrase in description
        elif command in ['d','description']:
            desc = input('enter description ')
            schedule = schedule.description(desc)
        #limit -- filter by the limit of a section
        elif command in ['l','limit']:
            num = input('enter minimum limit for courses ')
            schedule = schedule.description(num)
=======
            
        elif command in ['e','enrolled']:
            val1 = int(input("enter a min range integer in range(5,1000):"))
            val2 = int(input("enter a max range integer in range(5,1000):"))   
            schedule = schedule.enrolled(range(val1,val2))
            
            
>>>>>>> b4357a7204f2eca0273dfb4155e7e432f1631828
=======
            
>>>>>>> parent of 3d7d1f6 (implemented a few missing items)
        
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)


def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
           course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()


