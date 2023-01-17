
import requests

'''
r = requests.get(
    "https://api.telegram.org/bot1842197193:AAGAkU5t6JYzeBogk2RAl2u-v7HHyNKmnp0/setWebhook?url=https://nybble.ru/nbot/1842197193/&certificate=/home/nybble/nybble/conf/SSL_self/selfsigned.crt", data={}
    )
'''

r = requests.get(
    "https://api.telegram.org/bot1842197193:AAGAkU5t6JYzeBogk2RAl2u-v7HHyNKmnp0/setWebhook?url=https://nybble.ru/nbot/1842197193/", data={}
    )


print(r.status_code, r.reason)
print(r.text)
'''

    "https://api.telegram.org/bot1842197193:AAHH55ZLId2UkgcA8u9BBfnOC7q_m8y8qGs/setWebhook?url=https://nybble.ru/1842197193/", data={}



import urllib

content = urllib.request("https://api.telegram.org/bot1842197193:AAHH55ZLId2UkgcA8u9BBfnOC7q_m8y8qGs/setWebhook?url=https://nybble.ru/1842197193/")
print(content)
'''
'''

curl -F "url=https://IP_VPS:Port" -F "certificate=@/etc/ssl/certs/nginx-selfsigned.crt" "https://api.telegram.org/bot{ТокенБота}/setWebhook"

curl -F "url=https://nybble.ru/1842197193/" -F "certificate=@/home/nybble/nybble/conf/SSL/certificate.crt" "https://api.telegram.org/bot1842197193:AAHH55ZLId2UkgcA8u9BBfnOC7q_m8y8qGs/setWebhook"


'''
