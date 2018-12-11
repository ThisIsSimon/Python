# A simple proof of concept script that accesses the GitLab API and returns the latest commit
# and checks if the commit has been made on the same day and within the last 5 minutes

import requests
from datetime import datetime as dt, timedelta
import urllib
import sys


def _valid_200response(path):
    # Checks if the given path is valid and returns the JSON data in a dictionary
    request = requests.get(path)
    if request.status_code == requests.codes.ok:
        return request.json()
    else:
        sys.exit(request.raise_for_status())


def _get_commit_id():
    # Get commits from ONLY today
    time_minus_five = dt.now() - timedelta(minutes=5)
    current_date = dt.now().isoformat()
    commit_path = "https://gitlab.com/api/v4/projects/%s/repository/commits?private_token=%s&ref_name=%s&since=%s" % (project_id, private_token, branch, current_date)
                    (project_id, private_token, branch)
    # Get the commit_id data
    commit_path = _valid_200response(commit_path)
    commit_id = []
    for ids in commit_path:
        # Check if the committed_date was within the last 5 minutes
        if time_minus_five.isoformat() < ids['committed_date'] < dt.now().isoformat():
            commit_id.append(ids['id'])

    return commit_id

def _is_recent(datetime_parameter, path):
    # Determine if the given datetime parameter happened today within the last five minutes
    time_minus_five = dt.datetime.now() - dt.timedelta(minutes=5)

    if (
        str(dt.datetime.now().date()) == datetime_parameter['date'] and
        time_minus_five.time().isoformat('seconds') < datetime_parameter['time'] < dt.datetime.now().time().isoformat('seconds')
       ):
        # Runs the function to retrieve the SQL text and writes it
        print('do something')
    else:
        print('Commit not within the last five minutes')


def _get_file_path():
    # URL to get all existing paths within the project
    repo_path = "https://gitlab.com/api/v4/projects/%s/repository/tree?private_token=%s&ref=%s&recursive=True" % \
                      (project_id, private_token, branch)
    # Get JSON data
    repo_path = _valid_200response(repo_path)
    # Get all individual file paths
    paths = []
    for path in repo_path:
        paths.append(path['path'])

    # Combine the repositories with the URL path
    for file in range(len(paths)):
        # Encode the URL paths as required by GitLab's API
        # By default .quote does not encode '/', which is required by GitLab and solved by the safe parameter
        # .quote_plus is not used because it encodes spaces as + instead of %20
        encoded_path = urllib.parse.quote(paths[file], safe="%2f")
        paths[file] = "https://gitlab.com/api/v4/projects/%s/repository/tree?private_token=%s&ref=%s&path=%s" % \
                      (project_id, private_token, branch, encoded_path)

    return paths


def _get_sql_files(url_paths):
    # Within each file path, look for the .sql files
    sql_file_paths = []
    for paths in url_paths:
        # For each url in the lists, valid response and get JSON data
        path = _valid_200response(paths)
        for file in path:
            # For given JSON data, look for .sql file
            if ".sql" in file['name']:
                sql_file_paths.append(file['path'])

    return sql_file_paths


def _get_sql_content(sql_url):
    for content in sql_url:
        # HTML URL Encoding required by GitLab
        encoded_path = urllib.parse.quote(content, safe="%2f")
        file_content_path = "https://gitlab.com/api/v4/projects/%s/repository/files/%s?private_token=%s&ref=%s" % \
                            (project_id, encoded_path, private_token, branch)
        # Get JSON data about files
        file_content_path = _valid_200response(file_content_path)
        if file_content_path['last_commit_id'] in _get_commit_id():
            # If the last_commit_id exist in this files commit_ids go through the process of _retrieve_write
            # print(file_content_path['file_name'])
            _retrieve_write(file_content_path['file_path'])


def _retrieve_write(file_path):
    # The function takes raw content of the given file path and proceeds to write it somewhere
    path = "https://gitlab.com/api/v4/projects/%s/repository/files/%s/raw?private_token=%s&ref=%s" % \
           (project_id, file_path, private_token, branch)
    # Request the query in text form
    get_query = requests.get(path, stream=True).text
    # Write the file - currently it is using "w" for overwrite
    file = open(r"C:/Users/Path", "w")
    file.write(get_query)


project_id = 1234
branch = "foo"
private_token = "your_token"

# Get all repository API paths
file_url = _get_file_path()

# Get .sql files out of each given path
sql_files = _get_sql_files(file_url)

#
_get_sql_content(sql_files)
