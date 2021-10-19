import time
import requests

def ping():
    import platform
    import subprocess

    param = '-n' if platform.system().lower()=='windows' else '-c'

    if(subprocess.call(['ping', param, '1', "ec2-3-143-101-59.us-east-2.compute.amazonaws.com"]) == 1):
        bot_send_text("ec2-3-143-101-59.us-east-2.compute.amazonaws.com")
    if(subprocess.call(['ping', param, '1', "ec2-3-141-76-111.us-east-2.compute.amazonaws.com"]) == 1):
        bot_send_text("ec2-3-141-76-111.us-east-2.compute.amazonaws.com")  

def bot_send_text(server):

    bot_message = "El servidor "+server+" se encuentra caido"
    bot_token = '1784796735:AAGtcZtAfngDY224mkmdFFd3Okxfeyj5Hvs'
    bot_chatID = '1516729742'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)

while True:
    ping()
    time.sleep(60)
