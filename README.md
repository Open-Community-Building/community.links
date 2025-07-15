# community.links

Make sure that links in your git repositories are archived on archive.org.

Configure a base folder like this:

    export COMMUNITY_LINKS_BASE_FOLDER=/Users/maik/Writing/maikroeder/mcps-mkrdr/1/

Activate

    cd /Users/maik/Code/mcps
    source bin/activate

Install for development

    cd /Users/maik/Code/community.links/
    pip install --editable .

Prepare a data folder

    cd $COMMUNITY_LINKS_BASE_FOLDER
    mkdir config
    mkdir data
    mkdir html
    mkdir markdown    

In that folder, there needs to be a data folder:

    ├── config
    │   └── github.json
    ├── data
    │   ├── check_archive.org.md
    │   ├── do_not_put_on_archive.md
    │   ├── not_on_archive.org.md
    │   ├── on_archive.org.md
    │   └── on_archive.org.txt
    ├── html
    └── markdown

Put a github.json file into the config folder:

    config/github.json
    
It is a JSON file with the github repositories to watch for links:

    {
        "git repositories": [
        {
           "url": "maikroeder/openheidelberg",
           "local_folder": "/Users/maik/Writing/maikroeder/openheidelberg"
        },
        ...
    }

In the above example, this 
    
    /Users/maik/Writing/maikroeder/openheidelberg

is one of the github repositories you want to fetch urls from.

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
