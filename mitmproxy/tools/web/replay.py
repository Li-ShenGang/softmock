import requests
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


def proxy_req(result):
    data = result['data']
    req = data['request']
    url = (req['scheme'] + '://' + req['host'] + req['path']).strip()
    headers = parse_headers(req['headers'])
    req_data = req['raw_content']
    print('replay:', req['method'], url)
    resp = requests.request(req['method'], url, headers=headers, data=req_data,
                            timeout=(10, 10), proxies=proxy)
    if not data['response']:
        data['response'] = {}
    content_type = resp.headers['content-type'] or resp.headers['Content-type']
    data['response']['headers'] = dump_headers(resp.headers)
    if 'image' in content_type or 'video' in content_type:
        data['response']['html'] = base64.b64encode(resp.content).decode()
    else:
        data['response']['html'] = resp.text
    return result
