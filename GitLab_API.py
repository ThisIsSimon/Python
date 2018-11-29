# A simple proof of concept script that accesses the GitLab API and returns the latest commit
# and checks if the commit has been made on the same day and within the last 5 minutes

import requests
import datetime as dt


def return_date_time(json_datetime):
    # Takes the given json string
    # and returns date and time in a dictionary
    date = json_datetime[0:10]
    time = json_datetime[11:19]
    return {
            'date': date,
            'time': time
           }


def is_recent(datetime_parameter):
    # Determine if the committed time is within the last five minutes
    time_minus_five = dt.datetime.now() - dt.timedelta(minutes=5)

    if (
        str(dt.datetime.now().date()) == datetime_parameter['date'] and
        time_minus_five.time().isoformat('seconds') < datetime_parameter['time'] < dt.datetime.now().time().isoformat('seconds')
       ):
        print('date matches and time is within the last five minutes - do something')
    else:
        print('do not do anything because false')


response = requests.get('https://gitlab.example.com/api/v4/projects?private_token=##############')
if response.status_code == requests.codes.ok:
    data = response.json()
    committed_date = data[0]['committed_date']
    git_datetime = return_date_time(committed_date)
else:
    print(response.raise_for_status())

is_recent(git_datetime)
