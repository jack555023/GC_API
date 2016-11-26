from __future__ import print_function
import httplib2
import os
import datetime
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
try:
	import argparse
	flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
	flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'calendar-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
def insert_event(title,location,description,start_time,end_time,time_zone)
    event = {
        'summary': title,
        'location': location ,
        'description':description ,
        'start': {
          'dateTime':start_time ,
          'timeZone':time_zone,
        },
        'end': {
            'dateTime':end_time,
            'timeZone':time_zone,
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
        
          #{'email': 'sbrin@example.com'},
        ],
        'reminders': {
          'useDefault': False,
          # 'overrides': [
          #   {'method': 'email', 'minutes': 24 * 60},
          #   {'method': 'popup', 'minutes': 10},
          # ],
        },
     }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created')
def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
      calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
      orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


    title = 'IU 演唱會'
    location = '800 Howard St., San Francisco, CA 94103'
    description = 'A chance to hear more about Google\'s developer products.'
    start_time = '2016-11-28T09:00:00-07:00'
    end_time = '2016-11-28T17:00:00-07:00'
    time_zone = 'America/Los_Angeles'
    insert_event(title,location,description,start_time,end_time,time_zone)


if __name__ == '__main__':
    main()