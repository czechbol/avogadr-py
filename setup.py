import setuptools
import os


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    entry_points={
        "console_scripts": ["avogadr-py=avogadr_py.__main__:cli"],
    },
    name="avogadr_py",
    version=get_version("src/avogadr_py/__init__.py"),
    author="Adam Ludes",
    author_email="adam@ludes.cz",
    description="Simple avogadr.io batch downloader python script.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/czechbol/avogadr-py",
    project_urls={
        "Bug Tracker": "https://github.com/czechbol/avogadr-py/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=["aiofiles>=0.8,<1", "aiohttp>=3.8,<4"],
)
