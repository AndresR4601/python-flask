from flask import Flask, render_template
from flask_cors import CORS
import aiohttp
import asyncio
from GithubAPI import GithubRepos, GithubIssues, GithubPulls
from OutlookAPI import OutlookWeekEvents, OutlookMonthEvents, OutlookScheduleMeeting, OutlookAllEvents, OutlookGroups, OutlookDelete, OutlookFindMeetingTime
from AzureAPI import AzureCreateItem, AzureOneItem, AzureWorkItems
#from CVAPI import getCV, getGPTtext, upload
#from dbApi import obtener_usuarios, guardar_usuario, check_if_user_is_hr, guardar_tokens, obtener_tokens

app = Flask(__name__, static_folder='dist', static_url_path='')
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    print('Hello World')
    return app.send_static_file('index.html')

"""
@app.route('/upload/<user_id>', methods=['POST'])
def uploadCV(user_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(upload(user_id))
    return result

@app.route('/CV/<user_id>', methods=['GET'])
def getCVimg(user_id):
    return getCV(user_id)

@app.route('/GPTtext/<user_id>', methods=['GET'])
def getSummary(user_id):
    return getGPTtext(user_id)
"""

@app.route('/Github/Repositories')        
def getGithubRepos():
    return GithubRepos()


@app.route('/Github/Issues')       
def getGithubIssues():
    return GithubIssues()

@app.route('/Github/Pulls')   
def getGithubPulls():
    return GithubPulls()

@app.route('/Outlook/Groups')
def getOutlookGroups():
    return OutlookGroups()

@app.route('/Outlook/FindTime', methods=['POST'])
def getOutlookFreeTime():
    return OutlookFindMeetingTime()

@app.route('/Outlook/deleteMeeting', methods=['DELETE'])
def deleteMeeting():
    return OutlookDelete()

#
@app.route('/Outlook/WeekEvents')
def getWeekEvents():
    return OutlookWeekEvents()  

@app.route('/Outlook/MonthEvents')
def getMonthEvents():
    return OutlookMonthEvents()

@app.route('/Outlook/AllEvents')
def getAllEvents():
    return OutlookAllEvents()

@app.route('/Outlook/ScheduleMeeting', methods=['POST'])
def postScheduleMeeting():
    return OutlookScheduleMeeting()

@app.route('/Azure/AllWI')
def getAllWI():
    return AzureWorkItems()

@app.route('/Azure/WI/<id>')
def getWI(id):
    return AzureOneItem(id)

@app.route('/Azure/CreateItem', methods=['POST'])
def postCreateItem():
    return AzureCreateItem()

"""

@app.route('/api/DatabaseGET')
def obtenerU():
    return obtener_usuarios()

@app.route('/api/DatabasePOST', methods=['POST'])
def mandarU():
    return guardar_usuario()

@app.route('/api/CheckHR', methods=['GET'])
def checkHR():
    return check_if_user_is_hr()

@app.route('/api/DatabasePOSTTokens', methods=['POST'])
def postoken():
    return guardar_tokens()

@app.route('/api/DatabaseGETTokens/<sub>')
def obtokens(sub):
    return obtener_tokens(sub)
"""
