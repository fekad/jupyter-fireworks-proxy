# jupyter-fireworks-proxy

This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fekad/jupyter-fireworks-proxy/main?urlpath=fireworks)

## Requirements

- [Python 3.6+](https://www.python.org/downloads/)
- [Jupyter Notebook 6.0+](https://pypi.org/project/notebook/)
- [JupyterLab 2.1+](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

(Optional) For testing:

- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)

This package executes the standard `fireworks` command. This command assumes the `fireworks` command is available in the environment's `PATH`. For convenience, the tests include cases that assert outputs when running the `fireworks` command from a docker container. If you don't need to run tests with this setup running in a docker container, then remove the `tests/test_fireworks_docker.py` file or comment out the code in the file.

## Quick Starts

### Launch with `binder`

This test requires you to have a database instance available as a public endpoint or installed within the notebook container itself.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/illumidesk/jupyter-fireworks-proxy/main?urlpath=fireworks)

## The Hard Way

### Create and Activate Environment

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

### Install jupyter-fireworks-proxy

```bash
pip install git+https://github.com/fekad/jupyter-fireworks-proxy.git
```

### Enable jupyter-fireworks-proxy Extensions

1. For Jupyter Classic, activate the `jupyter-server-proxy` extension:

```bash
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

2. For Jupyter Lab, install the `@jupyterlab/server-proxy` extension:

```bash
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

3. Start Jupyter Classic or Jupyter Lab

4. Click on the `fireworks` icon from the Jupyter Lab Launcher or the `fireworks` item from the `New` dropdown in Jupyter Classic.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

