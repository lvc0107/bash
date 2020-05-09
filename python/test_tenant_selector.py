import json
import unittest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from time import sleep
from conf import (ENV,
                  auth,
                  us_username,
                  eu_username,
                  mmdb_username,
                  us_auth0_domain,
                  eu_auth0_domain,
                  APIGEE_API_KEY,
                  US_DEV_AUTH0_APP_CLIENT_ID,
                  EU_DEV_AUTH0_APP_CLIENT_ID,
                  US_QA_AUTH0_APP_CLIENT_ID,
                  EU_QA_AUTH0_APP_CLIENT_ID,
                  US_STAGING_AUTH0_APP_CLIENT_ID,
                  EU_STAGING_AUTH0_APP_CLIENT_ID
                  )

MAX_RETRIES = 5
TIMEOUT = 1


def make_requests_session_with_retries(max_retries):
    session = requests.Session()
    adapter = HTTPAdapter(
        max_retries=Retry(
            total=max_retries,
            status_forcelist=[  # this is a list of statuses to consider to be
                # an error and retry.
                429,  # Too many requests (i.e: back off)
                500,  # Generic internal server error
                502,  # Bad Gateway - i.e: upstream failure
                503,  # Unavailable, temporarily
                504,  # Gateway timeout
                522  # Origin connection timed out
            ],
            backoff_factor=1.0  # back off for 0s, 1s, 3s, 7s, etc... after
            # each successive failure. (factor*(2^N-1))
        ))

    # use retry for both HTTP and HTTPS connections.
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session


class ClearCache():
    headers = {"content-Type": "application/octet-stream"}
    params = {"action": "clear"}
    organization = "XXXXXX"
    auth = auth
    tc = unittest.TestCase('__init__')
    request = make_requests_session_with_retries(MAX_RETRIES)

    @classmethod
    def clear_cache(cls, cache_name):
        url_clear_cache = 'https://api.enterprise.apigee.com/v1/organizations/{organization}/environments/{env}/caches/{cache_name}/entries'. \
            format(organization=cls.organization, env=ENV, cache_name=cache_name)

        sleep(TIMEOUT)
        response = cls.request.post(url=url_clear_cache, headers=cls.headers, params=cls.params, auth=cls.auth)
        cls.tc.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        cls.tc.assertEqual(response_data["action"], "ClearCacheEntries")
        cls.tc.assertEqual(response_data["resourceName"], cache_name)

    @classmethod
    def clear_all_caches(cls):
        cls.clear_cache(cache_name='Auth0ClientId')
        cls.clear_cache(cache_name='Auth0ClientName')
        cls.clear_cache(cache_name='Auth0USAccessToken')
        cls.clear_cache(cache_name='Auth0EUAccessToken')


class TestTenantSelector(unittest.TestCase):
    apigee_apikey = APIGEE_API_KEY
    headers = {"content-Type": "application/json", "x-api-key": apigee_apikey}

    def setUp(self, *args, **kwargs):
        self.us_auth0_domain = us_auth0_domain
        self.eu_auth0_domain = eu_auth0_domain

        self.us_username = us_username
        self.eu_username = eu_username
        self.mmdb_username = mmdb_username

        self.request = make_requests_session_with_retries(5)
        if ENV == "dev":
            self.us_auth0_app_client_id = US_DEV_AUTH0_APP_CLIENT_ID
            self.eu_auth0_app_client_id = EU_DEV_AUTH0_APP_CLIENT_ID
            self.url = "https://apigee-domain-{env}.apigee.net/tenantselector/".format(env=ENV)

        elif ENV == "qa":
            self.us_auth0_app_client_id = US_QA_AUTH0_APP_CLIENT_ID
            self.eu_auth0_app_client_id = EU_QA_AUTH0_APP_CLIENT_ID
            self.url = "https://apigee-domain-{env}.apigee.net/tenantselector/".format(env=ENV)

        elif ENV == "staging":
            self.us_auth0_app_client_id = US_STAGING_AUTH0_APP_CLIENT_ID
            self.eu_auth0_app_client_id = EU_STAGING_AUTH0_APP_CLIENT_ID
            self.url = "https://api-staging.nationalgeographic.com/tenantselector/"

    def clear_all_caches(self):
        ClearCache.clear_all_caches()


class TestUserRegistedUSLocatedUS(TestTenantSelector):
    """
    User registered in US and located in US
    The Apigee cache is cleaned
    """

    def test_1a_cache(self):
        """
        Test 1a: clientID is ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "US", "clientId": "xxxxxxxxxxx"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

    def test_1b_cache(self):
        """
        Test 1b: clientId and defaultTenand(US) are ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "US", "clientId": "xxxxxxxxxxx", "defaultTenant": "US"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

    def test_1c_cache(self):
        """
        Test 1c: clientId and defaultTenand(EU) are ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "US", "clientId": "xxxxxxxxxxx", "defaultTenant": "EU"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

    def test_1d_cache(self):
        """
        Test 1d: clientId and defaultTenand(Any) are ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "US", "clientId": "xxxxxxxxxxx", "defaultTenant": "XX"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])


class TestUserRegistedUSLocatedEU(TestTenantSelector):
    """
    User registered in US and located in EU
    The Apigee cache is cleaned
    """

    def test_2a_cache(self):
        """
        Test 2a: Return redirect to US. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "EU", "clientId": self.eu_auth0_app_client_id}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

    def test_2b_cache(self):
        """
        Test 2b: Return redirect to US. defaultTenand(US) is ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "EU", "clientId": self.eu_auth0_app_client_id,
                "defaultTenant": "US"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

    def test_2c_cache(self):
        """
        Test 2c: Return redirect to US. defaultTenand(EU) is ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "EU", "clientId": self.eu_auth0_app_client_id,
                "defaultTenant": "EU"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

    def test_2d_cache(self):
        """
        Test 2d: Return redirect to US. defaultTenand(any) is ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "EU", "clientId": self.eu_auth0_app_client_id,
                "defaultTenant": "XXX"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.us_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])


class TestUserRegistedUSInvalidClientId(TestTenantSelector):
    """
    User registered in US. Invalid client Id
    The Apigee cache is cleaned
    """

    def test_3a_cache(self):
        """
        Test 3a: Error with invalid EU ClientId. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "EU", "clientId": "xxxxxxxxxxx"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the EU tenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the EU tenant.")

    def test_3b_cache(self):
        """
        Test 3b: Error with invalid EU ClientId and US defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": self.us_username, "tenantId": "EU", "clientId": "xxxxxxxxxxx", "defaultTenant": "US"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the EU tenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the EU tenant.")


class TestUserRegistedEULocatedEU(TestTenantSelector):
    """
    User registered in EU and located in EU
    The Apigee cache is cleaned
    """

    def test_4a_cache(self):
        """
        Test 4a: clientID is ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "EU", "clientId": "xxxxxxxxxxx"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

    def test_4b_cache(self):
        """
        Test 4b: clientID and defaultTenand(US) are ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "EU", "clientId": "xxxxxxxxxxx", "defaultTenant": "US"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

    def test_4c_cache(self):
        """
        Test 4c: clientID and defaultTenand(EU) are ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "EU", "clientId": "xxxxxxxxxxx", "defaultTenant": "EU"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

    def test_4d_cache(self):
        """
        Test 4d: clientID and defaultTenand(any) are ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "EU", "clientId": "xxxxxxxxxxx", "defaultTenant": "XX"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], "xxxxxxxxxxx")
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])


class TestUserRegistedEULocatedUS(TestTenantSelector):
    """
    User registered in EU and located in US
    The Apigee cache is cleaned
    """

    def test_5a_cache(self):
        """
        Test 5a: Return redirect to EU. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "US", "clientId": self.us_auth0_app_client_id}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

    def test_5b_cache(self):
        """
        Test 5b: Return redirect to EU. defaultTenand(US) is ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "US", "clientId": self.us_auth0_app_client_id,
                "defaultTenant": "US"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

    def test_5c_cache(self):
        """
        Test 5c: Return redirect to EU. defaultTenand(EU) is ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "US", "clientId": self.us_auth0_app_client_id,
                "defaultTenant": "EU"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

    def test_5d_cache(self):
        """
        Test 5b: Return redirect to EU. defaultTenand(XX) is ignored. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "US", "clientId": self.us_auth0_app_client_id,
                "defaultTenant": "XX"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], self.eu_username)
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])


class TestUserRegistedEUInvalidClientId(TestTenantSelector):
    """
    User registered in EU. Invalid client Id
    The Apigee cache is cleaned.
    """

    def test_6a_cache(self):
        """
        Test 6a: Error with invalid US ClientId. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "US", "clientId": "xxxxxxxxxxx"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the US tenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the US tenant.")

    def test_6b_cache(self):
        """
        Test 6b: Error with invalid US ClientId and EU defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": self.eu_username, "tenantId": "US", "clientId": "xxxxxxxxxxx", "defaultTenant": "EU"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the US tenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the US tenant.")


class TestUserNoRegistered(TestTenantSelector):
    """
    User not registered in any tenant.
    The Apigee cache is cleaned.
    """

    def test_7a_cache(self):
        """
        Test 7a: User Not registered and located in US without defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": "xxxxxx@xxxx.com", "tenantId": "US", "clientId": self.us_auth0_app_client_id}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"], {})
        self.assertEqual(response_data["message"],
                         "The user xxxxxx@xxxx.com is not registered in any tenant. Incorrect defaultTenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"], {})
        self.assertEqual(response_data["message"],
                         "The user xxxxxx@xxxx.com is not registered in any tenant. Incorrect defaultTenant.")

    def test_7b_cache(self):
        """
        Test 7b: User Not registered and located in EU without defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": "xxxxxx@xxxx.com", "tenantId": "US", "clientId": self.eu_auth0_app_client_id}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"], {})
        self.assertEqual(response_data["message"],
                         "The user xxxxxx@xxxx.com is not registered in any tenant. Incorrect defaultTenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"], {})
        self.assertEqual(response_data["message"],
                         "The user xxxxxx@xxxx.com is not registered in any tenant. Incorrect defaultTenant.")

    def test_7c_cache(self):
        """
        Test 7b: Not registered user located in EU with US as defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": "xxxxxx@xxxx.com", "tenantId": "EU", "clientId": self.eu_auth0_app_client_id,
                "defaultTenant": "US"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], "xxxxxx@xxxx.com")
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])
        self.assertEqual(response_data["message"], "The user xxxxxx@xxxx.com is not registered in any tenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], "xxxxxx@xxxx.com")
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])
        self.assertEqual(response_data["message"], "The user xxxxxx@xxxx.com is not registered in any tenant.")

    def test_7d_cache(self):
        """
        Test 7d: Not registered user located in US with EU as defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": "xxxxxx@xxxx.com", "tenantId": "US", "clientId": self.us_auth0_app_client_id,
                "defaultTenant": "EU"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], "xxxxxx@xxxx.com")
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertEqual(response_data["message"], "The user xxxxxx@xxxx.com is not registered in any tenant.")
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], "xxxxxx@xxxx.com")
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertEqual(response_data["message"], "The user xxxxxx@xxxx.com is not registered in any tenant.")
        self.assertTrue(response_data["content"]["redirect"])

    def test_7e_cache(self):
        """
        Test 7e:  Not registered user located in US with US as defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": "xxxxxx@xxxx.com", "tenantId": "US", "clientId": self.us_auth0_app_client_id,
                "defaultTenant": "US"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], "xxxxxx@xxxx.com")
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertEqual(response_data["message"], "The user xxxxxx@xxxx.com is not registered in any tenant.")
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], "xxxxxx@xxxx.com")
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertEqual(response_data["message"], "The user xxxxxx@xxxx.com is not registered in any tenant.")
        self.assertFalse(response_data["content"]["redirect"])

    def test_7f_cache(self):
        """
        Test 7f:  Not registered user located in EU with EU as defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": "xxxxxx@xxxx.com", "tenantId": "EU", "clientId": self.eu_auth0_app_client_id,
                "defaultTenant": "EU"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], "xxxxxx@xxxx.com")
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertEqual(response_data["message"], "The user xxxxxx@xxxx.com is not registered in any tenant.")
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "EU")
        self.assertEqual(response_data["content"]["username"], "xxxxxx@xxxx.com")
        self.assertEqual(response_data["content"]["clientId"], self.eu_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.eu_auth0_domain)
        self.assertEqual(response_data["message"], "The user xxxxxx@xxxx.com is not registered in any tenant.")
        self.assertFalse(response_data["content"]["redirect"])

    def test_7g_cache(self):
        """
        Test 7g:Not registered email with invalid defaultTenant. Cleaning The cache.
        :return:
        """
        data = {"username": "xxxxxx@xxxx.com", "tenantId": "EU", "clientId": self.eu_auth0_app_client_id,
                "defaultTenant": "XX"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"], {})
        self.assertEqual(response_data["message"],
                         "The user xxxxxx@xxxx.com is not registered in any tenant. Incorrect defaultTenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"], {})
        self.assertEqual(response_data["message"],
                         "The user xxxxxx@xxxx.com is not registered in any tenant. Incorrect defaultTenant.")

    def test_7h_cache(self):
        """
        Test 7h:  Not registered user with invalid clientID. Cleaning The cache.
        :return:
        """
        data = {"username": "xxxxxx@xxxx.com", "tenantId": "EU", "clientId": "xxxxxxxxxxx", "defaultTenant": "US"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the EU tenant.")

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"], "The provided client_id is not present in the EU tenant.")


class TestMissingParameters(TestTenantSelector):
    """
    Missing required parameters
    The Apigee cache is cleaned.
    """

    def test_8a(self):
        """
        Test 8a: Missing username.
        :return:
        """
        data = {"tenantId": "EU", "clientId": "xxxxxxxxxxx"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"],
                         "Missing parameters. Required parameters are: ['username', 'tenantId', 'clientId'].")

    def test_8b(self):
        """
        Test 8b: Missing clientId.
        :return:
        """
        data = {"username": "xxx@xxx.com", "tenantId": "US"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"],
                         "Missing parameters. Required parameters are: ['username', 'tenantId', 'clientId'].")

    def test_8c(self):
        """
        Test 8c: Missing tenantId.
        :return:
        """
        data = {"username": "xxx@xx.com", "clientId": "xxxxxxxxxxx"}

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["message"],
                         "Missing parameters. Required parameters are: ['username', 'tenantId', 'clientId'].")


class TestCORS(TestTenantSelector):
    """
    Missing required parameters
    The Apigee cache is cleaned.
    """

    def test_9a(self):
        """
        Test 9a: OPTIONS with response_data.
        :return:
        """
        data = {"username": "xxx@xx.com", "clientId": "xxxxxxxxxxx", "tenantId": "US"}
        sleep(TIMEOUT)
        response = requests.options(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["tenantId"], "US")
        self.assertEqual(response_data["username"], "xxx@xx.com")
        self.assertEqual(response_data["clientId"], "xxxxxxxxxxx")

    def test_9b(self):
        """
        Test 9b: OPTIONS without response_data.
        :return:
        """
        sleep(TIMEOUT)
        response = requests.options(url=self.url, headers=self.headers)
        self.assertEqual(response.status_code, 200)


class TestMMDB(TestTenantSelector):
    """
    User found in MMDB is redirected to US
    The Apigee cache is cleaned.
    """

    def test_10a(self):
        """
        Test 10a: User found in MMDB and located in US redirected to US.
        :return:
        """
        data = {"username": self.mmdb_username, "tenantId": "US", "clientId": self.us_auth0_app_client_id}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.mmdb_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.mmdb_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

    def test_10b(self):
        """
        Test 10b: User found in MMDB and located in EU redirected to US.
        :return:
        """
        data = {"username": self.mmdb_username, "tenantId": "EU", "clientId": self.eu_auth0_app_client_id}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.mmdb_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.mmdb_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

    def test_10c(self):
        """
        Test 10c User found in MMDB redirected to US even when the default tenant is EU.
        :return:
        """
        data = {"username": self.mmdb_username, "tenantId": "US", "clientId": self.us_auth0_app_client_id,
                "defaultTenant": "EU"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.mmdb_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.mmdb_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertFalse(response_data["content"]["redirect"])

    def test_10d(self):
        """
        Test 10d User found in MMDB redirected to US even when the default tenant is EU.
        :return:
        """
        data = {"username": self.mmdb_username, "tenantId": "EU", "clientId": self.eu_auth0_app_client_id,
                "defaultTenant": "EU"}
        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.mmdb_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])

        self.clear_all_caches()

        sleep(TIMEOUT)
        response = self.request.post(url=self.url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["content"]["tenantId"], "US")
        self.assertEqual(response_data["content"]["username"], self.mmdb_username)
        self.assertEqual(response_data["content"]["clientId"], self.us_auth0_app_client_id)
        self.assertEqual(response_data["content"]["tenantDomain"], self.us_auth0_domain)
        self.assertTrue(response_data["content"]["redirect"])


if __name__ == '__main__':
    # Use this for run an specific test suite
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestMMDB)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # Use this for run all test
    unittest.main(verbosity=2)
