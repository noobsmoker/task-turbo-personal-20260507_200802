from setuptools import setup, find_packages

setup(
    name="task-turbo-personal-20260507_200802",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'task=task:main',
        ],
    },
)
