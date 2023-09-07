from setuptools import setup, find_packages

setup(
    name='smi_python_commons',
    version='0.1.1-SNAPSHOT',
    description='setmy.info python commons library.',
    long_description='setmy.info python commons library.',
    author='Imre Tabur',
    author_email='info@setmy.info',
    license='MIT',
    url='https://github.com/setmy-info/python-commons',
    packages=find_packages(),
    install_requires=[
        "pyyaml==6.0.1"
    ],
)
