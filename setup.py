# voorbeeld van de Flask tutorial
# http://flask.pocoo.org/docs/1.0/tutorial/

import io

from setuptools import find_packages, setup

with io.open('DESCRIPTION.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='applicatie',
    version='1.0.0',
    url='http://blabla.nl',
    license='BSD',
    maintainer='Agile Team Overheid',
    maintainer_email='ato@cbs.nl',
    description='Controletool Iv3',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
