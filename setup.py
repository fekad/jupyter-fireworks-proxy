import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-fireworks-proxy",
    version='2021.5.0',
    url="https://github.com/modl-uclouvain/jupyter-fireworks-proxy",
    author="Adam Fekete",
    description="adam@fekete.co.uk",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
	keywords=['jupyter', 'Fireworks proxy', 'jupyterhub'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=1.5.0',
	'Fireworks'
    ],
    entry_points={
        'console_scripts': [
            'fireworks_launcher=jupyter_fireworks_proxy.launcher:main'
        ],
        'jupyter_serverproxy_servers': [
            'fireworks = jupyter_fireworks_proxy:setup_fireworks_proxy',
        ]
    },
    package_data={
        'jupyter_fireworks_proxy': ['icons/fireworks.svg'],
    },
)
