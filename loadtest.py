import urlparse
import json
from loads.case import TestCase

class TilesRecordDataTest(TestCase):

    # default server URL to match the nodejs testing
    # web server
    server_url = 'http://127.0.0.1:9999'

    def setUp(self):
        self.endpoint_click      = urlparse.urljoin(self.server_url, '/click')
        self.endpoint_impression = urlparse.urljoin(self.server_url, '/impression')
        self.endpoint_fetch      = urlparse.urljoin(self.server_url, '/fetch')

    def test_click(self):
        payload = self._makePayload(action='click')
        res = self.session.post(self.endpoint_click, data=json.dumps(payload))
        self.assertEqual(res.status_code, 200)

    def test_impression(self):
        payload = self._makePayload(action='impression')
        res = self.session.post(self.endpoint_impression, data=json.dumps(payload))
        self.assertEqual(res.status_code, 200)

    def test_fetch(self):
        payload = self._makePayload(action='fetch')
        res = self.session.get(self.endpoint_fetch, data=json.dumps(payload))
        self.assertEqual(res.status_code, 200)

    def _makePayload(self, action="click"):
        return {
                'action'    : action,
                'tile_id'   : 10,
                'position'  : 9,
                'pin'       : False,
                'timestamp' : 10,
                'ip'        : '10.0.1.1',
                'ua'        : 'loadtest client',
                'locale'    : 'en-US',
                'hll_index' : 275,
                'hll_value' : 8,
                'url'       : 'http://mozilla.org/path/to/something/crazy'
        }
