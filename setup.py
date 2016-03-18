from setuptools import setup
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/fundamentals/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()

setup(
    name='fundamentals',
    version=__version__,
    description='Some project setup tools including logging, settings and database connections',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords=['logging', 'database'],
    url='https://github.com/thespacedoctor/fundamentals',
    download_url='https://github.com/thespacedoctor/fundamentals/archive/v%(__version__)s.zip' % locals(
    ),
    author='David Young',
    author_email='davidrobertyoung@gmail.com',
    license='MIT',
    packages=['fundamentals'],
    install_requires=[
        'pyyaml',
        'docopt',
        'MySQL-python',
        'python-dateutil',
        'eventlet',
        'fundmentals'
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
    # entry_points={
    #     'console_scripts': ['fundamentals=fundamentals.cl_utils:main'],
    # },
    zip_safe=False
)
