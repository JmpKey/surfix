import os
import shutil
import git
import argparse

# args
def parse_arguments():
    parser = argparse.ArgumentParser(description='Search for a substring in a file from a Git repo.')
    parser.add_argument('-r', '--repo', required=True, help='URL repo')
    parser.add_argument('-f', '--file', required=True, help='Path to the file to read relative to the repo')
    parser.add_argument('-s', '--search', required=True, help='Substring to search for')
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # param
    repo_url = args.repo  # URL repo
    local_repo_path = 'repo/dir'  # local repository path
    file_name = args.file  # file read
    search_string = args.search  # substring for search

    # clear dir
    if os.path.exists(local_repo_path):
        print(f"Removing existing directory: {local_repo_path}")
        shutil.rmtree(local_repo_path)

    # clone
    print("Cloning...")
    git.Repo.clone_from(repo_url, local_repo_path)

    file_path = os.path.join(local_repo_path, file_name)

    if os.path.exists(file_path):
        found_records = []
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line in reversed(lines):
                if search_string in line:
                    found_records.append(line.strip())

        if found_records:
            print(f'Found occurrences of "{search_string}":')
            for record in found_records:
                print(record)
        else:
            print('No occurrences found')
    else:
        print(f'File {file_path} not found')

if __name__ == '__main__':
    main()
