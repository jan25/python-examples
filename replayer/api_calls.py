import requests
import os
import json

REQUESTS_JSON_PATH = os.path.join(
    os.path.dirname(__file__), 'api_requests.json')

s: requests.Session = requests.Session()


class MalformedRequestsJsonError(Exception):
    """Error about malformed requests json input file"""


def read_json_file(path):
    with open(path) as f:
        return json.loads(f.read())
    raise MalformedRequestsJsonError()


def pretty_print(d: dict) -> None:
    print(json.dumps(d, indent=2, sort_keys=True))


def get_response(req) -> dict:
    try:
        res = s.get(req.get('url'))
        return {
            'status_code': res.status_code,
            'content': res.text,
            'data': res.json()
        }
    except Exception as e:
        return {
            'request': req,
            'error': e
        }


def post_response(req):
    try:
        res = s.post(req.get('url'), data=req.get('payload'))
        return {
            'status_code': res.status_code,
            'text': res.text,
            'data': res.json()
        }
    except Exception as e:
        return {
            'request': req,
            'error': e.with_traceback
        }


def main():
    request_list = read_json_file(REQUESTS_JSON_PATH)
    for req in request_list:
        if req.get('method') == 'GET':
            pretty_print(get_response(req))
        elif req.get('method') == 'POST':
            pretty_print(post_response(req))
        else:
            print('Method not implemented')


if __name__ == '__main__':
    main()
