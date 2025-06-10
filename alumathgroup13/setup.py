from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="group13-matrix-operations-2025",
    version="1.0.1",
    author="Group13",
    author_email="group13@example.com",
    description="Advanced Linear Algebra Matrix Operations for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/group13/group13-matrix-operations-2025",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[],
)