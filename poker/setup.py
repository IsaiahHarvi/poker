from setuptools import setup, find_packages

def requirementsin():
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

setup(
    name='poker',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirementsin(),
    include_package_data=True,
    package_data={'' : ['tests/*.py']},
    entry_points={
        'console_scripts': [
            'poker=poker.main:main',
        ],
    },
)

