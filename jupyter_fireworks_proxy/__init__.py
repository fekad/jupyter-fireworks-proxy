import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel('INFO')


def setup_fireworks_proxy():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """
    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'icons', 'rocket.svg'
    )

    # Make sure executable is in $PATH
    def _get_command(port):
        executable = shutil.which('lpad')
        if not executable:
            raise FileNotFoundError('Can not find lpad executable in $PATH')

        logger.info(f"Fireworks command @ port:{port}")
        return ['lpad', 'webgui', '-s', '--port', str(port)]

    return {
        'command': _get_command,
        'port': 5000,
        'new_browser_tab': False,
        'launcher_entry': {
            'title': 'Fireworks webgui',
            'icon_path': _get_icon_path()
        },
    }
