from setuptools import setup
REQUIRES = [
    'requests',
    'structlog',
    'curlify',
    'allure-pytest'
]



setup(
    name='restclient_dl',
    version='0.1',
    packages=['restclient'],
    url='https://github.com/DiLysenk/restclient_dl',
    license='MIT',
    author='lysenkodmitry',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient ohh'
)
