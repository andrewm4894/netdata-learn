import pandas as pd
from github import Github
from creds import GH_TOKEN
from tqdm import tqdm
import time
import csv

# github setup
g = Github(GH_TOKEN)

# point at a repo
repo = g.get_repo("netdata/netdata")

# get num pages
page_len = len(repo.get_stargazers_with_dates().get_page(1))
num_stargazers = repo.get_stargazers().totalCount
num_pages = (num_stargazers // page_len) + 2

# list to collect data into
rownum = 0

# get latest page
latest_page_file = '/home/andrewm4894/netdata-learn/scripts/latest_page.txt'
with open(latest_page_file, "r") as f:
    latest_page = f.read()
latest_page = int(latest_page)
print(f'... latest_page is {latest_page} ...')

# loop over pages
for p in range(latest_page,num_pages):
    if p % 10 == 0:
        print(f'... page {p} of {num_pages} ({round(p/num_pages,4)}%) ...')
    if (rownum > 1) & (rownum % 1000 == 0):
        print(f'... row {rownum} of {num_stargazers} ({round(rownum/num_stargazers,4)}%) ...')
    stargazers = repo.get_stargazers_with_dates().get_page(p)
    for stargazer in stargazers:
        row = [
            stargazer.starred_at.strftime("%Y-%m-%d %H:%M:%S"), stargazer.user.name, stargazer.user.company, 
            stargazer.user.email, stargazer.user.location, stargazer.user.followers,
            stargazer.user.following, stargazer.user.url, stargazer.user.bio,
            stargazer.user.public_repos, stargazer.user.public_gists, stargazer.user.blog,
            stargazer.user.created_at.strftime("%Y-%m-%d %H:%M:%S"), stargazer.user.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        ]
        row = [str(x).replace(',',' ') for x in row]
        row = [f'"{x}"' for x in row]
        #row = ','.join(row)
        with open('/home/andrewm4894/netdata-learn/data/netdata_gh_data_raw.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        rownum += 1
    # write out latest page
    with open(latest_page_file, "w") as f:
        f.write(str(p))