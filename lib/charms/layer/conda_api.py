import shutil

from subprocess import call
from pathlib import Path

from charmhelpers.fetch.archiveurl import ArchiveUrlFetchHandler


CONDA_HOME = Path('/opt/conda')
CONDA_BIN = CONDA_HOME / 'bin' / 'conda'


def init_install_conda(url, checksum, hash_type):
    """Install conda

    Example Usage:

    conda_install_url =
        "https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh"

    sha256 = "7e6785caad25e33930bc03fac4994a434a21bc8401817b7efa28f53619fa9c29"

    validate = "sha256"

    init_install_conda(conda_install_url, sha256, validate)
    """

    # Download and validate conda installer
    aufh = ArchiveUrlFetchHandler()
    conda_installer_path = aufh.download_and_validate(
        url,
        checksum,
        hash_type
    )
    # If CONDA_HOME exists, remove it
    if CONDA_HOME.is_dir():
        shutil.rmtree(str(CONDA_HOME))
    # Capabilities
    CONDA_HOME.mkdir(mode=0o777, parents=True)
    # Run conda installer
    call(['bash', conda_installer_path, '-b', '-f', '-p', str(CONDA_HOME)])
    # Make sure conda base is up to date
    call([str(CONDA_BIN), 'update', '-y', '-n', 'base', 'conda'])


def create_conda_venv(env_name, python_version, packages=None):
    """Create conda venv and optionally install packages.

    Example Usage:

    create_conda_venv('jupyter', '3.5', ['jupyter', 'nb_conda'])
    """
    # Create virtualenv and install jupyter
    create_conda_venv = [str(CONDA_BIN), 'create', '-y', '-n', env_name,
                         'python={}'.format(python_version)]
    if packages:
        create_conda_venv = create_conda_venv + packages
    call(create_conda_venv)


def remove_conda_venv(env_name):
    """Remove conda venv.

    Example Usage:

    remove_conda_venv('jupyter')
    """
    # Remove conda env
    remove_conda_cmd = [str(CONDA_BIN), 'env', 'remove', '-n', env_name, '-y']
    call(remove_conda_cmd)


def install_conda_packages(env_name, conda_packages):
    """Install conda packages

    Example Usage:

    install_conda_packages(['jupyter', 'nb_conda'])
    """
    # Install conda packages
    call([str(CONDA_BIN), 'install', '-n', env_name, '-y'] + conda_packages)


def install_conda_pip_packages(env_name, conda_pip_packages):
    """Install conda pip packages

    Example Usage:

    conda_install_pip_packages(['findspark'])
    """
    CONDA_PIP_BIN = CONDA_HOME / 'envs' / env_name / 'bin' / 'pip'
    # Install conda pip packages
    call([str(CONDA_PIP_BIN), 'install'] + conda_pip_packages)
