__author__ = 'alexandre'

import requests
import ujson
from urlparse import urljoin
from functools import partial

#from IPython.core.debugger import Tracer; debug_here = Tracer

class SandsClient(object):

    def __init__(self, base_url, auth, headers):
        """
        Sands Client class constructor.

        :param base_url: string
         Base URL of the Sands API

        :param auth: 2-tuple of strings
         First username, second password, e.g.,
         ('alexandre', 'alex has no account')

        :param headers: dict
        HTTP request headers, e.g.,
        json_hdrs = {'content-type': 'application/json',
                     'accept': 'application/json'}

        xml_hdrs = {'content-type': 'application/xml',
                    'accept': 'application/xml'}
        """
        self._api_url = base_url
        self._auth = auth
        self._headers = headers
        self._endpoint_url = partial(urljoin, self._api_url)

        self._session = requests.Session()
        self._update_session()

    def _update_session(self):
        """
        Resets the auth and headers values in self._session,
        in case they have been changed.
        """
        self._session.auth = self._auth
        self._session.headers = self._headers

    def post(self, url_suffix, payload):
        """
        :param url_suffix: string

        :param payload: dict

        :param return: string
        post data ids
        """
        r = self._session.post(self._endpoint_url(url_suffix),
                               data=ujson.dumps(payload))

        try:
            resp = r.json()
            if '_id' in resp:
                return resp['_id']
            elif '_items' in resp:
                items = resp['_items']
                ids = [i['_id'] for i in items]
                return ids
            elif isinstance(resp, list):
                ids = [i['_id'] for i in resp]
                return ids
            else:
                return None

        except ValueError as ve:
            raise ve

    def patch(self, url_suffix, objectid, payload_patch):
        """
        :param url_suffix: string

        :param objectid: string

        :param payload_patch: dict

        :return
        post data ids
        """
        try:
            etag = self.get_by_id(self, url_suffix, objectid).json()['etag']

            patch_hdrs = self._headers.copy()
            patch_hdrs.update({'If-Match': etag})

            r = self._session.patch(self._endpoint_url(url_suffix),
                                    data=ujson.dumps(payload_patch),
                                    header=ujson.dumps({'If-Match': etag}))

            resp = r.json()
            if '_id' in resp:
                return resp['_id']
            elif '_items' in resp:
                items = resp['_items']
                ids = [i['_id'] for i in items]
                return ids
            elif isinstance(resp, list):
                ids = [i['_id'] for i in resp]
                return ids
            else:
                return None

        except ValueError as ve:
            raise ve

    def get(self, url_suffix):
        """
        :param url_suffix: string

        :param return: request
        """
        return self._session.get(self._endpoint_url(url_suffix))

    def get_by_id(self, url_suffix, object_id):
        """
        :param url_suffix: string

        :param return: request
        """
        return self.get(url_suffix + '/' + object_id)
