# layer-conda-api

Conda API

## Usage
The 'conda-api' exposes a few choice functionalities to charm authors.

Include this layer in your charm, then import `from charms.layer import conda_api` to access the helper functions.

```python
init_install_conda()
```
Installs a conda environment to `/opt/anaconda`.

```python
create_conda_venv()
```
Creates a conda venv named 'juju'.

```python
install_conda_packages()
```
Installs a list of conda packages.

```python
install_conda_pip_packages()
```
Installs a list of pip packages into your conda environment.


### License
* AGPLv3 (see `copyright` file)

### Copyright
* James Beedy (c) 2018 <jamesbeedy@gmail.com>
