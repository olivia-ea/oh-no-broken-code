import json

def github_api_response():  # string to dictionary
    with open('github.json') as f:
        github_response = json.loads(f.read())
    return github_response

def print_user_repository_names(api_response):
    for item in api_response:
        if item['description'] == "":
            print(f"{item['name']}")
        else:
            print(f"{item['name']}: {item['description']}")



if __name__=="__main__":
    github_response = github_api_response()
    print_user_repository_names(github_response)