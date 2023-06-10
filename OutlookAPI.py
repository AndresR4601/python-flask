from flask import Flask, jsonify, request
from datetime import datetime, timedelta
#from dotenv import load_dotenv
import requests, os

#load_dotenv("tokens.env")

app = Flask(__name__)

# Header content types
CONTENT_TYPE = 'application/json'
# Header access tokens
#API_OUT_KEY = os.environ.get("API_OUT_KEY")


API_OUT_KEY = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IldhMEp0TGJHd3VTUHY3d3p6aVVCbEVxQXBtX1ZaSWFTYm43bFNpUU9OMmsiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9jNjVhM2VhNi0wZjdjLTQwMGItODkzNC01YTZkYzE3MDU2NDUvIiwiaWF0IjoxNjg2MDAxMjE2LCJuYmYiOjE2ODYwMDEyMTYsImV4cCI6MTY4NjA4NzkxNiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhUQUFBQTNiV1JjRk9CZzkyRzdWYlRsamRIVXEwOUw2eVYwQnJ2bFhIRi9BTjlsWi81enhtd0QrU3cwbFRwdEJ0ak1HNjYiLCJhcHBfZGlzcGxheW5hbWUiOiJHcmFwaCBFeHBsb3JlciIsImFwcGlkIjoiZGU4YmM4YjUtZDlmOS00OGIxLWE4YWQtYjc0OGRhNzI1MDY0IiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJSYW3DrXJleiBGZXJuw6FuZGV6IiwiZ2l2ZW5fbmFtZSI6IkFuZHLDqXMgQWxlamFuZHJvIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTMxLjE3OC4xMDIuMjAwIiwibmFtZSI6IkFuZHLDqXMgQWxlamFuZHJvIFJhbcOtcmV6IEZlcm7DoW5kZXoiLCJvaWQiOiI3MDRhYWM4YS0zMjljLTRiNjgtOGU1My04MjEzNGI1N2UwYzIiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTcwODUzNzc2OC01NzM3MzU1NDYtNzI1MzQ1NTQzLTEzMTg0ODciLCJwbGF0ZiI6IjUiLCJwdWlkIjoiMTAwMzIwMDA5ODU4MDdBQiIsInJoIjoiMC5BVmNBcGo1YXhud1BDMENKTkZwdHdYQldSUU1BQUFBQUFBQUF3QUFBQUFBQUFBQlhBT1kuIiwic2NwIjoiQWNjZXNzUmV2aWV3LlJlYWQuQWxsIEFjY2Vzc1Jldmlldy5SZWFkV3JpdGUuQWxsIEFjY2Vzc1Jldmlldy5SZWFkV3JpdGUuTWVtYmVyc2hpcCBBZG1pbmlzdHJhdGl2ZVVuaXQuUmVhZC5BbGwgQWRtaW5pc3RyYXRpdmVVbml0LlJlYWRXcml0ZS5BbGwgQWdyZWVtZW50LlJlYWQuQWxsIEFncmVlbWVudC5SZWFkV3JpdGUuQWxsIEFncmVlbWVudEFjY2VwdGFuY2UuUmVhZCBBZ3JlZW1lbnRBY2NlcHRhbmNlLlJlYWQuQWxsIEFuYWx5dGljcy5SZWFkIEFwcENhdGFsb2cuUmVhZFdyaXRlLkFsbCBBcHByb3ZhbFJlcXVlc3QuUmVhZC5BZG1pbkNvbnNlbnRSZXF1ZXN0IEFwcHJvdmFsUmVxdWVzdC5SZWFkLkN1c3RvbWVyTG9ja2JveCBBcHByb3ZhbFJlcXVlc3QuUmVhZC5FbnRpdGxlbWVudE1hbmFnZW1lbnQgQXBwcm92YWxSZXF1ZXN0LlJlYWQuUHJpdmlsaWdlZEFjY2VzcyBBcHByb3ZhbFJlcXVlc3QuUmVhZFdyaXRlLkFkbWluQ29uc2VudFJlcXVlc3QgQXBwcm92YWxSZXF1ZXN0LlJlYWRXcml0ZS5DdXN0b21lckxvY2tib3ggQXBwcm92YWxSZXF1ZXN0LlJlYWRXcml0ZS5FbnRpdGxlbWVudE1hbmFnZW1lbnQgQXBwcm92YWxSZXF1ZXN0LlJlYWRXcml0ZS5Qcml2aWxpZ2VkQWNjZXNzIEJpdGxvY2tlcktleS5SZWFkLkFsbCBCaXRsb2NrZXJLZXkuUmVhZEJhc2ljLkFsbCBDYWxlbmRhcnMuUmVhZFdyaXRlIENvbnRhY3RzLlJlYWRXcml0ZSBEaXJlY3RvcnkuUmVhZC5BbGwgRmlsZXMuUmVhZFdyaXRlLkFsbCBNYWlsLlJlYWRXcml0ZSBOb3Rlcy5SZWFkV3JpdGUuQWxsIG9wZW5pZCBQZW9wbGUuUmVhZCBwcm9maWxlIFJlcG9ydHMuUmVhZC5BbGwgU2l0ZXMuRnVsbENvbnRyb2wuQWxsIFNpdGVzLk1hbmFnZS5BbGwgU2l0ZXMuUmVhZC5BbGwgU2l0ZXMuUmVhZFdyaXRlLkFsbCBUYXNrcy5SZWFkV3JpdGUgVGVhbS5SZWFkQmFzaWMuQWxsIFRlYW1NZW1iZXIuUmVhZC5BbGwgVGVhbXNBcHAuUmVhZCBUZWFtU2V0dGluZ3MuUmVhZC5BbGwgVGVhbVNldHRpbmdzLlJlYWRXcml0ZS5BbGwgVXNlci5SZWFkIFVzZXIuUmVhZC5BbGwgVXNlci5SZWFkQmFzaWMuQWxsIFVzZXIuUmVhZFdyaXRlIFVzZXIuUmVhZFdyaXRlLkFsbCBlbWFpbCIsInN1YiI6ImRRWXB5OXFWTW1zcjROcENQTXJhLThiWjdZa3JwTmpYOVFZVGVsZnpRS3MiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiTkEiLCJ0aWQiOiJjNjVhM2VhNi0wZjdjLTQwMGItODkzNC01YTZkYzE3MDU2NDUiLCJ1bmlxdWVfbmFtZSI6IkEwMDgzMTMxNkB0ZWMubXgiLCJ1cG4iOiJBMDA4MzEzMTZAdGVjLm14IiwidXRpIjoiREpSNlJfZE1fa2FpYUF5OUltb0hBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoiZmEwbUFTT043R28tWnFHc0ZxNENMRzQ0VWNpaTJkZGwzNW5CQTNKbllfTSJ9LCJ4bXNfdGNkdCI6MTM2MTk3ODU4NX0.rHc-sFubd4eRC7OAsPdZ_EGQS62GeNJ_deO_7zCGEg2OsGP1EAKgwP15al9eKnWdx7useA-tEHxGK90-86n8wG-o2v0dOOAibEVdiqvhj21QSpA-n9r_6udMxzD8T0hEGIxaGRo5v7Z_leiBSRuTteZbqU9agSPeWt0-oksdaCmNM59WtYxuvBZGNibZ9GSLPs7SlkB93LZbRcYn56NFNrgYZ7eZkHgC3ssPP1MD8ijOMp5sNG-UVJPUc5bWTebN9BURTI5imwFyzqX4I4Fzi9bImwx-ekn2u0mDajArVy7ycwbTzSkSg86Lk1aYX86yO9FCncRQKzkl-loV6NedLg"

"""
#prueba funcion
def setOutKey(key):
    global API_OUT_KEY
    API_OUT_KEY = key
"""


# Links para hacer los API calls
API_OUT_POSTMEETING = 'https://graph.microsoft.com/v1.0/me/events'
API_OUT_FINDMEETING = 'https://graph.microsoft.com/v1.0/me/findMeetingTimes'
API_OUT_ALLEVENTS = 'https://graph.microsoft.com/v1.0/me/events?$select=subject,body,bodyPreview,organizer,attendees,start,end,location'
API_OUT_GROUPS = 'https://graph.microsoft.com/v1.0/me/memberOf'
API_OUT_FINDTIME = 'https://graph.microsoft.com/v1.0/me/findMeetingTimes'

'''
{
    "attendees":[{"emailAddress": {"address": "A00831316@tec.mx"}},{"emailAddress": {"address": "A01411625@tec.mx"}}],
    "startDateTime": "2023-05-24T09:00:00",
    "finishDateTime": "2023-05-26T09:00:00",
    "duration": "PT1H"
}
'''
def OutlookFindMeetingTime():
    # Defino Header específico para hacer el call
    headers = {'Authorization': f'Bearer {API_OUT_KEY}', 'Content-Type': CONTENT_TYPE}

    addresses = request.json.get('attendees')
    start = request.json.get('startDateTime')
    finish = request.json.get('finishDateTime')
    duration = request.json.get('duration')

    data = {
        "attendees": addresses,
        "timeConstraint": {
            "timeslots": [
                {"start": {"dateTime": start, "timeZone": "UTC"},
                 "end": {"dateTime": finish, "timeZone": "UTC"}}
            ]
        },
        "meetingDuration": duration,
        "returnSuggestionReasons": "True"
    }

    # Hace el POST y verifica si se hace la llamada correctamente
    response = requests.post(API_OUT_FINDTIME, headers=headers, json=data)
    if response.status_code == 201:
        json_response = response.json()
        return json_response
    else:
        json_response = response.json()
        return json_response


# Método GET
# Trae todos los events que se tengan agendados en Outlook
def OutlookAllEvents():
    # Defino Header específico para hacer el call
    headers = {'Authorization': f'Bearer {API_OUT_KEY}', 'Content-Type': CONTENT_TYPE}
    response = requests.get(API_OUT_ALLEVENTS, headers=headers)

    # Verifica si el call devuelve un error
    if response.status_code == 200:
        json_response = response.json()
        subjects = []
        # Itero sobre el json de respuesta para extraer el subject de cada meeting
        for item in json_response['value']:
            subject = item['subject']
            start = item['start']
            end = item['end']
            id = item['id']

            attendees = []
            for i in item['attendees']:
                attendees.append(i['emailAddress']['name'])

            subjects.append({
                "subject": subject,
                "attendees": attendees,
                "start": start,
                "end": end,
                "id": id
            })
        
        return subjects
    else:
        return 'Error: unable to retrieve data from external API ' + response.text

# Método GET
# Trae todos los events que se tengan agendados en Outlook de hoy a una semana
def OutlookWeekEvents():
    # Defino variables de tiempo actual y una semana depués 
    current_date = datetime.now()
    next_week = current_date + timedelta(weeks=1)

    # Defino Header específico para hacer el call
    headers = {'Authorization': f'Bearer {API_OUT_KEY}', 'Content-Type': CONTENT_TYPE}
    response = requests.get(f'https://graph.microsoft.com/v1.0/me/calendarview?startdatetime={current_date}Z&enddatetime={next_week}', headers=headers)

    # Verifica si el call devuelve un error
    if response.status_code == 200:
        json_response = response.json()
        subjects = []
        # Itero sobre el json de respuesta para extraer el subject de cada meeting
        for item in json_response['value']:
            subject = item['subject']
            start = item['start']
            end = item['end']
            web = item['webLink']
            id = item['id']

            attendees = []
            for i in item['attendees']:
                attendees.append(i['emailAddress']['name'])

            subjects.append({
                "subject": subject,
                "attendees": attendees,
                "start": start,
                "end": end,
                "web": web,
                "id": id
            })
        
        return subjects
    else:
        return 'Error: unable to retrieve data from external API ' + response.text
    
# Método GET
# Trae todos los events que se tengan agendados en Outlook de hoy a un mes
def OutlookMonthEvents():
    # Defino variables de tiempo actual y una semana depués 
    current_date = datetime.now()
    next_month = current_date + timedelta(days=30)

    # Defino Header específico para hacer el call
    headers = {'Authorization': f'Bearer {API_OUT_KEY}', 'Content-Type': CONTENT_TYPE}
    response = requests.get(f'https://graph.microsoft.com/v1.0/me/calendarview?startdatetime={current_date}Z&enddatetime={next_month}', headers=headers)

    # Verifica si el call devuelve un error
    if response.status_code == 200:
        json_response = response.json()
        subjects = []
        # Itero sobre el json de respuesta para extraer el subject de cada meeting
        for item in json_response['value']:
            subject = item['subject']
            start = item['start']
            end = item['end']
            web = item['webLink']
            id = item['id']

            attendees = []
            for i in item['attendees']:
                attendees.append(i['emailAddress']['name'])

            subjects.append({
                "subject": subject,
                "attendees": attendees,
                "start": start,
                "end": end,
                "web": web,
                "id": id
            })
        
        return subjects
    else:
        return 'Error: unable to retrieve data from external API ' + response.text
    
# Método Post
# Crea un Meeting con el subject y duración determinado
# JSON entrada:
#{
#    "subject": "Listo",
#    "dateStart": "2023-05-02T00:10:40.099Z",
#    "dateEnd": "2023-05-03T00:10:50.099Z"
#}
def OutlookScheduleMeeting():
    # Defino Header específico para hacer el call
    headers = {'Authorization': f'Bearer {API_OUT_KEY}', 'Content-Type': CONTENT_TYPE}

    # Extraigo la información del JSON de entrada
    subject = request.json.get('subject')
    dateStart = request.json.get('dateStart')
    dateEnd = request.json.get('dateEnd')

    # Construyo el cuerpo del JSON para mandar en el POST
    data = {
        "subject": subject,
        "start": {
            "dateTime": dateStart,
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": dateEnd,
            "timeZone": "UTC"
        }
    }

    # Hace el POST y verifica si se crea correctamente
    response = requests.post(API_OUT_POSTMEETING, headers=headers, json=data)
    if response.status_code == 201:
        data = response.json()
        return {'message': 'Event created successfully.',
                'url': data['webLink']}
    else:
        response_data = {'message': 'Event failed to be created.'}
        return response_data

def OutlookGroups():
    # Defino Header específico para hacer el call
    headers = {'Authorization': f'Bearer {API_OUT_KEY}', 'Content-Type': CONTENT_TYPE}
    response = requests.get(API_OUT_GROUPS, headers=headers)

    name = []
    json_response = response.json()

    if response.status_code == 200:
        for item in json_response['value']:
           name.append(item['displayName'])
        return name
    else:
        return 'Error: unable to retrieve data from external API ' + response.text
    
# Metodo Delete para borrar meeting
# Requiere JSON en formato:
#{
# "id":"sdfsfddsf"
# }
def OutlookDelete():
    # Defino Header específico para hacer el call
    headers = {'Authorization': f'Bearer {API_OUT_KEY}', 'Content-Type': CONTENT_TYPE}
    event_id = request.json.get('id')
    response = requests.delete(f'https://graph.microsoft.com/v1.0/me/events/{event_id}', headers=headers)

    if response.status_code == 204:
        return jsonify({'message': 'Event deleted successfully'})
    else:
        return jsonify({'message': 'Failed to delete event'})


    
