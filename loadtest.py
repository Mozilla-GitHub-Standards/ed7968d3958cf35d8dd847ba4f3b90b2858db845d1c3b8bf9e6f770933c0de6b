import urlparse
from loads.case import TestCase

class TilesRecordDataTest(TestCase):

    # default server URL to match the nodejs testing
    # web server
    server_url = 'http://127.0.0.1:9999'

    def setUp(self):
        self.endpoint_click      = urlparse.urljoin(self.server_url, '/click')
        self.endpoint_impression = urlparse.urljoin(self.server_url, '/impression')
        self.endpoint_fetch      = urlparse.urljoin(self.server_url, '/fetch')

        print self.endpoint_fetch

    def test_click(self):
        res = self.session.get(self.endpoint_click)
        self.assertEqual(res.status_code, 200)

    def test_impression(self):
        res = self.session.get(self.endpoint_impression)
        self.assertEqual(res.status_code, 200)

    def test_click(self):
        res = self.session.get(self.endpoint_fetch)
        self.assertEqual(res.status_code, 200)
