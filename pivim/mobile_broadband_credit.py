"""The
"""
import requests
from lxml import html

USERNAME = "07465253874"
PASSWORD = "eq*mP@qCkxT6f$5C"

LOGIN_URL = "https://www.three.co.uk/My3Account/Login"
URL = "https://www.three.co.uk/New_My3/Account_balance"

def main():
    """The"""
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='lt']/@value")))[0]

    # Create payload
    payload = {"username": USERNAME, "password": PASSWORD, "lt": authenticity_token}
    
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)

    print(tree)


if __name__ == '__main__':
    main()