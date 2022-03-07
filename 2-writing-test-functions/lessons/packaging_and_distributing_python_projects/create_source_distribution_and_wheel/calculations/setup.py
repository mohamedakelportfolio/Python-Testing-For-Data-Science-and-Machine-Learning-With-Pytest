from setuptools import setup, find_packages

setup(
    name='simple_math',
    description="This package do simple math calculation",
    version="1.0",
    author = "mohamed akel",
    author_email="mohamed@daily_datum.edu",
    url="https://any_url.com",
    packages=find_packages(where='src'),
    package_dir={'':'src'}
)