import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]



setuptools.setup(
    name="lin_class_simncg",
    version="0.0.2",
    author="Simón Caicedo",
    author_email="simncg@gmail.com",
    description="Package for solving linear classification project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = get_requirements()
)