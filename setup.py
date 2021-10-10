import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="liaison",
    packages=["liaison"],
    author="Julian Nash",
    version="0.1",
    description="Liaison is a Python library for defining schemas, parsing and validating payloads",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="python schema parser",
    url="https://github.com/Julian-Nash/liaison",
    project_urls={
        "Bug Tracker": "https://github.com/Julian-Nash/liaison",
        "Documentation": "https://github.com/Julian-Nash/liaison",
        "Source Code": "https://github.com/Julian-Nash/liaison",
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    extras_require={
        "dev": ["pytest", "black", "coverage"],
        "test": ["pytest", "coverage"],
    }
)