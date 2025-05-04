string = ("abcd123435@xyz.com")
# abscd@xyz.com
# 12345@xyz.com
# var = "abcd@xyz.com"
var = "a12345@xyz.com"
var = var.split("@")
result = "invalid" if var[0].isalnum() else "valid"
print(result)