from setuptools import setup

setup(
    name="tch",
    version="1.0.1",
    py_modules=["tch"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "tch = tch.tch:cli",
        ],
    },
)
