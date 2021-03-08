from setuptools import setup

setup(
    name="pandas_pipe",
    version="0.0.0",
    description="routine pandas method chain links wrapped with scikit-lego",
    author="Benjamin Datko",
    author_email="ben.datko@gmail.com",
    license="MIT",
    packages=["pandas_pipe"],
    install_requires=["numpy", "pandas>=1.1.5", "scikit-lego>=0.6.1"],
)
