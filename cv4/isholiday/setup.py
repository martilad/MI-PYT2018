'''from setuptools import setup

setup(
    name='isholiday',
    version='0.1',
    description='Finds Czech holiday for given year',
    author='Ondřej Caletka',
    author_email='ondrej@caletka.cz',
    license='Public Domain',
    url='https://gist.github.com/oskar456/e91ef3ff77476b0dbc4ac19875d0555e',
    py_modules=['isholiday'],
)
'''

#python setupy develop - aktualni kod, nemusi se d2lat updaty
# sdist  instala4n9 ba94ek tar - poslani k instalaci 


from setuptools import setup


with open('README') as f:
    long_description = ''.join(f.readlines())


setup(
    name='isholiday',
    version='0.1',
    description='Finds Czech holiday for given year',
    long_description=long_description,
    author='Ondřej Caletka',
    author_email='ondrej@caletka.cz',
    keywords='holiday,dates',
    license='Public Domain',
    url='https://gist.github.com/oskar456/e91ef3ff77476b0dbc4ac19875d0555e',
    #py_modules=['isholiday'],
    packages=['isholiday'],
    install_requires=['Flask'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'isholiday_demo = isholiday.holidays:main',
        ],
    },
)