from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Evil-Balaji",
    version="0.1",
    author="hitbug-exe",
    description="We know what we are, but know not what we may be.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hitbug-exe/Evil-Balaji",
    packages=["Evil-Balaji"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "markovify",
        "spacy",
        "nltk"
    ],
)
