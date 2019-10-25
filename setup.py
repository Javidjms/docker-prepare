from setuptools import find_packages, setup

VERSION = '1.0.0'

with open('requirements.txt', 'r') as f:
    requirements = [x.strip() for x in f if x.strip()]

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='docker-prepare',
    packages=find_packages(),
    version=VERSION,
    license='MIT',
    description='Docker-prepare is a tool for generating Dockerfile from a combination of templates',
    long_description=readme,
    author='Javid Mougamadou',
    author_email='javidjms0@gmail.com',
    url='https://github.com/Javidjms/docker-prepare',
    download_url='https://github.com/Javidjms/docker-prepare/archive/1.0.0.zip',
    keywords=['docker', 'docker-prepare', 'template', 'jinja', 'dockerfile', 'extends'],
    install_requires=requirements,
    entry_points={
        'console_scripts': ['docker-prepare=docker_prepare.command_line:main'],
    },
    python_requires='>=3.0.*',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    project_urls={
        'Source': 'https://github.com/Javidjms/docker-prepare',
    },
)
