from setuptools import setup, find_packages
from engine import __version__

with open("requirements.txt") as requirements_txt:
    requirements = requirements_txt.read().splitlines()


setup(
    name="demon3D",
    version=__version__,
    author="d3m0n@demonkingswarn",
    author_email="demonkingswarn@protonmail.com",
    description="Just a 3D cube generator.",
    packages=find_packages(),
    url="https://github.com/demonkingswarn/demon3d",
    keywords=[
        "pygame"
    ],
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        demon3d=engine.__main__:__main__
    """,
    include_package_data=True,
    )
