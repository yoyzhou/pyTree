'''
Created on Sep 2, 2012

@author: yoyzhou
'''

from distutils.core import setup

setup(
      name='pyTree',
      version='1.0.8',
      description='A list-derived TREE data structure in Python ',
      author='Yoyo Zhou',
      author_email='iamyoyozhou@gmail.com',
      url='https://github.com/yoyzhou/pyTree/tree/pretty',
      packages=['pyTree'],
      package_dir={'pyTree': 'src/pyTree'},
      classifiers=[
          'Development Status :: 4 - Beta ',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License    ',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
           'Topic :: Software Development'
          ]
       )