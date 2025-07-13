# community.links

Make sure that links in your git repositories are archived on archive.org.

## Update git repositories

Look in the github.json config file for all Github repositories, and pull them.

    python git_pull.py      

## Extract urls from github repos

Go though all .md files in your the repositories, usung spaCy to check what looks like an URL.

    python extract_urls.py

## Check availability on archive.org

Check whether the urls are already available on archive.org

    python check_archive_org.py

## Save to archive.org

When a URL is not on archive.org, save it to archive.org

    python save_to_archive.py

## Fetch html from archive.org

Once everything is on archive.org, fetch the HTML from there

    python internet_archive.py

## Produce Markdown from html

Now produce the Markdown from the HTML using docling

    python docling_from_ia.py
