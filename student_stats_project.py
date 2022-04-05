from datetime import datetime
from jinja2 import Template
import numpy as np
import plotly.graph_objects as go
import requests

api_adress = "deleted"
api_source = "deleted"
method = "getDataPerWeek"
response = requests.post(api_adress + api_source + method, json={"studEmail": "deleted",
                                                                 "beginDate": "2021-12-15",
                                                                 "endDate": "2022-03-31",
                                                                 "timeRange": 1,
                                                                 "hideMerge": True,
                                                                 "token": "deleted"
                                                                 })
response = response.json()
project_id = 6663
commit_count = 0
week_begin = []
commit_current = []
for project in response['projects']:
    if project['id'] == project_id:
        commit_count = len(project['commits'])
        for commits_in_week in project['commits_stats']:
            week_begin.append(commits_in_week['beginDate'][4:10])
            commit_current.append(commits_in_week['commitCount'])
        break
git_bar = go.Figure([go.Bar(x=week_begin, y=commit_current)])
git_line = go.Figure([go.Line(x=week_begin, y=commit_current)])

api_source = "deleted"
response = requests.post(api_adress + api_source + method, json={"studEmail": "deleted",
                                                                 "beginDate": "2022-01-01",
                                                                 "endDate": "2022-03-31",
                                                                 "timeRange": 1,
                                                                 "token": "deleted"
                                                                 }
                         )
response = response.json()
message_count = len(response['messages'])
days = []
messages = []
message_count_current = 0
message_number = []
for day in response['stats']:
    days.append(day['beginDate'][4:10])
    messages.append(day['messageCount'])
    message_count_current += day['messageCount']
    message_number.append(message_count_current)
zulip_bar = go.Figure([go.Bar(x=days, y=messages)])
zulip_line = go.Figure([go.Line(x=days, y=message_number)])
streams = set()
for message in response['messages']:
    streams.add(message['name'])

api_source = "deleted"
method = "deleted"
response = requests.post(api_adress + api_source + method, json={"studEmail": "deleted",
                                                                 "beginDate": "2021-09-01",
                                                                 "endDate": "2022-03-31",
                                                                 "token": "deleted"
                                                                 })
response = response.json()
sessions_count = 0
date = 0
month = 0
year = 0
week_number = []
week_entrance = []
rooms = set()

for session in response:
    rooms.add(session['room'])
    datetime = datetime.strptime(session['date'], '%Y-%M-%d')
    sessions_count += 1
    if len(week_number) <= 0:
        week_entrance.append(sessions_count)
        week_number.append(datetime.date().isocalendar()[1])
    elif datetime.date().isocalendar()[1] != week_number[len(week_number) - 1]:
        week_number.append(datetime.date().isocalendar()[1])
        week_entrance.append(sessions_count)
    else:
        week_entrance[len(week_entrance)-1] += 1
jitsi_bar = go.Figure([go.Bar(x=week_number, y=week_entrance)])
jitsi_line = go.Figure([go.Line(x=week_number, y=week_entrance)])

api_adress = "deleted"
api_source = "deleted"
method = "70"
response = requests.get("deleted", headers={"x-disable-pagination": "true"})
response = response.json()
userstories_count = 0
for userstory in response:
    if userstory['epics']:
        for epic in userstory['epics']:
            if epic['subject'] == "deleted":
                userstories_count += 1
# print(len(userstory['tasks']))
response = requests.get("deleted", headers={"x-disable-pagination": "true"})
response = response.json()
task_created = []
week_created = []
task_count = 0
for task in response:
    if task['user_story_extra_info'] and task['user_story_extra_info']['epics']:
        for epic in task['user_story_extra_info']['epics']:
            if epic['subject'] == "deleted":
                datetime = datetime.strptime(task['created_date'][0:10], '%Y-%M-%d')
                task_count += 1

                if len(week_created) <= 0:
                    week_created.append(datetime.date().isocalendar()[1])
                    task_created.append(task_count)
                elif datetime.date().isocalendar()[1] != week_created[len(week_created) - 1]:
                    week_created.append(datetime.date().isocalendar()[1])
                    task_created.append(task_count)
                else:
                    task_created[len(task_created)-1] += 1

taiga_line = go.Figure([go.Line(x=week_created, y=task_created)])

html = open('/home/prsem/folder/folder/template.html').read()
template = Template(html)
my_date = datetime.now()

with open('/var/www/html/folder/folder/result.html', 'w+') as fh:
    fh.write(template.render(name="deleted", group="deleted", date_time=datetime.today(),
                             zulip="Zulip", zulip_count=message_count, zulip_bar=zulip_bar.to_html(),
                             zulip_line=zulip_line.to_html(),
                             zulip_streams=streams, jitsi="Jitsi",
                             jitsi_count=sessions_count, jitsi_bar=jitsi_bar.to_html(),
                             jitsi_line=jitsi_line.to_html(),
                             jitsi_rooms=rooms, taiga="Taiga", taiga_userstory=userstories_count,
                             taiga_tasks_count=task_count,
                             taiga_line=taiga_line.to_html(),
                             gitlab="GitLab", git_commits_count=commit_count, git_bar=git_bar.to_html(),
                             git_line=git_bar.to_html()))
fh.close()
