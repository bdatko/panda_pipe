import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

setup(
    name="pandas_pipe",
    version="0.0.0",
    description="routine pandas method chain links wrapped with scikit-lego",
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    url="https://github.com/bdatko/panda_pipe",
    author="Benjamin Datko",
    author_email="ben.datko@gmail.com",
    license="MIT",
    packages=["pandas_pipe"],
    install_requires=["numpy", "pandas>=1.1.5", "scikit-lego>=0.6.1"],
)
