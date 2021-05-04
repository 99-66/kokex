import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kokex",
    version="0.0.2",
    author="jsmyung",
    author_email="jsmyung@datansoft.com",
    description="A Korean Keywords Extractor with Syntactic Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsmyung-datansoft/kokex",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'konlpy>=0.5.2',
        'networkx>=2.5.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
