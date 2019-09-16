# netdata-learn

Repo for playing around with Netdata.

## conda env

create conda env like below:
```
conda create -n netdata-learn python=3.6 numpy pandas requests jupyterlab matplotlib pytest scikit-multiflow
```

## packages

To add custom dev package to the conda env run this (note requires install conda-build `conda install --quiet --yes conda-build`):
```
conda develop -n netdata-learn ~/netdata-learn/packages/netdata_api_utils
```

## launch jupyter

Activate conda env:
```
conda activate netdata-learn
```

Launch jupyter (this assumes you are remote accessing into the jupyter lab otherwise just run `jupyter lab`):
```
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser 
```

