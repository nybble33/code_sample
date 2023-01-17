import requests


r = requests.post(
    "https://api.telegram.org/bot1842197193:AAGAkU5t6JYzeBogk2RAl2u-v7HHyNKmnp0/getWebhookInfo", data={})

print(r.status_code, r.reason)
print(r.text)
