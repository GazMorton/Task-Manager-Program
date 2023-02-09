# finalCapstone
Project name:
Task Manager

Project Description:
This project is a task manager system designed to assist users in performing various operations such as adding a new user, adding a new task, reassigning tasks to different users and viewing statistics in the form of reports

Installation:
For this project to work locally you must have the python extension downloaded and python installed on your mac/windows/operating system
You must import datetime module and also define the colour variables at the beginning of the project for the colours to appear in the program
Please ensure that you have the supplementary txt files in the same folder as the python py file, if the program does not run it may be because the file paths of the txt files are incorrect

Project Walkthrough:
The project works by reading tasks from the tasks.txt file and also stores registered users in the users.txt file.
When you run the project you will be faced with a main menu containing options such as register a user, view all tasks etc. etc
if you are the admin user, you select register a user you will be prompted for a new username and password, the program will check to ensure there is no duplicate usernames in the user.txt file, it will also confirm the chosen password
if the user selects view my tasks they will be shown a list of all tasks assigned to them and also have the option to edit the task or mark it as complete
if the user selects add task they will be prompted to enter all the data for this task
if the user select view all they will be shown a list of every task in the system
if the user is an admin they will be able to generate reports which will show which tasks are overdue and various metrics such as count of uncomplete tasks etc. This option will write the reports to new txt files called tasks_overview.txt and user_overview.txt
Please see screenshots below to see some of the program in action:

![0B1A52E5-0AF1-4575-85D4-F85752916A4D](https://user-images.githubusercontent.com/124776767/217526591-ed5222c7-20ca-4327-b37a-2b7a9bc0e2eb.jpeg)
![90E1FAE3-6405-4FBB-ACAD-1ADA256C511A](https://user-images.githubusercontent.com/124776767/217528070-5efd3f09-e777-4dfb-b257-1f5bf2f8a520.jpeg)
![F4D932AF-8F5E-46B3-B386-CBEAA94A1F99](https://user-images.githubusercontent.com/124776767/217528089-4ba9102b-7a21-4d37-8b53-4f934effeede.jpeg)
![56AABA71-8B44-4915-9350-41083F6808C7](https://user-images.githubusercontent.com/124776767/217528100-7433d0a9-0e75-4927-a595-7d8a7042f48e.jpeg)

Credits:
Gareth Morton

