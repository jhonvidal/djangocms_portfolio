import os
from setuptools import setup, find_packages


def read(fname):
        # read the contents of a text file
            return open(os.path.join(os.path.dirname(__file__), fname)).read()

        # allow setup.py to be run from any path
        os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

        setup(
                    name='djangocms_portfolio',
                        version='0.6',
                            packages=find_packages(),
                                include_package_data=True,
                                    license='GNU General Public License',
                                        description='A simple Portfolio APP for djangoCMS.',
                                            long_description=read('README.md'),
                                                url='https://github.com/Pyc0kw4k/djangocms_portfolio',
                                                    author='Lozano Joaquim',
                                                        author_email='joaquimlozano@gmail.com',
                                                            install_requires=(
                                                                        'django-filer',
                                                                                'django-taggit',
                                                                                    ),
                                                                classifiers=[
                                                                            'Environment :: Web Environment',
                                                                                    'Framework :: Django',
                                                                                            'Framework :: Django :: 1.8',
                                                                                                    'Intended Audience :: Developers',
                                                                                                            'License :: OSI Approved :: BSD License',  # example license
                                                                                                                    'Operating System :: OS Independent',
                                                                                                                            'Programming Language :: Python',
                                                                                                                                    # Replace these appropriately if you are stuck on Python 2.
                                                                                                                                            'Programming Language :: Python :: 3',
                                                                                                                                                    'Programming Language :: Python :: 3.4',
                                                                                                                                                            'Programming Language :: Python :: 3.5',
                                                                                                                                                                    'Topic :: Internet :: WWW/HTTP',
                                                                                                                                                                            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                                                                                                                                                                                ],
                                                                )
