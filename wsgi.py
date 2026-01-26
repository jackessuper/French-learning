"""
WSGI entry point for French Learning App
=========================================
Used by production servers like gunicorn and PythonAnywhere.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from web.app import app as application

# For gunicorn compatibility
app = application

if __name__ == '__main__':
    application.run()
