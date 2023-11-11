from setuptools import find_packages, setup           # map the application's foder strucure. for every folder create package
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(fil_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(fil_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', "")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)      # remove -e . from requirement.txt

    return requirements



setup(
    name='ml_pro',
    version='0.0.1',
    author="Aditya Pandey",
    author_email='adityapande107@gmail.com',
    packages=find_packages(),
    install_requres=get_requirements('requirements.txt')
)