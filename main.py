# Python script to find free slots to get a CoVID-19 vaccination in India
# Based on the APIs available at https://apisetu.gov.in/public/marketplace/api/cowin
# Author: Apurva Joshi
# E-mail: firstname[dot]lastname[at]iitbombay.org

import requests
import winsound
import json
import datetime
import time
from requests.models import to_native_string

from requests.sessions import session

TNA = '392'
MUM = '395'

def audio_alert():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def hdl_time(week_no):
    today = datetime.date.today()
    next_date = today + datetime.timedelta(weeks = week_no)
    next_date= next_date.strftime('%d-%m-%Y')
    chk_date = str(next_date)
    return chk_date

def hdl_request(place, week_no):
    preamble = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='
    link = preamble + place + '&date=' + hdl_time(week_no)
    response = requests.get(link)
    #response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=395&date=02-05-2021')
    print('-------------------------------------------')
    print('Checking for week starting: ', hdl_time(week_no))
    print('-------------------------------------------')
    data = response.json()

    no_of_centers = len(data["centers"])
    print("Total no. of centers providing vaccinations: ", no_of_centers)

    ref_id = []
    ref_id_age = []

    for i in range(0,no_of_centers):
        
        sample = data["centers"][i]
        sessions_data = sample["sessions"]
        sessions_data = sessions_data[0]
        available = sessions_data["available_capacity"]
        if available > 0:
            ref_id.append(i)

    no_vacc_centers = len(ref_id)
    print('No. of centers with open slots: ', no_vacc_centers)
    # data_filtered = {k: data["centers"][k] for k in ref_id}
    # print('Details of centers: ', data_filtered)

    # Check whether slots are open for 18+
    for i in ref_id:
        age = data["centers"][i]["sessions"][0]["min_age_limit"]
        if age == 18:
            ref_id_age.append(i)
    no_vacc_centers_18yo = len(ref_id_age)
    print('No. of centers with open slots for age 18+: ', no_vacc_centers_18yo)
    if no_vacc_centers_18yo > 0:
        for i in ref_id_age:
            pincode = data["centers"][i]["pincode"]
            if pincode < 400800:
                audio_alert()
                print(data["centers"][i])

if __name__ == "__main__":
    no_of_weeks = 10 
    while True:
        print('***********************************************')
        print('Checking for free slots in Thane at', datetime.datetime.now())
        print('***********************************************')
        for week in range(0, no_of_weeks):
            hdl_request(TNA, week)
        
        time.sleep(30)
        
        print('***********************************************')
        print('Checking for free slots in Mumbai at', datetime.datetime.now())
        print('***********************************************')
        for week in range(0, no_of_weeks):
            hdl_request(MUM, week)

        time.sleep(30)
