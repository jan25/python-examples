from replayer.api_calls import get_response
import unittest
from unittest.mock import patch, Mock, MagicMock

SAMPLE_GET_RESPONSE = MagicMock(status_code=200, text='success!')
SAMPLE_GET_RESPONSE.json = lambda: {'status_code': 200, 'text': 'success!'}


class TestApiCalls(unittest.TestCase):
    @patch('replayer.api_calls.requests.Session.get', return_value=SAMPLE_GET_RESPONSE)
    def test_get_response(self, mock_get):

        result = get_response({'url': 'https://host/path?params'})
        self.assertEqual(result, {
            'status_code': 200,
            'content': 'success!',
            'data': {'status_code': 200, 'text': 'success!'}
        })
