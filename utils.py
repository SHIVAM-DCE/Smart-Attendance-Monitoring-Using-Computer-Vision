import os
import sys


def resource_path(relative_path):
    """Get the absolute path to a resource, working for PyInstaller and normal execution."""
    base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(base_path, os.path.normpath(relative_path))
