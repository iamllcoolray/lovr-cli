from setuptools import setup, find_packages # type: ignore

setup(
    name="lovr",
    version="0.1",
    description="Lovr is a command line interface that manages LÖVE2D projects",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Nobunaga",
    author_email="iamllcoolray@gmail.com",
    url="https://github.com/iamllcoolray/lovr-cli",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "lovr=src.main:main",
        ],
    },
)