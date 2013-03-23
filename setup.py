from setuptools import setup, find_packages

requires=[
    'pyramid',
    'python-social-auth',
]

testing_extras = [
    'unittest2',
    'nose',
    'nose-testconfig',
    'selenium',
]

docs_extras = [
    'Sphinx',
    'docutils',
]

setup(name='pyramid-social-auth',
      version='0.1',
      description=(
          'Python Social Auth (PSA) for Pyramid.'),
      long_description='',
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
          'Framework :: Pyramid',
      ],
      keywords='oauth openid social auth facebook google pyramid rest',
      author='Wayne Witzel III',
      author_email='wayne@pieceofpy.com',
      maintainer='',
      maintainer_email='',
      url='http://pythonhosted.org/pyramid-social-auth',
      packages=find_packages(
          exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={
          'docs': docs_extras,
          'testing': testing_extras,
      },
      )
