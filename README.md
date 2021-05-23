# jupyter-fireworks-proxy

This package provides an easy way to launch the [webgui](https://materialsproject.github.io/fireworks/basesite_tutorial.html) interface of [Fireworks](https://materialsproject.github.io/fireworks/) in a Jupyter notebook environment. Please note that the Fireworks python must be fully configured.


## Requirements

- [Python 3+](https://www.python.org/downloads/)
- [Jupyter Notebook](https://pypi.org/project/notebook/)
- [Fireworks](https://github.com/materialsproject/fireworks)


This package also contains a `fireworks_luancher` command which is also used internally to initialise a single-threaded interface for the webgui implementation of Fireworks. 

## Quick Starts

1. Use `pip` to install jupyter-fireworks-proxy:
```bash
pip install jupyter-fireworks-proxy
```

2. Start Jupyter Classic or Jupyter Lab

3. Click on the `Fireworks (webgui)` icon from the Jupyter Lab Launcher or the `Fireworks (webgui)` item from the `New` dropdown in Jupyter Classic.


### Install jupyter-fireworks-proxy from gihub source

Note: These steps might be optional, depending on the python environment that you use.

1. Use `pip` to install jupyter-fireworks-proxy:
```bash
pip install git+https://github.com/modl-uclouvain/jupyter-fireworks-proxy.git
```

2. For Jupyter Classic, activate the `jupyter-server-proxy` extension:

```bash
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

3. For Jupyter Lab, install the `@jupyterlab/server-proxy` extension:

```bash
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

4. Start Jupyter Classic or Jupyter Lab

5. Click on the `Fireworks (webgui)` icon from the Jupyter Lab Launcher or the `Fireworks (webgui)` item from the `New` dropdown in Jupyter Classic.

## Useful links:

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)
- [`jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).
