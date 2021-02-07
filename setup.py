from setuptools import setup, find_packages
from src.utils.version import version
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def _process_requirements():
    with open('./requirements.txt', encoding='utf-8') as rqmts:
        result = rqmts.read()
    return result.split('\n')


setup(
    name="softmock",
    version=version,
    author="lishengang",
    author_email="py.r@qq.com",
    description="一个基于录制请求的mock工具",
    long_description=long_description,
    license="MIT",
    url="https://github.com/web-trump/soft-mock",
    packages=find_packages(include=['softmock', 'softmock.*']),
    install_requires=_process_requirements(),
    python_requires='>=3.8',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)'
    ],
    entry_points={
        'console_scripts': ['softmock=main:main']
    }
)
