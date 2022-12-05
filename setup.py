from setuptools import setup, find_packages


VERSION = '0.0.3'
DESCRIPTION = 'Create a Streamlit Pandas App'

setup(
    name="streamlit_pandas",
    author="WJB Mattingly",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["pandas>=1.0.0,<2.0.0"],
)
