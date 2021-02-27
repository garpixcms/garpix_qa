from setuptools import setup, find_packages

setup(
    name='garpix_qa',
    version='1.0.2',
    description='Checking the Django project for quality',
    author='Garpix LTD',
    author_email='info@garpix.com',
    license='MIT',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django >= 1.11',
        'flake8 >= 3.8.4',
        'flake8-polyfill >= 1.0.2',
        'radon >= 4.3.2',
        'bandit >= 1.7.0',
    ],
)
