#        /\          /\          /\          /\          /\          /\          /\          /\          /\          /\
#     /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\
#  /\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\
# //\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\
# \\//\/                                                                                                                \/\\//
#  \/                                                "In the Name of Allah"                                                \/
#  /\                                                                                                                      /\
# //\\                                              Python Automation Scrpits                                             //\\
# \\//                                                                                                                    \\//
#  \/                                                                                                                      \/
#  /\              Script ID: 002                                                                                          /\
# //\\           Script Name: Create Event in Calendar                                                                    //\\
# \\//           Description: This script creates scheduled and specified events in google calendar associating           \\//
#  \/                         a pdf attachment. The pdf file is automatically uploaded to google drive in order            \/
#  /\                         to attach with calendar event.                                                               /\
# //\\                                                                                                                    //\\
# \\//           Author Name: Abu Bakar Siddique Arman (#arman_bhaai)                                                     \\//
#  \/                  Email: arman.bhaai@gmail.com                                                                        \/
#  /\                 GitHub: github.com/arman-bhaai                                                                       /\
# //\\              Facebook: fb.me/arman.bhaai                                                                           //\\
# \\//               Youtube: tiny.cc/arman-bhaai-on-youtube                                                              \\//
#  \/                         bit.ly/arman-bhaai-on-youtube                                                                \/
#  /\                                                                                                                      /\
# //\\         Creation Date: 2020-08-30                                                                                  //\\
# \\//               Version: v1.0                                                                                        \\//
#  \/        Versioning Date: 2020-08-30                                                                                   \/
#  /\                                                                                                                      /\
# //\\               License: Custom License                                                                              //\\
# \\//                                                                                                                    \\//
#  \/           Dev Language: Python 3.8.5                                                                                 \/
#  /\                 Dev OS: Linux Mint 19.3 (tricia)                                                                     /\
# //\\                                                                                                                    //\\
# \\//           Source Code: www.github.com/arman-bhaai/python-automation-scripts/002_create_event_in_calendar.py        \\//
#  \/             Video Demo: ###                                                                                          \/
#  /\                                                                                                                      /\
# //\\/\                                                                                                                /\//\\
# \\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\//
#  \/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/
#     \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/
#        \/          \/          \/          \/          \/          \/          \/          \/          \/          \/

#       ,
#   /\^/`\
#  | \/   |                                         Custom License!!!
#  | |    |                                                                                                       jgs
#  \ \    /                                                                                                     _ _
#   '\\//'                      Copyright (c) 2020 Abu Bakar Siddique Arman (#arman_bhaai)                    _{ ' }_
#     ||                                                                                                     { `.!.` }
#     ||                                                                                                     ',_/Y\_,'
#     ||                 Only Muslim brothers and sisters may use this file/project/source-code.               {_,_}
#     ||          And bear in mind that this file/project/source-code may only be used in an islamically         |
#     ||             lawful (halaal) purpose/project. So, any kinds of islamically unlawful (haraam)             |
#     ||  ,            implementation/use of this file/project/source-code is strictly prohibited!               |
# |\  ||  |\                                                                                                     |
# | | ||  | |                For any further queries, contact me at --> arman.bhaai@gmail.com                  (\|  /)
# | | || / /                                                                                                    \| //
#  \ \||/ /                                                                                                      |//
#   `\\//`   \   \./    \\   \./    \\   \./    \\   \./    \\   \./    \\   \./    \\   \./    \\   \./    \ \\ |/ /
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



# scaffold code taken from --> https://developers.google.com/calendar/quickstart/python
# $ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib sh
from datetime import datetime, timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import json
import sh
import logging


# define switches
# python switch concept taken from --> https://jaxenter.com/implement-switch-case-statement-python-138315.html
def translate_remote_dir_id(dir_name):
    switcher_dict = {
        'Information Technology': '1vnRwu7vloNbgJM8GpuAH0xu0sBXT68w_',
        'Biography of Prophet (pbuh) (Madani Life)': '1tHb01wcg9XEIssNOnmziTVexdZceo4vy',
        'Fiqh of Muamalat': '1kzsxKmBTzW363ymOQwrNvV_SFowMSCUU',
        'Fiqh of Hajj': '1I0A7ygbhTx8_lSnEhbmrhzx7U_nyFcbA',
        'Fiqh of Zakaat': '1YEqJgXMuWuHfPqNS07rOF2SefBApFaEh',
        'Language of Quran': '1iaUamnXzXsw0yXU0Xgso2FXa00YNoW9q',
        'Introduction to Tawhid': '1dotmauzkVL3OwOfjp-9KX8cSUoYcUxig',
        'Basic Rules to Understand Quran': '1yxYJTWrjq6S8tWp-FYUS17_yt5noUgpz',
        'Biography of Prophet (pbuh) (Makki Life)': '1Ba1EbmCSwyEfBkichqZ1q9MlDTkk9WV7',
        'Fiqh of Siyam': '1h0koMVSTmqbIhTIfWHkDsT-NknFJ4CoW',
        'Fiqh of Purity and Salah': '1rPMPW0Y6yLBec34QQoOL3Bg8Vw2NP57t',
        'Basic Rules to Understand Hadith': '1wQXb3BS4QfwfCLbyuCOlIzvLU7mbDmeM',
        'Study Skills': '1m5faCA1pPHZT6l8BhtntaAXkfkHJ5OGL',
        'Introduction to Islamic Aqidah': '1JvZzQoPv7eaYz4UbnmbZWRq-DBtG4p2D',
    } 
    return switcher_dict.get(dir_name, 'Unknown Directory!')

def translate_course_name(course_name):
    switcher_dict = {
        'Information Technology': 'তথ্য প্রযুক্তি',
        'Biography of Prophet (pbuh) (Madani Life)': 'সীরাতে রাসূল (সাঃ) (মাক্কী যুগ)',
        'Fiqh of Muamalat': "ফিক্বহুল মু'আমালাত",
        'Fiqh of Hajj': 'ফিক্বহুল হাজ্জ',
        'Fiqh of Zakaat': 'ফিক্বহুয যাকাত',
        'Language of Quran': 'লুগাতুল কুরআন',
        'Introduction to Tawhid': 'তাওহীদ পরিচিতি',
        'Basic Rules to Understand Quran': 'কুরআন বোঝার মূলনীতি',
        'Biography of Prophet (pbuh) (Makki Life)': 'সীরাতে রাসূল (সাঃ) (মাদানী যুগ)',
        'Fiqh of Siyam': 'ফিক্বহুস সিয়াম',
        'Fiqh of Purity and Salah': 'ফিক্বহুত তাহারাত ওয়াস সালাত',
        'Basic Rules to Understand Hadith': 'হাদীস বোঝার মূলনীতি',
        'Study Skills': 'অধ্যয়ন দক্ষতা',
        'Introduction to Islamic Aqidah': 'ইসলামী আকীদার পরিচয়',
    } 
    return switcher_dict.get(course_name, 'Unknown Course!')

def translate_module_no(module_no):
    switcher_dict = {
        '01': 'মডিউলঃ ১',
        '02': 'মডিউলঃ ২',
        '03': 'মডিউলঃ ৩',
        '04': 'মডিউলঃ ৪',
        '05': 'মডিউলঃ ৫',
        '06': 'মডিউলঃ ৬',
        '07': 'মডিউলঃ ৭',
        '08': 'মডিউলঃ ৮',
        '09': 'মডিউলঃ ৯',
        '10': 'মডিউলঃ ১০',
        '11': 'মডিউলঃ ১১',
        '12': 'মডিউলঃ ১২',
        '13': 'মডিউলঃ ১৩',
        '14': 'মডিউলঃ ১৪',
        '15': 'মডিউলঃ ১৫',
        '16': 'মডিউলঃ ১৬',
        '17': 'মডিউলঃ ১৭',
        '18': 'মডিউলঃ ১৮',
        '19': 'মডিউলঃ ১৯',
        '20': 'মডিউলঃ ২০',
    } 
    return switcher_dict.get(module_no, 'Unknown Module!')

# !@UNUSED_FUNCTION
# get attachment metadata by file name and parent dir id
def get_attach_file_meta_by_name(attach_name, remote_parent_dir_id):
    file_obj = driveAPI.files().list(q=f"name = '{attach_name}' and parents in '{remote_parent_dir_id}'", fields='files(name, id, mimeType, webViewLink)').execute()
    # get name, id, mimeType, webViewLink of attachment file
    attach_file_meta = file_obj.get('files')[0]
    return attach_file_meta

# !@UNUSED_FUNCTION
# list all directiory ids from google drive 
def get_dirs_ids():
    dir_list = driveAPI.files().list(q="mimeType = 'application/vnd.google-apps.folder' and trashed=false", fields='files(id, name)').execute().get('files')
    for dir in dir_list:
        print(f"{dir['name']} --> {dir['id']}")
        

# create a custom logger instance
logger = logging.getLogger(__name__)
# logger level concept taken from --> https://www.toptal.com/python/in-depth-python-logging
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
log_format = logging.Formatter('%(levelname)s: >>> %(message)s')
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

# define global variables
# If modifying these scopes or want to change google account, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar', 
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive.file',]


#################### Define Primary (User Input) Variables #########################!PRIMVAR!
# define event info
course_name = 'Study Skills'
module_no = '01'
module_topic_str = 'আলোচ্য বিষয়ঃ'
# video url of the module lecture
module_vid_url = 'https://youtube.com'
# the date when the event is being created
evt_creation_stamp = '2020-08-29'
# a notification should appear before specified minutes of the event date
evt_reminder_min_before = 120
# define path to attachment local directory
raw_attach_dir = '/home/antidote/Desktop/taibahacadmy_raw'
# taibah academy directory path where final and processed pdfs and events info will reside
taibah_academy_dir = '/home/antidote/Taibah Academy'
# event recurrence rule
repeat_freq = 'MONTHLY'
# define the date until which the event should recur
event_recur_until_date = '20200913'
logger.info('defined primary variables')

###################### Define Secondary (Generated) Variables ############################!SECVAR!
# construct event title string (summary) with combination of course name and module number
evt_title_str = f'{translate_course_name(course_name)} - {translate_module_no(module_no)}'
# construct module number string from module number
module_no_str = f'Module - {module_no}'
# construct html link from module video url
# html link concept taken from --> https://webapps.stackexchange.com/a/28115
module_vid_url_html = f'<a href="{module_vid_url}"><b>Watch Video</b></a>'
# construct event description with combination of module topic string and html link of module video
evt_desc_str = module_topic_str + '\n\n' + module_vid_url_html
# construct attachment file name from module name
attach_name = f'{module_no_str}.pdf'
# get corresponding remote dir id by name with help of switch function
attach_remote_parent_id = translate_remote_dir_id(course_name)
# create datetime object for today
evt_creation_dt_obj = datetime.strptime(evt_creation_stamp, '%Y-%m-%d')
# event recurrence rule
# the day of the month when the events will occur
month_day = evt_creation_dt_obj.day
# rrule is for scheduled events
rrule = f'RRULE:FREQ={repeat_freq};UNTIL={event_recur_until_date};INTERVAL=1;BYMONTHDAY={month_day}'
logger.info('processed secondary variables')


###################################### Main ###################################!MAIN!
# perform oAuth Login
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    logger.info('token.pickle file exists')
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
        logger.info('credentials have been loaded from token.pickle file')
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    logger.info('no valid credentials have been found. please login')
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        logger.info('taken user information from credentials.json file')
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
        logger.info('credentials have been saved into token.pickle file')
logger.info('finished oAuth login')
# finished oAuth Login

# rename and move the file to taibah academy dir from raw dir
# sh globbing concept taken from --> https://stackoverflow.com/a/32923739
# rename the file
raw_pdf = sh.glob(f'{raw_attach_dir}/*.pdf')
processed_pdf = f'{raw_attach_dir}/{module_no_str}.pdf'
sh.mv(raw_pdf, processed_pdf)
logger.info(f'renamed {raw_pdf} to "{processed_pdf}"')
# check if the corresponding course dir is present inside taibah academy dir
if not os.path.exists(f'{taibah_academy_dir}/{course_name}'):
    # create a dir within taibah academy dir with corresponding course name
    sh.mkdir('-p', f'{taibah_academy_dir}/{course_name}')
    logger.info('the course name dir "{course_name}" doesn\' exist. so created a new dir named "{taibah_academy_dir}/{course_name}"')
# move the file to corresponding categorized dir
sh.mv(f'{raw_attach_dir}/{module_no_str}.pdf', f'{taibah_academy_dir}/{course_name}')
logger.info(f'moved the file "{processed_pdf}" to "{taibah_academy_dir}/{course_name}"')

# get API services for Google Drive and Google Calendar
driveAPI = build('drive', 'v3', credentials=creds)
calendarAPI = build('calendar', 'v3', credentials=creds)

# store attachment file metadata (id, name, webViewLink) from google drive
attach_file_meta = driveAPI.files().create(body={'name': attach_name, 'parents': [attach_remote_parent_id]}, media_body=MediaFileUpload(f'{taibah_academy_dir}/{course_name}/{attach_name}', resumable=True), fields='id, name, mimeType, webViewLink').execute()
logger.info(f'uploaded file "{taibah_academy_dir}/{course_name}/{attach_name}" to google drive inside corresponding parent dir')

# define event body
event = {
'summary': evt_title_str,
'description': evt_desc_str,
'start': {'date': evt_creation_stamp,},
'end': {'date': evt_creation_stamp,},
'recurrence': [rrule],
'reminders': {
    'useDefault': False,
    'overrides': [
        {
            'method': 'popup', 
            'minutes': evt_reminder_min_before
            },
        ],
    },
'attachments': [
    {
        'title': attach_file_meta.get('name'),
        'fileUrl': attach_file_meta.get('webViewLink'),
        'mimeType': attach_file_meta.get('mimeType'),
    },
],
}
# push event into calendar
event_exec = calendarAPI.events().insert(calendarId='primary', supportsAttachments=True, body=event).execute()
logger.info('an event has been created on google calendar with drive attachment file and corresponding metadata')

# save event meta into 'event_meta.json' file
module_meta = {
    'event-id': event_exec.get('id'),
    'event-topic': module_topic_str,
    'created': event_exec.get('start')['date'],
    'repetition-start': event_exec.get('start')['date'],
    'repetition-end': event_recur_until_date,
    'module-video-url': module_vid_url,
    'attach-file-url': event_exec.get('attachments')[0]['fileUrl'],
    'event-link': event_exec.get('htmlLink'),
    'recurrence': event_exec.get('recurrence'),
}
# check if 'event_meta.json' file exists
if os.path.exists(f'{taibah_academy_dir}/event_meta.json'):
    logger.info(f'found file "{taibah_academy_dir}/event_meta.json"')
    # if the file exists then load the file in reading mode
    with open(f'{taibah_academy_dir}/event_meta.json', 'r') as file_obj:
        #convert json object into python dict
        event_meta = json.load(file_obj)
        # check whether the course name is new or not
        # checking dict key concept taken from --> https://stackoverflow.com/a/1602964
        if course_name in event_meta:
            logger.info(f'course name {course_name} is found inside the json file')
            # if it's not a new course then append event meta into existing course
            event_meta[course_name][module_no] = module_meta
            logger.info('added module meta in the json file')
        else:
            # otherwise create new course entry and insert event meta into it
            event_meta[course_name] = {module_no: module_meta}
            logger.info(f'course name {course_name} not found inside the json file')
            logger.info(f'created a new entry "{course_name}" in the json file')

    # save the file
    with open(f'{taibah_academy_dir}/event_meta.json', 'w') as file_obj:
        # no utf-8 character escape concept taken from --> https://pynative.com/python-json-encode-unicode-and-non-ascii-characters-as-is/ 
        json.dump(event_meta, file_obj, indent=4, ensure_ascii=False)
        logger.info('saved the json file')
else:
    logger.info(f'file "{taibah_academy_dir}/event_meta.json" not found')
    # if the json file doesn't exist, then create one
    with open(f'{taibah_academy_dir}/event_meta.json', 'w') as file_obj:
        logger.info(f'created file "{taibah_academy_dir}/event_meta.json"')
        event_meta = {
            course_name: {
                module_no: module_meta
            }
        }
        logger.info('added course and module meta to json file')
        # save the formatted event meta into the file
        json.dump(event_meta, file_obj, indent=4, ensure_ascii=False)
        logger.info('saved the json file')


################################### Final Output #################################!FOUT!
# show process summary
proc_summary = f"""
####################### Process Summary #######################
---------------------------------------------------------------

        Event ID : {event_exec.get('id')}
     Event Topic : {module_topic_str}

         Created : {evt_creation_stamp}
Repetition Start : {event_exec.get('start')['date']}
Module Video URL : {module_vid_url}
      Event Link : {event_exec.get('htmlLink')}
      Recurrence : {event_exec.get('recurrence')}

---------------------------------------------------------------
                 Process Has Been Completed!!!
###############################################################
"""
print(proc_summary)