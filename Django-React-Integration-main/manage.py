#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess     
# from django.conf import settings

def main():
    """Run administrative tasks."""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connect.settings')
    from django.conf import settings
    if settings.DEBUG and 'runserver' in sys.argv:
        process2 = subprocess.Popen(['npm', 'run', 'dev'],cwd=os.getcwd()+'/frontend')
    # elif 'runserver' in sys.argv:
        # process2 = subprocess.Popen(['npm', 'run', 'build'],cwd=os.getcwd()+'/frontend')
        # process2_1 = subprocess.Popen(['python3', 'manage.py', 'collectstatic'],cwd=os.getcwd())
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
