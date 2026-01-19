from setuptools import setup, find_packages

HYPENATE = '-e ./'  # Example of a line to ignore
def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    requirements = [req for req in requirements if req.strip() != HYPENATE]
    return [req.strip() for req in requirements]

setup(
    name='my_package',
    version='0.1.0',
    author='adithya prabhu',
    author_email='adithyaprabhu@example.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  
    description='A sample Python package',
)
    