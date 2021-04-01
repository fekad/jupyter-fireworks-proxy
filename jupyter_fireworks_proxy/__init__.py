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

        # # Create theia working directory
        # home_dir = os.environ.get('HOME') or '/home/jovyan'
        # working_dir = f'{home_dir}/fireworks'
        # if not os.path.exists(working_dir):
        #     os.makedirs(working_dir)
        #     logger.info("Created directory %s" % working_dir)
        # else:
        #     logger.info("Directory %s already exists" % working_dir)

        return ['lpad webgui --host "0.0.0.0"']

    return {
        'command': '_get_command',
        'timeout': 20,
        'new_browser_tab': False,
        'launcher_entry': {
            'title': 'Fireworks proxy',
            'icon_path': _get_icon_path()
        },
    }
