from distutils.core import setup

setup(
    name='django-auditlog',
    version='0.4.7',
    packages=['auditlog', 'auditlog.migrations', 'auditlog.management', 'auditlog.management.commands'],
    package_dir={'': 'src'},
    url='https://github.com/GoVanguard/django-auditlog',
    license='MIT',
    author='Shane William Scott; Jan-Jelle Kester',
    description='Audit log app for Django',
    install_requires=[
        'django-jsonfield>=1.0.0',
        'python-dateutil>=2.6.0'
    ],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],        
)
