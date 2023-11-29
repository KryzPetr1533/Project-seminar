# Project-seminar
This program is created solely for academic purposes.

##### Description
The program retrieves statistics from corporate services, specifically from Zulip, Jitsi, Taiga, and GitLab. Based on the data, it generates charts for absolute values and their changes. The program outputs the following data:

1. Numbers of:
  - commits made by the student in the Git project repository
  - attended sessions in Jitsi across all disciplines
  - messages in Zulip
2. Bar chart displaying:
  - the number of student commits in the Git project repository per week
  - message count per day
  - number of attended sessions per week
3. Line chart illustrating:
  - change in the total number of messages
  - change in the total number of attended sessions per week
  - number of student commits in the Git project repository per week
4. List of:
  - rooms visited by the student
  - channels where the student posted messages
5. Total number of:
  - user stories created by the student
  - tasks in user stories within an epic
6. Linear graph depicting the growth of task numbers in the project in Taiga on a weekly basis.

The program was written in Python and utilizes the following libraries: datetime, jinja2, numpy, plotly, requests.

