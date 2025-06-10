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
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
    keywords="linear algebra, matrix, multiplication, mathematics",
    project_urls={
        "Bug Reports": "https://github.com/group13/group13-matrix-operations-2025/issues",
        "Source": "https://github.com/group13/group13-matrix-operations-2025",
    },
    license_files=["LICENSE"],  # Updated format
)