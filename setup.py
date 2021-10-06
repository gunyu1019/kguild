from sys import version_info
from setuptools import setup

if version_info < (3, 7):
    raise RuntimeError("kguild v2 requires Python 3.7+")

packages = [
    'kguild',
]

setup(
    name='kguild',
    version='v1.0',
    packages=packages,
    url='https://github.com/gunyu1019/kguild',
    project_urls={
        "GitHub: issues": "https://github.com/gunyu1019/kguild/issues",
        "GitHub: repo": "https://github.com/gunyu1019/kguild",
    },
    license='MIT',
    author='gunyu1019',
    author_email='gunyu1019@gmail.com',
    description='A python wrapper for KoreanList',
    python_requires='>=3.7',
    long_description=open('README.md', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=open('requirements.txt', encoding='UTF-8').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: Korean',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
