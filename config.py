import os

BASE_FOLDER = os.environ.get('COMMUNITY_LINKS_BASE_FOLDER'))

DATA_FOLDER = BASE_FOLDER + "data/"
CONFIG_FOLDER = BASE_FOLDER + "config/"
HTML_FOLDER = BASE_FOLDER + "html/"
MARKDOWN_FOLDER = BASE_FOLDER + "markdown/"
CHECK_ARCHIVE = DATA_FOLDER + "check_archive.org.md"
ON_ARCHIVE = DATA_FOLDER + "on_archive.org.md"
NOT_ON_ARCHIVE = DATA_FOLDER + "not_on_archive.org.md"
DO_NOT_PUT_ON_ARCHIVE = DATA_FOLDER + "do_not_put_on_archive.md"
GITHUB_FOLDER = CONFIG_FOLDER + "github.json"

check_archive_list = [line.strip() for line in open(CHECK_ARCHIVE).readlines()]
on_archive_list = [line.strip() for line in open(ON_ARCHIVE).readlines()]
not_on_archive_list = [line.strip() for line in open(NOT_ON_ARCHIVE).readlines()]
do_not_put_on_archives_list = [line.strip() for line in open(DO_NOT_PUT_ON_ARCHIVE).readlines()]
