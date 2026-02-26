import os
import git

# parameters
repo_url = 'https://your.site/user/repo'  # URL repo
local_repo_path = 'repo/dir'  # local repository path
file_name = 'dir/list.txt'  # file to read
search_string = ':1080'  # type the substring you want to search for

# git clone and update
if not os.path.exists(local_repo_path):
    print("Cloning...")
    git.Repo.clone_from(repo_url, local_repo_path)
else:
    print("Update...")
    repo = git.Repo(local_repo_path)
    repo.remotes.origin.pull()

file_path = os.path.join(local_repo_path, file_name)
first_record = None

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in reversed(lines):
            if search_string in line:
                first_record = line.strip()
                break

    if first_record:
        print(f'Return "{search_string}": {first_record}')
    else:
        print('No found')
else:
    print(f'File {file_path} no found')
