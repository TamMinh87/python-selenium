import requests
import json
import xmljson
import xml.etree.cElementTree as cElementTree
from requests.exceptions import RequestException


def send_request(endpoint, options):
    try:
        # send request
        response = requests.get(endpoint, options)

        # parse xml to json
        xml = cElementTree.fromstring(response.text)
        return json.loads(json.dumps(xmljson.badgerfish.data(xml)))

    except RequestException as e:
        raise RequestException("send request error: {}", e.args)
