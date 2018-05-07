from pygments import highlight, lexers, formatters
import requests
import json
import get_access_token as at
import os
import sys
import getopt


def usage():
    """
    Usage:
    python create_user.py --user=user1 --email=user1@yopmail.com
    python create_user.py -u user1 -e user1@yopmail.com
    """
    print usage.__doc__
    exit()


if __name__ == '__main__':
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + at.access_token
    }
    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:u:v", [
                                   "help", "email=", "user="])
    except getopt.GetoptError as err:
        usage()

    username = email = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-e", "--email"):
            email = a
        elif o in ("-u", "--user"):
            username = a
        else:
            usage()
    if not username:
        usage()
    if not email:
        usage()

    user_url = os.environ["AUDIENCE"] + "users"

    user_payload = {
        "email": email,
        "username": username,
        "password": "Password123",
        "user_metadata": {
            "given_name": "migue",
            "last_name": "vargas",
            "birth_year": "1981",
            "birth_month": "11",
            "birth_day": "11",
            "city": "cordoba",
            "state": "cordoba",
            "country": "argentine"
        },
        "connection": os.environ["CONNECTION"]
    }

    print "USER PAYLOAD:"
    formatted_json = json.dumps(user_payload, indent=4, sort_keys=True)
    print highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())

    res = requests.post(user_url, json.dumps(user_payload), headers=headers)
    print "RESPONSE:"
    formatted_json = json.dumps(res.json(), indent=4, sort_keys=True)
    print highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    res.raise_for_status()
