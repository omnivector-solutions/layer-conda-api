import shutil

from subprocess import call
from pathlib import Path

from charmhelpers.core.host import chownr
from charmhelpers.fetch.archiveurl import ArchiveUrlFetchHandler


CONDA_HOME = Path('/opt/anaconda')
CONDA_BIN = CONDA_HOME / 'bin' / 'conda'
CONDA_PIP_BIN = CONDA_BIN / 'envs' / 'juju' / 'bin' / 'pip'


def init_install_conda(url, sha, validate):
    """Install conda
    """

    aufh = ArchiveUrlFetchHandler()
    conda_installer_path = aufh.download_and_validate(
        url,
        sha,
        validate=validate
    )

    if CONDA_HOME.is_dir():
        shutil.rmtree(str(CONDA_HOME))

    CONDA_HOME.mkdir(mode=0o777, parents=True)

    # Run conda installer
    call(['bash', conda_installer_path, '-b', '-f', '-p', str(CONDA_HOME)])

    # Make sure conda base is up to date
    call([str(CONDA_BIN), 'update', '-y', '-n', 'base', 'conda'])


def create_conda_venv(python_version, packages=None):
    """Create conda venv and optionally install packages.

    This can only be called one time.

    Example Usage:

    create_conda_venv('jupyter', '3.5', ['jupyter', 'nb_conda'])
    """
    # Create virtualenv and install jupyter
    create_conda_venv = [str(CONDA_BIN), 'create', '-y', '-n', 'juju',
                         'python={}'.format(python_version)]
    if packages:
        create_conda_venv = create_conda_venv + packages

    call(create_conda_venv)


def install_conda_packages(conda_packages):
    """Install conda packages

    Example Usage:

    install_conda_packages(['jupyter', 'nb_conda'])
    """
    # Install conda packages
    call([str(CONDA_BIN), 'install', '-y'] + conda_packages)


def install_conda_pip_packages(conda_pip_packages):
    """Install conda pip packages

    Example Usage:

    conda_install_pip_packages(['findspark'])
    """
    # Install conda pip packages
    call([str(CONDA_PIP_BIN), 'install', '-y'] + conda_pip_packages)
