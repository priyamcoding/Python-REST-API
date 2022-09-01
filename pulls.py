# # #imported required libraries

# import requests
# import json

# # # Base URL of GitHub API and authentication token

# base_url = "https://api.github.com/"
# token = "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"

# # #trying to give pull_number manually using id from github/users/priyamcoding/priyam1
# pull_number = "531457965"



# # #LIST PULL REQUEST
# # '''Response code - 200 '''
# # #Syntax from documentation -/repos/{owner}/{repo}/pulls

# # def list_pulls(owner,repo):
# #     #  url = base_url + "repos/" + owner + "/" + repo + "/pulls"
# #     url = base_url + "/users/" + owner + "/" + repo + "/pulls"
# #     print(url)
# #     req = requests.get(url, auth=(token,''))
# #     #  print(req.content)
# #     return req.json()
# # print(list_pulls("priyamcoding","priyam1")) 



# # #CREATE PULL REQUEST
# # '''Response code - 422 (Invalid Request)'''
# # # /repos/{owner}/{repo}/pulls

# def post_pulls(owner,repo):
#      url = base_url + "repos/" + owner + "/" + repo + "/pulls"
#      print(url)
#      params = json.dumps({head: "main", base: "master"})
#     #  params = json.dumps({"head": "main", "base": "master"})
#      req = requests.post(url, auth= (token,'', params))

#      #tried to print req content 
#     #  print(req.content)
#      print(req.json())
#      return req.json()
#      # print("the error here is", req.text)
# print(post_pulls("priyamcoding","priyam1"))



# # # GET pull request 
# # # /repos/{owner}/{repo}/pulls/{pull_number}
# # '''getting error 404 because no pull number is generated'''
# # # def get_pulls(owner, repo, pull_number):
# # #     url = base_url + "repos/" + owner + "/" + repo + "/pulls/" + pull_number
# # # #     print(pull_number)
# # #     print(url)
# # #     # todo = 
# # #     req = requests.get(url, auth=(token,''))
# # #     print(req)
# # #     # return req.json()
# # #     return req.json()
# # # print(get_pulls("priyamcoding","priyam1", "54709332")) 


# # # #Update pull request 
# # # ''''error - 404'''
# # # # patch method
# # # # repos/{owner}/{repo}/pulls/{pull_number}
# # # def update_pulls(owner, repo, pull_number):
# # #     url = base_url + "repos/" + owner + repo + "/pulls/" + pull_number
# # #     print(url)
# # #     req = requests.patch(url, auth=(token, ''))
# # #     print(req)
# # #     return req.json()
# # # print(update_pulls("priyamcoding", "priyam1", "main"))


# # # # List commits on a pull request
# # # # /repos/{owner}/{repo}/pulls/{pull_number}/commits
# # # '''error - 404'''

# # # def get_commits(owner, repo, pull_number):
# # #     url = base_url + "repos/" + owner + repo + "/pulls/" + pull_number + "/commits"
# # #     print(url)
# # #     req = requests.get(url, auth=(token, ''))
# # #     print(req)
# # #     return req.json()
# # # print(get_commits("priyamcoding", "priyam1", "main"))
