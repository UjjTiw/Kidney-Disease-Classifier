import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classifier"
AUTHOR_USER_NAME = "UjjTiw"
SRC_REPO = "Kidney-Disease-Classifier"
AUTHOR_EMAIL = "ujjwaltiwari2004razor@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for classifying kidney disease based on the CT scan images",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "BUG Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

# for creating environment `conda create -n python=3.9 -y` 