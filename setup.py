from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty line and -e.
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_list

setup(
    name='Network Security',
    version='0.0.1',
    author='Neelakanta Sapare',
    author_email='neelakantasapare@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement()
)