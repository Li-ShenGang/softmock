import requests
import ahttp
import base64

proxy = {
    'http': None,
    'https': None
}


def parse_headers(headers):
    result = {}
    for i in headers:
        result[i[0]] = i[1]
    return result


def dump_headers(headers):
    result = []
    for key, value in headers.items():
        result.append([key, value])
    return result


def proxy_req(result, serve_url):
    data = result['data']
    req = data['request']
    url = (req['scheme'] + '://' + req['host'] + req['path']).strip()
    headers = parse_headers(req['headers'])
    req_data = req['raw_content']
    print('replay:', req['method'], url)
    resp = requests.get(url, headers=headers, data=req_data,
                        timeout=(3, 3), proxies=proxy)
    if not data['response']:
        data['response'] = {}
    data['response']['headers'] = dump_headers(resp.headers)
    data['response']['html'] = resp.text
    return result
