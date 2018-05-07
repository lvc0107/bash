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
    python change_email_user.py --id=6153 --email=new_email@yopmail.com
    python change_email_user.py -i 6153 -e new_email@yopmail.com
    """
    print usage.__doc__
    exit()


if __name__ == '__main__':
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + at.access_token
    }

    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:i:v", [
                                   "help", "email=", "id="])
    except getopt.GetoptError as err:
        usage()

    user_id = email = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-e", "--email"):
            email = a
        elif o in ("-i", "--id"):
            user_id = "auth0|" + a
        else:
            usage()
    if not user_id:
        usage()
    if not email:
        usage()

    user_url = os.environ["AUDIENCE"] + "users/{}".format(user_id)
    res = requests.get(user_url, headers=headers)
    res.raise_for_status()

    user_payload = {
        "email": email,
        "email_verified": False,
        "verify_email": True,
        "connection": os.environ["CONNECTION"],
        "client_id": os.environ["CLIENT_ID"]
    }

    print "USER PAYLOAD:"
    formatted_json = json.dumps(user_payload, indent=4, sort_keys=True)
    print highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())

    res = requests.patch(user_url, data=json.dumps(
        user_payload), headers=headers)
    print "RESPONSE:"
    formatted_json = json.dumps(res.json(), indent=4, sort_keys=True)
    print highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    res.raise_for_status()
