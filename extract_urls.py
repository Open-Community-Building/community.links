import json
import spacy
from spacy_layout import spaCyLayout
from pathlib import Path
from config import GITHUB_FOLDER
from config import CHECK_ARCHIVE
from config import on_archive_list
from config import not_on_archive_list
from config import do_not_put_on_archives_list


def run():
    nlp = spacy.blank("en")
    layout = spaCyLayout(nlp)

    urls = []

    gh_repos = json.loads(open(GITHUB_FOLDER, "r").read())

    for repository in gh_repos['git repositories']:
        counter = 0
        print(repository['local_folder'])
        for path in Path(repository['local_folder']).rglob('*.md'):
            # Process a document and create a spaCy Doc object
            doc_layout = layout(path)
            doc_nlp = nlp(doc_layout)
            url_list=[token.text for token in doc_nlp if token.like_url]
            for url in url_list:
                url = url.strip()
                if url in on_archive_list:
                    continue
                elif url in not_on_archive_list:
                    continue
                elif url in do_not_put_on_archives_list:
                    continue
                if url in urls:
                    continue
                urls.append(url)
                counter += 1
        print(counter)

    urls.sort()

    with open(CHECK_ARCHIVE, 'w') as check_archive_file:
        check_archive_file.write('\n'.join(urls))

# Example usage
if __name__ == "__main__":
    run()

