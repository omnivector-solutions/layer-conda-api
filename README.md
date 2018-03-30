# layer-conda-api

Conda API

## Usage
The 'conda-api' exposes a few choice functionalities to charm authors.

Include this layer in your charm, then import `from charms.layer import conda_api` to access the helper functions.

```python
init_install_conda(url, sha, validate)
```
Installs a conda environment to `/opt/anaconda`.

##### Example Usage:
```python
conda_install_url =
    "https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh"

sha256 = "7e6785caad25e33930bc03fac4994a434a21bc8401817b7efa28f53619fa9c29"

validate = "sha256"

init_install_conda(conda_install_url, sha256, validate)
```

```python
create_conda_venv(python_version, packages=None)
```
Create conda venv and optionally install packages.

##### Example Usage:
```python
create_conda_venv('3.5', ['jupyter', 'nb_conda'])
```

```python
install_conda_packages(conda_packages)
```
Install conda packages.

##### Example Usage:
```python
install_conda_packages(['jupyter', 'nb_conda'])
```

```python
install_conda_pip_packages(conda_pip_packages)
```
Installs a list of pip packages into your conda environment.

##### Example Usage:
```python
install_conda_pip_packages(['findspark'])
```

### License
* AGPLv3 (see `copyright` file)

### Copyright
* James Beedy (c) 2018 <jamesbeedy@gmail.com>
