import requestUtils

coinbaseMainDomain = "api.coinbase.com"
coinbaseExchangeDomain = "api.exchange.coinbase.com"

# this only gets the product ids that are ending with 'USD'.
def getProductsIDs():
    res = requestUtils.makeRequest('GET', coinbaseMainDomain, '/api/v3/brokerage/products')
    if res.status_code != 200: return []
    response = res.json()
    products = response['products']
    return [p['product_id'] for p in products if p['product_id'].split('-')[-1] == 'USD']

def getCandles(productId):
    #todo, construct path using productId, and calculate time, and granularity
    path = "/products/BTC-USD/candles?granularity=3600&start=1707120017&end=1707206417"
    res = requestUtils.makeRequest('GET', coinbaseExchangeDomain, path)
    if res.status_code != 200: return []
    print(res.json())

productIds = getProductsIDs()
getCandles('BTC-USD')
