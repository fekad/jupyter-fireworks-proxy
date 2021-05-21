# jupyter-fireworks-proxy

This package provides an easy way to launch the webgui interface of Fireworks in a Jupyter notebook environment. The Fireworks package must be fully configured with a config file stored at the `~/.fireworks/my_launchpad.yaml` location.


## Requirements

- [Python 3+](https://www.python.org/downloads/)
- [Jupyter Notebook](https://pypi.org/project/notebook/)
- [Fireworks](https://github.com/materialsproject/fireworks)


This package also contains a `fireworks_luancher` command which is also used internally to initialise a single-threaded interface for the webgui implementation of Fireworks. 

## Quick Starts

### Install jupyter-fireworks-proxy

```bash
pip install git+https://github.com/modl-uclouvain/jupyter-fireworks-proxy.git
```

### Enable jupyter-fireworks-proxy Extensions

Note: These steps might be optional, depending on the python environment that you use.

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

4. Click on the `Fireworks (webgui)` icon from the Jupyter Lab Launcher or the `Fireworks (webgui)` item from the `New` dropdown in Jupyter Classic.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)
- [`jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).
