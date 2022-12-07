from setuptools import setup

setup(
    name='437-project',
    version='1.0',
    packages=['tests'],
    url='https://github.com/tianakk/437-project',
    license='Personal',
    author='yousseffarouk',
    author_email='mail@mail.com',
    description='desc',
    long_description='desc',
    project_urls={
        'Source': 'https://github.com/tianakk/437-project',
    },
    install_requires=['pytest', 'pytest-cov', 'prettytable'],
    python_requires='>=3',
)
