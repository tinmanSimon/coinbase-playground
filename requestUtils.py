
from coinbase import jwt_generator
from coinbase.constants import USER_AGENT
import http.client

# mysecrets is not uploaded for security reasons. it just contains api_key and api_secret.
from mysecrets import api_key, api_secret

def getJWT(request_method, request_path):
    jwt_uri = jwt_generator.format_jwt_uri(request_method, request_path)
    jwt_token = jwt_generator.build_rest_jwt(jwt_uri, api_key, api_secret)
    return jwt_token

def getCBHeaders(jwt_token):
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}",
        "User-Agent": USER_AGENT,
    }

# returns response. use res.getcode() to get request code, use res.read() to get the response data.
def makeRequest(method, path, payload = ''):
    jwt_token = getJWT(method, path)
    headers = getCBHeaders(jwt_token)
    conn = http.client.HTTPSConnection("api.coinbase.com")
    conn.request(method, path, payload, headers)
    res = conn.getresponse()
    if res.getcode() != 200:
        # error handling
        print("Error for makeRequest of", method, path, "errorCode:", res.getcode())
        print("Err body: ", res.read())
    return res


