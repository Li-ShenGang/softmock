from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="softmock",
    version="0.2.6",
    author="lishengang",
    author_email="py.r@qq.com",
    description="一个基于录制请求的mock工具",
    long_description="",
    license="MIT",
    url="https://github.com/web-trump/soft-mock",
    packages=find_packages(
        include=['mitmproxy', 'softmock', 'softmock.*', 'mitmproxy.*']),
    include_package_data=True,
    install_requires=[
        "cchardet",
        "requests>=2.10.0,<3.0",
        "colorama>=0.4.4,<1.0",
        "asgiref>=3.2.10,<3.4",
        "blinker>=1.4, <1.5",
        "Brotli>=1.0,<1.1",
        "certifi>=2019.9.11",  # no semver here - this should always be on the last release!
        "click>=7.0,<8",
        "cryptography>=3.3,<3.4",
        "flask>=1.1.1,<1.2",
        # "h11>=0.11,<0.13",
        "h2>=4.0,<5",
        "hyperframe>=6.0,<7",
        "kaitaistruct>=0.7,<0.10",
        "ldap3>=2.8,<2.9",
        "msgpack>=1.0.0, <1.1.0",
        "passlib>=1.6.5, <1.8",
        "protobuf>=3.14,<3.15",
        "pyOpenSSL>=20.0,<20.1",
        "pyparsing>=2.4.2,<2.5",
        "pyperclip>=1.6.0,<1.9",
        "ruamel.yaml>=0.16,<0.17",
        "sortedcontainers>=2.3,<2.4",
        "tornado>=4.3,<7",
        "urwid>=2.1.1,<2.2",
        "wsproto>=1.0,<1.1",
        "publicsuffix2>=2.20190812,<3",
        "zstandard>=0.11,<0.16",
    ],
    extras_require={
        ':sys_platform == "win32"': [
            "pydivert>=2.0.3,<2.2",
        ],
        'dev': [
            "hypothesis>=5.8,<6.1",
            "parver>=0.1,<2.0",
            "pytest-asyncio>=0.10.0,<0.14,!=0.14",
            "pytest-cov>=2.7.1,<3",
            "pytest-timeout>=1.3.3,<2",
            "pytest-xdist>=2.1.0,<3",
            "pytest>=6.1.0,<7",
            "tox>=3.5,<4",
        ]
    },
    python_requires='>=3.8',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)'
    ],
    entry_points={
        'console_scripts': ['softmock=softmock:entry']
    }
)
