from setuptools import setup, find_packages

from smi_python_commons.project import NAME, VERSION

setup(
    name=NAME,
    version=VERSION,
    description='setmy.info python commons library.',
    long_description='setmy.info python commons library.',
    author='Imre Tabur',
    author_email='info@setmy.info',
    license='MIT',
    url='https://github.com/setmy-info/python-commons',
    packages=find_packages(),
    install_requires=[
        "pyyaml==6.0.3"
    ],
    extras_require={
        "dev": [
            "bandit==1.8.6",
            "behave==1.3.3",
            "pip_audit==2.9.0",
            "wheel==0.46.3",
            "twine==6.2.0",
        ]
    },
)
