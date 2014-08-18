import urlparse
import json
from random import randint
from loads.case import TestCase

class TilesRecordDataTest(TestCase):

    # default server URL to match the nodejs testing web server
    server_url = 'http://127.0.0.1:9999'

    # cache of payload bodies to avoid JSON generation overhead
    payloads = [
        '{"locale":"en-US","tiles":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10}]}'
        , '{"locale":"en-US","tiles":[{"id":1,"pin":1},{"id":2},{"id":3},{"id":4},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10}],"pin":0}'
        , '{"locale":"en-US","tiles":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10}],"unpin":0}'
        , '{"locale":"en-US","tiles":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10}],"block":0}'
        , '{"locale":"en-US","tiles":[{"id":2},{"id":3},{"id":4},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10}]}'
        , '{"locale":"en-US","tiles":[{"id":5,"url":"https://m.load"},{"id":2},{"id":3},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10}]}'
        , '{"locale":"en-US","tiles":[{"id":5,"url":"https://m.load"},{"url":"https://twitter.com/firefox"},{"id":2},{"id":3},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10}]}'
        , '{"locale":"en-US","tiles":[{"id":5,"url":"https://m.load"},{"id":2},{"id":3},{"id":6},{"id":8},{"id":9},{"id":10},{"pin":1,"pos":8,"url":"https://twitter.com/firefox"}]}'
    ]

    def setUp(self):
        self.endpoint_click = urlparse.urljoin(self.server_url, '/click')
        self.endpoint_view  = urlparse.urljoin(self.server_url, '/view')
        self.endpoint_fetch = urlparse.urljoin(self.server_url, '/fetch')

    def test_click(self):
        pass

    def test_view(self):
        pass

    def test_fetch(self):
        pass

    # just generates a bunch of requests. Rather than waste CPU cycles generating
    # specific json payloads, we'll just use some pre-canned ones and send 
    # those along as much of the work is done on the server
    def test_justload(self):
        payload = self.payloads[randint(0, len(self.payloads) - 1)]
        res = self.session.post(self.endpoint_click, data=payload)
        self.assertEqual(res.status_code, 200)

