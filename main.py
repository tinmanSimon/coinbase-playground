import requestUtils
res = requestUtils.makeRequest("GET", "/api/v3/brokerage/products")
print(res.read())