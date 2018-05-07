from pygments import highlight, lexers, formatters
import requests
import json
import get_access_token as at
import os
import sys


def usage():
    """
    Usage:
    python update_connection_change_email.py con_rNRU22BU07nSdLMW
    """
    print usage.__doc__
    exit()


if __name__ == '__main__':
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + at.access_token
    }

    conn_payload = {
        "enabled_clients": [
           "xxxxxxxxxxxxxxxxxxxx"
        ],
        "options": {
            "brute_force_protection": True,
            "configuration": {
                "key1": "value",
                "key2": "value",

                "auth0_clientcrt": "",
               "auth0_clientkey": "",
                "auth0_passphrase": "auth0;;;",

                "auth0_selfca": ""           
		},
            "customScripts": {
                "change_email": "function changeEmail (oldEmail, newEmail, verified, callback) { }",
                "change_password": ""
           },
            "enabledDatabaseCustomization": True,
            "requires_username": True,
            "mfa": {
                "active": True,
                "return_enroll_settings": True
            },
            "passwordPolicy": "good",
            "strategy_version": 2
        }
    }

    try:
        conn_id = sys.argv[1]
    except IndexError:
        usage()
    conn_url = os.environ["AUDIENCE"] + "connections/{}".format(conn_id)
    res = requests.patch(url=conn_url,
                         data=json.dumps(conn_payload),
                         headers=headers)
    formatted_json = json.dumps(res.json(), indent=4, sort_keys=True)
    print highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    res.raise_for_status()
