from setuptools import setup, find_packages

setup(
    name='tinydav',
    url='https://github.com/ZeitOnline/tinydav',
    version='0.7.1+patchmultipleprops.dev0',
    author='Manuel Hermann, Zeit Online',
    author_email='zon-backend@zeit.de',
    description='A small and handy WebDav Client',
    long_description=open('README.txt', 'r').read(),
    setup_requires=['setuptools_git'],
    namespace_packages=['tinydav'],
    include_package_data=True,
    zip_safe=False,
    keywords='WebDAV',
    license='LGPL',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet ::'
    ]
)
