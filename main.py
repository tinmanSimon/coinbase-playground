import requestUtils
import json

def getProductsIDs(filename = "tmp"):
    res = requestUtils.makeRequest("GET", "/api/v3/brokerage/products")
    if res.getcode() != 200: return
    response = json.loads(res.read().decode())
    products = response["products"]
    return [p["product_id"] for p in products]

getProductsIDs()