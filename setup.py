"""it is essential part of packing and distributing Python projects.it is used by setup tools to package the project, manage dependencies, and provide metadata about the project."""

from setuptools import setup, find_packages 
#so where ever ther is __init__.py file it will be considered as a package which is the parent folder of the project

from typing import List

def get_requirements() -> List[str]:
    """ this function will return list of requirements"""
    requirement_lst:List[str] = [] 
    try: 
        with open('requirements.txt','r') as file:
            #read lines frm line
            lines = file.readlines()
            #proces each line 
            for line in lines:
                #remove any leading or trailing whitespace
                requirement = line.strip()
               #ignoring empty lines and -e. 

                if requirement and not requirement.startswith('-e'):

                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")

    return requirement_lst

## print(get_requirements())


setup(
    name='networksecurity',
    version='0.0.1',
    author='mohammad faiz jabir',
    author_email='faizjabir003@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements() # makes sure it install the requirements.txt file
)