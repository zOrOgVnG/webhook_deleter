import time
import requests
import pyfiglet

banner = pyfiglet.figlet_format("dxvl#0001")

print(banner)
hook = input("URL du webhook : ")
def delete(webhook):
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print("\n [✔] Succes, webhook deleted.")
    elif check.status_code == 200:
        print("\n [✗] Fail, impossible to remove the webhook.")

kingman_top = 1
if kingman_top == 1:
    delete(hook)
