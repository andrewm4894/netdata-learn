import pandas as pd
from github import Github
from creds import GH_TOKEN
from tqdm import tqdm

# github setup
g = Github(GH_TOKEN)

# point at a repo
repo = g.get_repo("netdata/netdata")

# get info on users who starred the repo
data = []
n_max = 50
n = 0
for x in tqdm(repo.get_stargazers_with_dates()):
    if n >= n_max:
        break
    data.append([x.starred_at, x.user.name, x.user.company, x.user.email, x.user.location, x.user.followers, x.user.url, x.user.bio])
    n += 1
cols = ['starred_at','name','company','email','location','followers','url','bio']
df = pd.DataFrame(data,columns=cols)

# save data
df.to_csv('../data/netdata_github_users_raw.csv',index=False)

# look at data
print(df.shape)
print(df.sample(5))



