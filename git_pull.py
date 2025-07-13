import git
import json
from config import GITHUB_FOLDER
import logging

logger = logging.getLogger('mcp-archive-org')


def run():
    gh_repos = json.loads(open(GITHUB_FOLDER, "r").read())
    for gh_repo in gh_repos['git repositories']:
        local_folder = gh_repo['local_folder']
        repo = git.Git(local_folder)
        print(local_folder)
        try:
            repo.pull()
        except Exception as e:
            logger.error("Git pull error: %s", e, exc_info=1)

# Example usage
if __name__ == "__main__":
    run()

