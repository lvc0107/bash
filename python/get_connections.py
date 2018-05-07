from pygments import highlight, lexers, formatters
import requests
import json
import get_access_token as at
import os

if __name__ == '__main__':
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + at.access_token
    }

    res = requests.get(os.environ["AUDIENCE"] + "connections",
                       headers=headers)
    formatted_json = json.dumps(res.json(), indent=4, sort_keys=True)
    print highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    res.raise_for_status()
