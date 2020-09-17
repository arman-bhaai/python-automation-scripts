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
# \\//               Version: v1.1                                                                                        \\//
#  \/        Versioning Date: 2020-09-18                                                                                   \/
#  /\                                                                                                                      /\
# //\\               License: Custom License                                                                              //\\
# \\//                                                                                                                    \\//
#  \/           Dev Language: Python 3.6.9                                                                                 \/
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



#################################### Import Packages ####################################!IMPAC
# scaffold code was taken from --> https://developers.google.com/calendar/quickstart/python
# $ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib sh
from datetime import datetime, timedelta
import pickle
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import json
import sh
import logging


# main functional class
class ConsoleApp:
    def __init__(
                self, 
                course_name, 
                module_no,
                module_topic_str,
                module_vid_url, 
                evt_creation_stamp, 
                evt_reminder_min_before,
                raw_attach_file_path,
                taibah_academy_dir,
                repeat_freq,
                event_recur_until_date,
                api_creds_file,
                json_file_path):
        # create a custom logger instance
        self.init_logger()

        # define event info
        # course name
        self.course_name = course_name # ex: 'Study Skills'
        # module number
        self.module_no = module_no #ex: '01'
        # module topic
        self.module_topic_str = module_topic_str #ex: 'আলোচ্য বিষয়ঃ'
        # video url of the module lecture
        self.module_vid_url = module_vid_url # ex: 'https://youtu.be/jYrwAysfBBg'
        # the date when the event is being created
        self.evt_creation_stamp = evt_creation_stamp # ex: '2020-08-29'
        # a notification should appear before specified minutes of the event date
        self.evt_reminder_min_before = evt_reminder_min_before # ex: 120
        # path to raw attachment local directory
        self.raw_attach_file_path = raw_attach_file_path # ex: '/home/antidote/Desktop/taibahacadmy_raw'
        # path to taibah academy directory, where final and processed pdfs and events info will reside
        self.taibah_academy_dir = taibah_academy_dir # ex: '/home/antidote/Taibah Academy'
        # event recurrence rule
        self.repeat_freq = repeat_freq # ex: 'MONTHLY'
        # the date until which the event should recur
        self.event_recur_until_date = event_recur_until_date # ex: '20200913'
        # google credentials json file
        self.api_creds_file = api_creds_file # ex: '/home/antidote/credentials.json'
        # json file path for saving meta info  
        self.json_file_path = json_file_path # ex: /home/antidote/Taibah Academy/event_meta.json

        self.logger.info('defined primary variables')

        # initialize main function
        self.main()

    # create a custom logger instance
    def init_logger(self):
        self.logger = logging.getLogger('__name__')
        # logger level concept was taken from --> https://www.toptal.com/python/in-depth-python-logging
        self.logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        log_format = logging.Formatter('[%(levelname)s] >>> %(message)s')
        console_handler.setFormatter(log_format)
        self.logger.addHandler(console_handler)

    # main function
    def main(self):
        # process primary variables
        self.process_variables()
    
        # oAuth login
        self.google_login()
        
        # check duplicate module
        self.check_duplicate_module()

        # rename and move the file to taibah academy dir from raw dir
        self.move_to_taibahacademy_dir()

        # upload attachment pdf to google drive from taibahacademy dir and return attach meta (id, name, mimeType, webViewLink)
        self.attach_file_meta = self.upload_attach_to_drive()

        # create an event on google calendar and return the event object
        self.event_exec = self.create_event_in_calendar()

        # save event meta into 'event_meta.json' file
        self.save_as_json()

        # show process summary
        self.show_proc_summary()

    # process primary variables
    def process_variables(self):
        # construct event title string (summary) with combination of course name and module number
        self.evt_title_str = f'{self.translate_course_name(self.course_name)} - {self.translate_module_no(self.module_no)}'
        # construct module number string from module number
        self.module_no_str = f'Module - {self.module_no}'
        # construct html link from module video url
        # html link concept was taken from --> https://webapps.stackexchange.com/a/28115
        self.module_vid_url_html = f'<a href="{self.module_vid_url}"><b>Watch Video</b></a>'
        # construct event description with combination of module topic string and html link of module video
        self.evt_desc_str = self.module_topic_str + '\n\n' + self.module_vid_url_html
        # construct attachment file name from module name
        self.attach_name = f'{self.module_no_str}.pdf'
        # get corresponding remote dir id by name with help of switch function
        self.attach_remote_parent_id = self.translate_remote_dir_id(self.course_name)
        # create datetime object for today
        self.evt_creation_dt_obj = datetime.strptime(self.evt_creation_stamp, '%Y-%m-%d')
        # event recurrence rule
        # the day of the month when the events will occur
        self.month_day = self.evt_creation_dt_obj.day
        # rrule is for scheduled events
        self.rrule = [f'RRULE:FREQ={self.repeat_freq};UNTIL={self.event_recur_until_date};INTERVAL=1;BYMONTHDAY={self.month_day}']

        self.logger.info('processed secondary variables')

    # oAuth verification
    def google_login(self):
        # define global variables
        # If modifying these scopes or want to change google account, then delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/calendar', 
                'https://www.googleapis.com/auth/drive.metadata.readonly',
                'https://www.googleapis.com/auth/drive.file',]
        # perform oAuth Login
        self.creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time
        if os.path.exists('token.pickle'):
            self.logger.info('token.pickle file exists')
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
                self.logger.info('credentials have been loaded from token.pickle file')
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            self.logger.info('no valid credentials have been found. please login')
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.api_creds_file, SCOPES)
                self.creds = flow.run_local_server(port=0)
                self.logger.info(f'taken user information from file {self.api_creds_file}')
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
                self.logger.info('credentials have been saved into token.pickle file')
        # finished oAuth Login
        self.logger.info('finished oAuth login')
    
    # check for duplicate module entry
    def check_duplicate_module(self):
        # check if json event meta file exists
        if os.path.exists(self.json_file_path):
            self.logger.info(f'found file "{self.json_file_path}"')
            # if the file exists then load the file in reading mode
            with open(self.json_file_path, 'r') as file_obj:
                # convert json object into python dict
                event_meta = json.load(file_obj)
                # check whether the course name is new or not
                # checking dict key concept was taken from --> https://stackoverflow.com/a/1602964
                if self.course_name in event_meta:
                    # check if the module no already exists in the course data
                    try:
                        assert (self.module_no not in event_meta[self.course_name]), f'"Module - {self.module_no}" entry already exists in "{self.course_name}" course'
                        self.logger.info('duplicate module check --> passed')
                    except:
                        self.logger.error(f'"Module - {self.module_no}" entry already exists in "{self.course_name}" course')
                        exit()
    
    # rename and move the file to taibah academy
    def move_to_taibahacademy_dir(self):
        # check if the corresponding course dir is present inside taibah academy dir
        if not os.path.exists(f'{self.taibah_academy_dir}/{self.course_name}'):
            # if not, then create a dir within taibah academy dir with corresponding course name
            sh.mkdir('-p', f'{self.taibah_academy_dir}/{self.course_name}')
            self.logger.info(f'the course name dir "{self.course_name}" doesn\'t exist. so created a new dir named "{self.taibah_academy_dir}/{self.course_name}"')
        # check if the file exists
        try:
            # move the file to corresponding categorized dir
            sh.mv(self.raw_attach_file_path, f'{self.taibah_academy_dir}/{self.course_name}/{self.module_no_str}.pdf')
            self.logger.info(f'renamed and moved {self.raw_attach_file_path} to {self.taibah_academy_dir}/{self.course_name}/{self.module_no_str}.pdf')
        except:
            self.logger.error(f'file {self.raw_attach_file_path} not found')
            exit()

    # upload attachment pdf to google drive from taibahacademy dir and return attach meta (id, name, mimeType, webViewLink)
    def upload_attach_to_drive(self):
        # get API services for Google Drive
        # concept of disabling cache_discovery was taken from --> https://github.com/googleapis/google-api-python-client/issues/299#issuecomment-288190015
        driveAPI = build('drive', 'v3', credentials=self.creds, cache_discovery=False)

        self.logger.info(f'uploading file "{self.taibah_academy_dir}/{self.course_name}/{self.attach_name}" to google drive inside corresponding parent dir...')
        # return attachment file metadata (id, name, webViewLink) from google drive
        attach_file_meta = driveAPI.files().create(body={'name': self.attach_name, 'parents': [self.attach_remote_parent_id]}, media_body=MediaFileUpload(f'{self.taibah_academy_dir}/{self.course_name}/{self.attach_name}', resumable=True), fields='id, name, mimeType, webViewLink').execute()
        return attach_file_meta

    # create an event on google calendar and return the event object
    def create_event_in_calendar(self):
        # get API services for Google Calendar
        calendarAPI = build('calendar', 'v3', credentials=self.creds, cache_discovery=False)
        # define event body
        event = {
        'summary': self.evt_title_str,
        'description': self.evt_desc_str,
        'start': {'date': self.evt_creation_stamp,},
        'end': {'date': self.evt_creation_stamp,},
        'recurrence': self.rrule,
        'reminders': {
            'useDefault': False,
            'overrides': [
                {
                    'method': 'popup', 
                    'minutes': self.evt_reminder_min_before
                    },
                ],
            },
        'attachments': [
            {
                'title': self.attach_file_meta.get('name'),
                'fileUrl': self.attach_file_meta.get('webViewLink'),
                'mimeType': self.attach_file_meta.get('mimeType'),
            },
        ],
        }

        self.logger.info('an event is being created on google calendar with drive attachment file and corresponding metadata...')
        # push event into calendar
        event_exec = calendarAPI.events().insert(calendarId='primary', supportsAttachments=True, body=event).execute()
        return event_exec

    # save event meta into json file
    def save_as_json(self):
        # retrieve event meta into dict
        module_meta = {
            'event-id': self.event_exec.get('id'),
            'event-topic': self.module_topic_str,
            'created': self.event_exec.get('start')['date'],
            'repetition-start': self.event_exec.get('start')['date'],
            'repetition-end': self.event_recur_until_date,
            'module-video-url': self.module_vid_url,
            'attach-file-url': self.event_exec.get('attachments')[0]['fileUrl'],
            'event-link': self.event_exec.get('htmlLink'),
            'recurrence': self.event_exec.get('recurrence'),
        }
        # check if 'event_meta.json' file exists
        if os.path.exists(self.json_file_path):
            self.logger.info(f'found file "{self.json_file_path}"')

            self.logger.info('saving the json file...')
            # if exists, then load the file in reading mode
            with open(self.json_file_path, 'r') as file_obj:
                #convert json object into python dict
                event_meta = json.load(file_obj)
                # check whether the course name is new or not
                # checking dict key concept was taken from --> https://stackoverflow.com/a/1602964
                if self.course_name in event_meta:
                    self.logger.info(f'course name {self.course_name} is found inside the json file')
                    # if not new course, insert module meta into module no
                    event_meta[self.course_name][self.module_no] = module_meta
                    self.logger.info('added module meta in the json file')
                else:
                    # if new course, then create new course entry and insert event meta into it
                    event_meta[self.course_name] = {self.module_no: module_meta}
                    self.logger.info(f'course name {self.course_name} not found inside the json file')
                    self.logger.info(f'created a new entry "{self.course_name}" in the json file')

            # save the file
            with open(self.json_file_path, 'w') as file_obj:
                # no utf-8 character escape concept was taken from --> https://pynative.com/python-json-encode-unicode-and-non-ascii-characters-as-is/ 
                json.dump(event_meta, file_obj, indent=4, ensure_ascii=False)
        else:
            self.logger.info(f'file "{self.json_file_path}" not found')
            # if the json file doesn't exist, then create one
            with open(self.json_file_path, 'w') as file_obj:
                self.logger.info(f'created file "{self.json_file_path}"')
                event_meta = {
                    self.course_name: {
                        self.module_no: module_meta
                    }
                }
                self.logger.info('added course and module meta to json file')
                # write formatted event meta to the file
                json.dump(event_meta, file_obj, indent=4, ensure_ascii=False)
                self.logger.info('saved the json file')

    # show process summary
    def show_proc_summary(self):
        self.logger.info('generating process summary...')
        proc_summary = f"""
####################### Process Summary #######################
---------------------------------------------------------------

    Event Name : {self.event_exec.get('summary')}
        Event ID : {self.event_exec.get('id')}
    Event Topic : {self.module_topic_str}

        Created : {self.evt_creation_stamp}
Repetition Start : {self.event_exec.get('start')['date']}
Module Video URL : {self.module_vid_url}
    Event Link : {self.event_exec.get('htmlLink')}
    Recurrence : {self.event_exec.get('recurrence')}

---------------------------------------------------------------
                Process Has Been Completed!!!
###############################################################
"""
        print(proc_summary)

    # define switches
    # python switch concept was taken from --> https://jaxenter.com/implement-switch-case-statement-python-138315.html
    # switch from course name to google drive course directory id
    def translate_remote_dir_id(self, dir_name):
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

    # switch from english course name to bengali course name
    def translate_course_name(self, course_name):
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

    # switch from english short module no to bengali long module no
    def translate_module_no(self, module_no):
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

def main():
    ConsoleApp(
        course_name = 'Information Technology', 
        module_no = '06', 
        module_topic_str = 'hello', 
        module_vid_url = 'https://youtu.be/jYrwAysfBBg', 
        evt_creation_stamp = '2020-08-18', 
        evt_reminder_min_before = 120,
        raw_attach_file_path = '/home/antidote/Desktop/taibahacadmy_raw/ff.pdf',
        taibah_academy_dir = '/home/antidote/Taibah Academy',
        repeat_freq = 'MONTHLY',
        event_recur_until_date = '20200925',
        api_creds_file = 'credentials.json',
        json_file_path = '/home/antidote/Taibah Academy/event_meta.json',
    )

if __name__ == '__main__':
    main()