import requests

# base_url = "https://api.github.com/"
# token = "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"

# username = "priyamcoding"

# url = base_url + "user"
# response = requests.get(url, auth= (token, ''))
# print(response)
# print (response.json())

# # we are concatenating user which is an endpoint to the github base_url
# # and if we change that to users, it gives us a list of ALL users

# # updating authenticated user

# url = base_url + "user"
# response = requests.patch(url, auth= (token, ''))
# todo = {"name": "priyamcoding"}
# print(response)
# print (response.json())

# #post method 


#working on a public api 
response = requests.get("https://www.adoptapet.com/public/apis/pet_list.html")
print(response)
print(response.headers["Content-Type"])

response = requests.post("https://www.adoptapet.com/public/apis/pet_list.html")
print(response)
print(response.headers)

query = {'Lat': '-40.55279', 'Lon': '-121.95272'}
response = requests.get("https://www.google.com/maps", params = query)
print(response)
# print(response.json())
print(response.text)