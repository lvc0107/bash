from pygments import highlight, lexers, formatters
import requests
import json
import get_access_token as at
import os
import sys


def usage():
    """
    Call this funtion passing user email:
    Example:
    python get_user_by_id.py aaa@some.com
    """
    print usage.__doc__
    exit()


if __name__ == '__main__':
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + at.access_token
    }
    try:
        email = sys.argv[1]
    except IndexError:
        usage()
    user_url = os.environ["AUDIENCE"] + "users-by-email/email={0}".format(email)
    res = requests.get(user_url, headers=headers)
    formatted_json = json.dumps(res.json(), indent=4, sort_keys=True)
    print highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    #res.raise_for_status()
