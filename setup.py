from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


long_description = '''This project contains all the necessary code to connect, send and receive messages to/from an AMQP-compliant peer or broker (Qpid, OpenAMQ, RabbitMQ) using Twisted.
It also includes support for using Thrift RPC over AMQP in Twisted applications.'''

setup_dict = dict(name='txamqp',
                  version='0.6.2',
                  url='http://github.com/odedlaz/txamqp',
                  license='Apache License 2.0',
                  author='Oded Lazar',
                  tests_require=['pytest'],
                  cmdclass={'test': PyTest},
                  install_requires=['Twisted>=16.2.0'],
                  author_email='odedlaz@gmail.com',
                  description='Python library for communicating with AMQP peers and brokers using Twisted',
                  long_description=long_description,
                  packages=['txamqp', 'txamqp.contrib', 'txamqp.contrib.thrift'],
                  package_dir={'txamqp': 'src/txamqp',
                               'txamqp.contrib': 'src/txamqp/contrib',
                               'txamqp.contrib.thrift': 'src/txamqp/contrib/thrift',
                               },
                  platforms='any',
                  extras_require={
                      'testing': ['pytest'],
                  })

setup(**setup_dict)
