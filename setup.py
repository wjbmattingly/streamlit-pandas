from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

VERSION = '0.0.8'
DESCRIPTION = 'Create a Streamlit Pandas App'

setup(
    name="streamlit_pandas",
    author="WJB Mattingly",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["pandas>=1.0.0,<2.0.0"],
)
