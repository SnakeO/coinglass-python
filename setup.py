"""
Setup configuration for CoinGlass Python library
"""
from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="coinglass",
    version="1.0.0",
    author="CoinGlass Python",
    author_email="",
    description="A comprehensive Python library for the CoinGlass API v4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/coinglass-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial :: Investment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "pytest-asyncio>=0.18.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
            "sphinx>=4.5.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
        "async": [
            "aiohttp>=3.8.0",
        ],
    },
    keywords="coinglass cryptocurrency trading futures options api bitcoin ethereum crypto derivatives",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/coinglass-python/issues",
        "Source": "https://github.com/yourusername/coinglass-python",
        "Documentation": "https://github.com/yourusername/coinglass-python/blob/main/README.md",
    },
)