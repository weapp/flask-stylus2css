"""
flask-stylus2css
================

A small Flask extension that makes it easy to use Stylus with your Flask application.

Usage
-----

You can activate it by calling the ``stylus2css`` function with your Flask app as a parameter:

      from flaskext.stylus2css import stylus2css
      stylus2css(app, css_folder='css', stylus_folder='src/stylus')

This will intercept the request to ``css_folder`` and compile de file if is necesary using the files from ``stylus_folder``.

When you deploy your app you might not want to accept the overhead of checking the modification time of your ``.stylus`` and ``.css`` files on each request. A simple way to avoid this is wrapping the stylus2css call in an if statement:

      if app.debug:
          from flaskext.stylus2css import stylus2css
          stylus2css(app)
          
If you do this you'll be responsible for rendering the ``.stylus`` files into ``.css`` when you deploy in non-debug mode to your production server.


- documentation_
- development_


.. _documentation: https://github.com/weapp/flask-stylus2css
.. _development: https://github.com/weapp/flask-stylus2css

"""

from setuptools import setup


setup(
    name='flask-stylus2css',
    version='0.1',
    url='https://github.com/weapp/flask-stylus2css',
    license='MIT',
    author='Manuel Albarran',
    #author_email='',
    description='A small Flask extension that adds Stylus support to Flask.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'stylus'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
