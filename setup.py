from setuptools import setup

setup(
    name='437-project',
    version='1.2',
    packages=['tests', 'src'],
    url='https://github.com/tianakk/437-project',
    license='Personal',
    author='yousseffarouk',
    author_email='mail@mail.com',
    description='Event management system',
    long_description='Using this event management system, a user can create events or book tickets for an event as '
                     'well as view all events and all tickets or get a summary of all tickets',
    project_urls={
        'Source': 'https://github.com/tianakk/437-project',
    },
    install_requires=['pytest', 'pytest-cov', 'prettytable'],
    python_requires='>=3',
)
