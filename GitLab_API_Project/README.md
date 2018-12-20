## Problem

In the development process, we (the team) currently lack a process of automatically migrating changes made in the extract reports from GitLab to the windows server that the Python Framework sits on. The current process requires an individual to push/merge the code and then manually copy the code over to the server.


## Objective

•	Reduce error: Individuals may make mistakes when they manually copy and paste the code, and an automatic continuous deployment will help prevent error.

•	Reduce time: Individuals will require access to the server to move the code, and it will take time to verify where to appropriately move it.

•	Provide consistency: Consistency provided by continuous deployment means low margin of error, high efficiency, and allows for the focus or other priorities.

•	Provide insight: In the scenario an issue arrives, it will be easier track down errors and the source of the problem.


## Context

•	As a developer, I want to eliminate the manual process of moving changes made on GitLab to the server.

•	As an analyst, I want to make changes to the extracts and reports without to make changes in Git and the server.

•	As a manager, I want to eliminate the need to grant individuals access as changes occur, or train existing and new hires to work on manual processes.


## Prototype

The prototype takes extracts that have made commits in the last five minutes and proceeds to copy their content and write it to a specific location and file. The prototype currently written is designed around constraints provided by GitLab’s API:
1.	Commits are uniquely identified by “id” and the commit id is different than that of the actual extract.
2.	To find out which commit id belongs to which extract, one will need to investigate the details of the file API – which provides “last_commit_id”.
3.	The file API requires a file_path parameter that can only be obtained through navigating the repository tree API recursively. 
4.	The file_path parameter is obtained by returning all existing .sql files within the repository tree and then accessing specific .sql files through the API. 

###### GitLab API References
• [Commits](https://docs.gitlab.com/ee/api/commits.html#list-repository-commits)

• [Repository Files](https://docs.gitlab.com/ee/api/repository_files.html)

• [Repositories](https://docs.gitlab.com/ee/api/repositories.html)



## Design

1.	The script starts by calling the _get_file_path() function which  returns all of the directory information within the project. We proceed to gather of all the paths and combine them with a new call to retrieve specific information within the paths. 

2.	Function _get_sql_files() takes the returned URLs from _get_file_path() and looks for all sql files within the file path and returns them all in a list/array.

3.	Function _get_sql_content() looks through the files and checks if the last_commit_id exists in the _get_commit_id()* function and if it does, it will execute _retrieve_write() to retrieve the query and write it out to a specific location.


*  _get_commit_id() is a function that retrieves all commits made today and calls _is_recent() to check if they have been committed within the last five minutes.
