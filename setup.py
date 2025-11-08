'''
The setup.py is a Python script typically included with Python-written libraries or apps.
Its objective is to ensure that the program is installed correctly. With the aid of pip, we can use the setup.py to install any module without having the call setup.py directly.
command used: pip install -r requirements.txt(added HYPHEN_E_DOT in requirements.txt to connect to `setup.py`)
'''
from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]: 
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #the text file has a new line after every line, to avoid adding it in our list we replace the new line with ""
        requirements = [requirement.replace("\n", "") for requirement in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements       

setup(
    name='PihusFirstMLProject',
    version='0.0.1',
    author='Pihu',
    author_email='pihulearns@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)