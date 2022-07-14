from distutils.core import setup
import py2app, glob
import pygame
from build_win import Build

pygame_path = os.path.dirname(pygame.__file__)
icns_path = os.path.join(pygame.__file__, "pygame_icon.icns")

setup(
    name="NovelPy Mac Test",
    version="Dependencies"
    app = [ "main.py" ],
    data_files = [
        ("data", glob.glob("data/*")),
        ("", [ "main.py" ] + [ "build_mac.py" ])
        ],
    options = {
        "py2app": {
            "excludes": [ 'pip', 'setuptools', 'easy_install', 'altgraph', 'opencv-python', 'Cython', 'cython', 'graphviz' ],
            "argv_emulation" : True,
            "semi_standalone" : True,
            "site_packages" : True,
            "iconfile": icns_path
            }
        }
    )

build = Build()
build.build_zip()

