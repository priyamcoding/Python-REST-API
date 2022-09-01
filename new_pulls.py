import requests
import json

base_url = "https://api.github.com/"
token = "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"

#tried to pass pull_number as priyam1 (repo) id 
pull_number = "531457965"

#LIST PULL REQUEST
# /repos/{owner}/{repo}/pulls
def list_pulls(owner,repo):
     url = base_url + "repos/" + owner + "/" + repo + "/pulls"
     print(url)
     req = requests.get(url, auth=(token,''))

#tried to print req.content - but it gaven an error
# print(req.content)

     print(req)
     return req.json()
print(list_pulls("priyamcoding","priyam1")) 

#CREATE PULL REQUEST
# POST
# /repos/{owner}/{repo}/pulls
def post_pulls(owner,repo):
    url = base_url + "repos/" + owner + "/" + repo + "/pulls"
    print(url)
    req = requests.post(url, auth=(token,''))

    print(req)
        #  tried to print req.headers - it is working properly;
        #  which means the right info is being accessed.
        #  print(req.headers)
    return req.json()
print(post_pulls("priyamcoding","priyam1"))

# GET
# /repos/{owner}/{repo}/pulls/{pull_number}
def get_pulls(owner,repo,pull_number):
    url = base_url + "repos/" + owner + "/" + repo + "/pulls/" + pull_number
    print(url)
    req = requests.get(url, auth=(token,''))
    print(req)
    return req.json()
print(get_pulls("priyamcoding","priyam1", pull_number)) 


#Update pull request 

# repos/{owner}/{repo}/pulls/{pull_number}

def update_pulls(owner, repo, pull_number):
    url = base_url + "repos/" + owner + repo + "/pulls/" + pull_number
    print(url)
    req = requests.patch(url, auth=(token, ''))
    print(req)
    return req.json()
print(update_pulls("priyamcoding", "priyam1", pull_number))


# # List commits on a pull request
# # /repos/{owner}/{repo}/pulls/{pull_number}/commits
'''error - 404'''

def get_commits(owner, repo, pull_number):
    url = base_url + "repos/" + owner + repo + "/pulls/" + pull_number + "/commits"
    print(url)
    req = requests.get(url, auth=(token, ''))
    print(req)
    return req.json()
print(get_commits("priyamcoding", "priyam1", pull_number))

# List pull requests files
# get/repos/{owner}/{repo}/pulls/{pull_number}/files

def pull_request_files(owner, repo, pull_number):
    url = base_url + "repos/" + owner + "/pulls/"+ pull_number + "/files"
    print(url)
    req = requests.get(url, auth=(token, ''))
    print(req)
    return req.json()
print(pull_request_files("priyamcoding", "priyam1", pull_number))