import platform
from setuptools import setup, find_packages

def get_requirements():
    os_type = platform.system()
    
    if os_type == "Windows":
        requirements_file = "requirements-win.txt"
    else:
        requirements_file = "requirements-linux.txt"
    
    with open(requirements_file, "r") as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

setup(
    name='poker',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=get_requirements(),
    include_package_data=True,
    package_data={'' : ['tests/*.py']},
    entry_points={
        'console_scripts': [
            'poker=poker.main:main',
        ],
    },
)

