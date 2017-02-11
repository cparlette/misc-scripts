## This python script will search Github for all open pull requests
## related to AngularJS.  Specifically, it will search for "angular",
## but only for open pull requests using JavaScript. It will output
## a list including the title and link to the pull request.

## To generate a text file, run:
## python search_github.py > search_github_results.txt

## This script requires the requests library
## See http://docs.python-requests.org/en/master/ for installation
import requests

## Define search parameters
# Search terms
search = "angular"
# Issue type (either issue or pr)
issue_type = "pr"
# Issue state (either open or closed)
state = "open"
# Language for the issue
language = "JavaScript"

## Build the search query and get the results
url = "https://api.github.com/search/issues?"
url += "l=" + language
url += "&q=" + search
url += "&state=" + state
url += "&type=" + issue_type

search_results = requests.get(url)

## Get JSON
results_json = search_results.json()

## Iterate the results and print in a nice format
for result in results_json["items"]:
	print result["title"]
	print result["url"]
	print
