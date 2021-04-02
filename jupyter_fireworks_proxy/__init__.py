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
            os.path.dirname(os.path.abspath(__file__)), 'icons', 'fireworks.svg'
    )

    def _get_command(port, base_url):
        executable = shutil.which('lpad')
        if not executable:
            raise FileNotFoundError('Can not find lpad executable in $PATH')

        logger.info(f"Fireworks command @ port: {port}, base_url: {base_url}")
        return ['fireworks_launcher', '--port', str(port), '--base_url', base_url + 'fireworks']

    def _get_env(port, base_url):
        return {}


    return {
        'command': _get_command,
        'environment': _get_env,
        'absolute_url': True,
        # 'port': 5000,
        # 'timeout': 20,
        'new_browser_tab': True,
        'launcher_entry': {
            'title': 'Fireworks (webgui)',
            'icon_path': _get_icon_path()
        },
    }
