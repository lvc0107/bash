from pygments import highlight, lexers, formatters
import requests
import json
import get_access_token as at
import os
import sys


def usage():
    """
    Usage:
    python get_connection_by_id.py con_rNRU22BU07nSdLMW
    """
    print usage.__doc__
    exit()


if __name__ == '__main__':
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + at.access_token
    }
    try:
      conn_id = sys.argv[1]
    except IndexError:
        usage()

    conn_url = os.environ["AUDIENCE"] + "connections/{}".format(conn_id)
    res = requests.get(conn_url, headers=headers)
    formatted_json = json.dumps(res.json(), indent=4, sort_keys=True)
    print highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    res.raise_for_status()
