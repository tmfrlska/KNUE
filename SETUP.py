from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("VERSION", "r") as f:
    version = f.read().strip()


setup(
    name="edudata4ai",
    version=version,
    author="Seulki.Kim",
    author_email="tmfrlska85@gmail.com",
    description="KNUE_TEST",
    url="https://github.com/tmfrlska/KNUE",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
