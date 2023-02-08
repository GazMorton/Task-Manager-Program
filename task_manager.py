"""Program to create a task manager to help a company assign tasks, register users, view all tasks,
view the tasks of a specific user and display statistics if user is the admin"""

# PLEASE OPEN MY OVERVIEW FILES IN VS CODE, FOR SOME REASON THE NUMBERS ARENT LINED UP WHEN I OPEN THE FILES IN DROPBOX BUT THEY WERE ALIGNED ON MY SIDE

#=====importing libraries=====================================================
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
CBEIGE2  = '\33[96m'

from datetime import datetime

#====Functions===================================================================

def reg_user():
        while True:
            if user == 'admin':
                print(f'\n════════════════ {CYAN}Register A New User{END} ════════════════\n')
                user_file = open('T26 Capstone 3/user.txt', 'a')
                new_user = input('Please enter a new username: \t\t')
                new_password = input('Please enter a password: \t\t')
                conf_password = input('Please re-enter your chosen password: \t')
                if new_user in user_list:
                    print(f'\n{RED}This user already exists, please enter a different username{END}')
                    continue
                elif new_user not in user_list and new_password == conf_password:
                    user_file.write(f'\n{new_user}, {new_password}')
                    break
                else:
                    print(f'\n{RED}Your passwords do not match, please try again{END}')
                    continue
            else:
                print(f'\n{RED}You are not authorised to register new users, please select a different option{END}\n')
            continue   
        user_file.close()

def view_all():
        print(f'\n═══════════════════ {DARKCYAN}{BOLD}View All Tasks{END} ══════════════════\n')
        tasks_read = open('T26 Capstone 3/tasks.txt', 'r')
        data = tasks_read.readlines()
        # loop through all split lines and output the correct index for each data column
        for pos, line in enumerate(data,1):
            split_data = line.split(', ')
            output = f'∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞[{DARKCYAN}{BOLD}{pos}{END}]∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞\n'
            output += '\n'
            output += f'Assigned To: \t\t{split_data[0]}\n'
            output += f'Task Name: \t\t{split_data[1]}\n'
            output += f'Task Description: \t{split_data[2]}\n'
            output += f'Assigned Date: \t\t{split_data[3]}\n'
            output += f'Due Date: \t\t{split_data[4]}\n'
            output += f'Is Completed: \t\t{split_data[5]}\n'
    
            print(output)
        tasks_read.close()
    

def add_task():
        print(f'\n═══════════════════ {BLUE}{BOLD}Add A New Task{END} ══════════════════\n')
        task_user = input('Please enter the username of the person the task is assigned to:\t\t')
        task_title = input('Please enter the task title:\t\t\t\t\t\t\t')
        task_desc = input('Please enter a task description:\t\t\t\t\t\t')
        curr_date = input('Please enter todays date as the date assigned in the format \'XX XXX XXXX\':\t')
        due_date = input('Please enter a due date for the task in the format \'XX XXX XXXX\':\t\t')

        tasks_file = open('T26 Capstone 3/tasks.txt', 'a+')
        tasks_file.write(f'{task_user}, {task_title}, {task_desc}, {curr_date}, {due_date}, No')
        tasks_file.close()

def view_mine():
        print(f'\n══════════════════ {PURPLE}{BOLD} View My Tasks{END} ═══════════════════\n')
        user_tasks_read = open('T26 Capstone 3/tasks.txt', 'r')
        data = user_tasks_read.readlines()
        # repeat method used for all tasks but ensure the first index matches the user currently logged in
        for pos, line in enumerate(data,1):
            split_data = line.split(', ')
            if split_data[0] == user:
                output = f'∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞[{PURPLE}{BOLD}{pos}{END}]∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞\n'
                output += '\n'
                output += f'Assigned To: \t\t{split_data[0]}\n'
                output += f'Task Name: \t\t{split_data[1]}\n'
                output += f'Task Description: \t{split_data[2]}\n'
                output += f'Assigned Date: \t\t{split_data[3]}\n'
                output += f'Due Date: \t\t{split_data[4]}\n'
                output += f'Is Completed: \t\t{split_data[5]}\n'
                print(output)

        while True:
            task_num = int(input('Please enter a specific task number to edit the task or enter -1 to return to main menu: '))-1
            if task_num == -2:
                return         
            elif task_num < 0 or task_num > len(data):
                print('Please select a valid task number.')
                continue
            
            edit_data = data[task_num] 
            split_edit_data = edit_data.split(', ')
            break
                
        while True:
            output = f'\n∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞ {PURPLE}{BOLD}Select an option{END} ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞\n'
            output += f'\n🔸 {BOLD}1{END} - Edit the task \n'
            output += f'🔸 {BOLD}2{END} - Mark as completed \n'
            choice = int(input(output))
            
            if choice <= 0 or choice >= 3:
                print('you have selected an invalid option')
                continue

            if split_edit_data[5].strip('\n') == 'Yes':
                print(f'\n{RED}This task is completed and can no longer be edited{END}')
            elif choice == 1:
                while True:
                    output = f'\n{PURPLE}{BOLD} Select an option or enter -1 to return to main menu{END}\n'
                    output += f'\n🔸 {BOLD}1{END} - Edit username \n'
                    output += f'🔸 {BOLD}2{END} - Edit due date \n'
                    output += f'🔸 {BOLD}3{END} - Edit both \n'
                    output += f'\n∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞\n'

                    edit_choice = int(input(output))

                    if edit_choice == -1:
                        break
                    elif edit_choice == 1:
                        split_data = edit_data.split(', ')
                        split_data[0] = input('Please enter a new username for this task: ')
                        new_data = ', '.join(split_data)
                        data[task_num] = new_data
                    tasks_write = open('T26 Capstone 3/tasks.txt', 'w')
                    for line in data:
                        tasks_write.write(line)
                        

                    if edit_choice == 2:
                        split_data = edit_data.split(', ')
                        split_data[4] = input('Please enter a new due date for this task: ')
                        new_data = ', '.join(split_data)
                        data[task_num] = new_data
                    tasks_write = open('T26 Capstone 3/tasks.txt', 'w')
                    for line in data:
                        tasks_write.write(line)
                        

                    if edit_choice == 3:
                        split_data = edit_data.split(', ')
                        split_data[0] = input('Please enter a new username for this task: ')
                        split_data[4] = input('Please enter a new due date for this task: ')
                        new_data = ', '.join(split_data)
                        data[task_num] = new_data
                    tasks_write = open('T26 Capstone 3/tasks.txt', 'w')
                    for line in data:
                        tasks_write.write(line)
                    break

                    
            elif choice == 2:
                split_data = edit_data.split(', ')
                split_data[-1] = 'Yes\n'
                new_data = ', '.join(split_data)
                data[task_num] = new_data
            tasks_write = open('T26 Capstone 3/tasks.txt', 'w')
            for line in data:
                tasks_write.write(line)
                
                
            break

        user_tasks_read.close()
        tasks_write.close()
        
def generate_reports():
# writing the task overview file
        user_tasks_read = open('T26 Capstone 3/tasks.txt', 'r')
        data = user_tasks_read.readlines()
        task_overview = open('T26 Capstone 3/task_overview.txt', 'w')       
        for pos, line in enumerate(data,1): 
                num_tasks = pos
        count_complete = 0
        count_uncomplete = 0      
        overdue = 0
# use for loop to count the jobs that have been completed
        for line in data:
            if line.split(', ')[5].strip('\n') == 'Yes':
                    count_complete += 1
            else:
                    count_uncomplete += 1

            due_date = line.split(', ')[4] # the due date in the format "XX XXX XXXX"  
            due_date_datetime = datetime.strptime(due_date, "%d %b %Y") # convert the string to a datetime object
            if line.split(', ')[5].strip('\n') == 'No' and datetime.now() > due_date_datetime:
                overdue += 1
            else:
                overdue

        task_overview.write(f"""════════════════════ TASK OVERVIEW REPORT ═════════════════════
Number of Tasks:\t\t\t{num_tasks}
Number of Complete Tasks:\t{count_complete}
Number of Uncomplete Tasks:\t{count_uncomplete}
Number of Overdue Tasks:\t{overdue}
% of Uncomplete Tasks:\t\t{round(count_uncomplete/num_tasks*100,1)}
% of Overdue Tasks:\t\t\t{round(overdue/count_uncomplete*100,1)}""")

# writing the user overview file
# many similar steps are repeated from the tasks overview, however there's an added layer of complexity because we need to reference both the user and tasks file here
# I had to append all the output to a list in order to write it to the txt file
        user_file_read = open('T26 Capstone 3/user.txt', 'r')
        user_data = user_file_read.readlines()
        user_overview = open('T26 Capstone 3/user_overview.txt', 'w')
        my_list = []
        for pos, line in enumerate(user_data,1): 
                num_users = pos
                split_data = line.split(', ')
                output = f'∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞ {split_data[0]} ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞\n'
                user_task_count = 0
                user_count_comp = 0
                user_count_todo = 0
                user_count_overdue = 0
                for pos, line in enumerate(data,1): 
                    due_date = line.split(', ')[4] # the due date in the format "XX XXX XXXX"  
                    due_date_datetime = datetime.strptime(due_date, "%d %b %Y") 
                    if line.split(', ')[0] == split_data[0]:
                        user_task_count += 1
                        if line.split(', ')[5].strip('\n') == 'Yes':
                            user_count_comp +=1
                        else:
                            user_count_todo += 1
                        if line.split(', ')[5].strip('\n') == 'No' and datetime.now() > due_date_datetime:
                            user_count_overdue += 1
                        
                output += f'Total Number of Tasks:\t\t\t{str(user_task_count)}\n'
                output += f'% of Total Number of Tasks:\t\t{round(user_task_count / num_tasks * 100,1)}\n'
                try:
                    output += f'% of Tasks Completed:\t\t\t{round(user_count_comp / user_task_count * 100,1)}\n'
                except ZeroDivisionError:
                    output += f'% of Tasks Completed:\t\t\t0.0\n'
                try:
                    output += f'% of Tasks Uncompleted:\t\t\t{round(user_count_todo / user_task_count * 100,1)}\n'
                except ZeroDivisionError:
                    output += f'% of Tasks Uncompleted:\t\t\t0.0\n'
                try:
                    output += f'% of Tasks Overdue:\t\t\t\t{round(user_count_overdue / user_count_todo * 100,1)}\n'
                except ZeroDivisionError:
                    output += f'% of Tasks Overdue:\t\t\t\t0.0\n'
                
                my_list.append(output)          
        
                
        user_overview.write(f"""════════════════════ USER OVERVIEW REPORT ═════════════════════
Number of Users:\t\t\t\t{num_users}
Number of Tasks:\t\t\t\t{num_tasks}\n""")
        user_overview.writelines(my_list)

        user_tasks_read.close()
        task_overview.close()
        user_overview.close()
        user_file_read.close()


        
#====Login Section=======================================================

print(f"""           
                {RED}╔══════════════════╗{END}
                    {BOLD}TASK MANAGER 
                {RED}╚══════════════════╝{END}
      """)
print('')

print(f'══════════ 👋  {YELLOW}{BOLD}Welcome! Please log in!{END} 👋 ═══════════\n')
# Created a list for users and then added users and passwords to a dictionary 
user_list = []
pass_dict = {}

user_file = open('T26 Capstone 3/user.txt', 'r')
file_read = user_file.readlines()
# Loop through the user file, split, append the users to list, users will be keys and then passwords as the values
for line in file_read:
    temp = line.strip('\n')
    temp = temp.split(', ')
    user_list.append(temp[0])
    pass_dict[temp[0]]=temp[1]

"""verify inputs using the user list and passwords in the dictionary,
break the loop if both username and password are correct
"""
while True:
    user = input('Please enter your username:\t')
    password = input('Please enter your password:\t')
    
    if user in user_list and password != pass_dict[user]:
        print(f'\nHello {user}, please enter a valid username and password')
        continue 
    elif user not in user_list:
        print('\nPlease enter a valid username and password\n')
        continue
    elif password == pass_dict[user] and user in user_list:
        print(f'\nThank you. Hello {user}!\n')
        break
    
user_file.close()
        
# Give admin account additional options, else give standard options
while True:
    if user == 'admin':
        print(f'\n═════════════════ 🔴 {GREEN}Main Menu{END} 🔴 ═══════════════════\n')
        menu = input(f'''\nSelect one of the following options below:
🔸 {BOLD}r{END}  - Registering a user
🔸 {BOLD}a{END}  - Adding a task
🔸 {BOLD}va{END} - View all tasks
🔸 {BOLD}vm{END} - View my task
🔸 {BOLD}gr{END} - Generate reports
🔸 {BOLD}s{END}  - Display statistics
🔸 {BOLD}e{END}  - Exit

: ''').lower()

    else:
        print(f'\n═════════════════ 🔴 {GREEN}Main Menu{END} 🔴 ═══════════════════\n')
        menu = input(f'''\nSelect one of the following options below:
🔸 {BOLD}r{END}  - Registering a user
🔸 {BOLD}a{END}  - Adding a task
🔸 {BOLD}va{END} - View all tasks
🔸 {BOLD}vm{END} - View my task
🔸 {BOLD}e{END}  - Exit

: ''').lower()

# if user selects r and is logged in as admin, allow to add user if passwords match, else deny request
    if menu == 'r':
        if user == 'admin':
            reg_user()    
        else:
            print(f'\n{RED}You are not authorised to register new users, please select a different option{END}\n')
            continue
        
# ask for user inputs then write these to the tasks file using a+ access mode
    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()
# call the function to generate the reports and then print in the terminal using read and a for loop    
    elif menu == 's' and user == 'admin':
        generate_reports()
        task_overview = open('T26 Capstone 3/task_overview.txt','r')

        for line in task_overview:
            line = line.replace('\t',' ')
            print(line)
        print()
        user_overview = open('T26 Capstone 3/user_overview.txt','r')
        for line in user_overview:
            line = line.replace('\t',' ')
            print(line)
        
        task_overview.close()
        user_overview.close()
# if admin selects gr, write the reports to 2 txt files
    elif menu == 'gr' and user == 'admin':
        generate_reports()

    elif menu == 'e':
        print(f'\n═════════════════ 👋 {YELLOW}{BOLD}Goodbye!!!{END} 👋 ══════════════════\n')
        exit()

    else:
        print(f"\n{RED}You have made a wrong choice, Please Try again{END}\n")