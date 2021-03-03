from setuptools import setup

setup(
    name="peing-dl",
    version="0.1",
    install_requires=["requests", "pandas"],
    entry_points={"console_scripts": ["peing-dl = peing:main"]},
    author="5h4ru",
)
