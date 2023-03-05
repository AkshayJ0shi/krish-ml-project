from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the listt of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements

setup(
    name="krish-ml-project",
    description="This is an end-to-end ml project",
    author="akshay joshi",
    author_email="akshayjoshi1117@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)