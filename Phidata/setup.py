# A minimal setup.py file for supporting editable installs

from setuptools import setup


"""
how to make utils folder in public python package
"""

from setuptools import setup

setup(
    name="Phidata-Learning",
    version="0.1",
    packages=["utils"],
    entry_points={
        "console_scripts": [
            "env=utils.llm_environment:multi_main",
        ],
    },
)