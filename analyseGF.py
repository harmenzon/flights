#!/usr/bin/python

import json
import datetime
import yaml
import pandas as pd

dir = '/services/python/flights/'
# dir = 'E:/Dropbox/GitHub/flights/'

with open(dir + 'dataGF.json') as data_file:
    data = json.load(data_file)

maxSalePrice = 2500
currency = 'EUR'
df = pd.DataFrame()
i = 0
columns = ['totalPrice', 'totalDuration1', 'conDuration1', 'flightCarrier1', 'totalDuration2',
           'conDuration2', 'flightCarrier2']

for option in data['trips']['tripOption']:
    tmp01 = []
    tmp02 = []
    saleTotal = option['saleTotal']
    saleTotal = saleTotal.replace(currency, '')
    saleTotal = float(saleTotal)
    tmp01.append(saleTotal)

    # if saleTotal <= maxSalePrice:
    #print('--- option ', i, '---')
    for slice in option['slice']:
        sliceDuration = slice['duration']
        tmp01.append(sliceDuration)

        for segment in slice['segment']:
            segmentDuration = segment['duration']
            flightCarrier = segment['flight']['carrier']
            flightNumber = segment['flight']['number']
            flightNumber = segment['flight']['number']
            aircraft = segment['leg'][0]['aircraft']
            arrivalTime = segment['leg'][0]['arrivalTime']
            departureTime = segment['leg'][0]['departureTime']
            origin = segment['leg'][0]['origin']
            tmp02.append(origin)
            destination = segment['leg'][0]['destination']
            tmp02.append(destination)
            legDuration = segment['leg'][0]['duration']
            mileage = segment['leg'][0]['mileage']
            try:
                connectionDuration = segment['connectionDuration']
                tmp01.append(connectionDuration)
            except:
                connectionDuration = 0

            #print(saleTotal, sliceDuration, flightCarrier, flightNumber, origin, destination, segmentDuration, connectionDuration)

        tmp01.append(flightCarrier)
        # tmp01.append(tmp02)

    df02 = pd.DataFrame([tmp01], columns=columns)
    # df02 = pd.DataFrame([tmp01])
    df = df.append(df02, ignore_index=True)

    i += 1


df['tt'] = df['totalDuration1'] + df['totalDuration2']
df['ct'] = df['conDuration1'] + df['conDuration2']
# df = df.sort_values(['totalPrice', 'tt'], ascending=[1, 1])
df = df.sort(['totalPrice', 'tt'], ascending=[1, 1])
df = df.head(n=1)
df = df.reset_index(drop=True)

dateTime = datetime.datetime.now()

with open(dir + 'pricesGF.yaml', 'r') as f:
    data = yaml.load(f)

tmpList01 = df.to_dict('records')
option = tmpList01[0]
option['dateTime'] = dateTime
data['data'].append(option)

with open(dir + 'pricesGF.yaml', 'w') as f:
    f.write(yaml.dump(data, default_flow_style=False))


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        #print('successfully sent the mail')
    except:
        #print("failed to send mail")
        pass

gmailUserName = 'harmenzon@gmail.com'
gmailPassword = 'bigmczzkgyqcaslg'
subject = 'Flight alert (EUR ' + str(option['totalPrice']) + ')'
body = 'This option meets your criteria: \n' + \
       'totalPrice: EUR' + str(option['totalPrice']) + '\n' + \
       'totalDuration: ' + str(option['tt']) + '\n' + \
       'totalStopOverDuration: ' + str(option['ct'])

if option['totalPrice'] <= maxSalePrice:
    send_email(gmailUserName, gmailPassword, 'harmenzon@gmail.com', subject, body)