"""Create environment for dev and use."""
from setuptools import setup


setup(
    name='http-server',
    description='A package for building and running the server module',
    package_dir={'': 'src'},
    author='Mark and Brian',
    author_email='mreynoso@spu.edu, monsteraono@gmail.com',
    py_modules=['http-server'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    # entry_points={
    #     'console_scripts': [
    #         'server=server:main'
    #     ]
    # }
)
