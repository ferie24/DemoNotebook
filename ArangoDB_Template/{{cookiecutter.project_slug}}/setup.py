#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = []

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest>=3',{%- endif %} ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    project_urls={
        "Bug Tracker": "https://github.com/rajivsam/arangomlFeatureStore",
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        {%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
        {%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
    {%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
    {%- endif %}
    keywords='{{ cookiecutter.project_slug }}',
    package_dir={'{{ cookiecutter.project_slug }}' : '{{ cookiecutter.project_slug }}'},
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    package_data={'config': ['config/arango_feature_store_config.yaml']},

    include_package_data=True,
    #-----

    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
    #entry_points={
    #    'console_scripts': [
    #        '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
    #    ],
    #},
)
