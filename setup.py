from setuptools import find_packages, setup 
from typing import List


def get_requirements(file_path:str) ->List[str]:
    """
    this function will return list of requirements
    """

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","")for req in requirements]


    return requirements


     
setup(
name = "ml_project",
version = "0.0.1",
author = "fahad",
author_email = "techfahad.s@gmail.com",
packages = find_packages(),
install_requires = get_requirements("requirements.txt")

)