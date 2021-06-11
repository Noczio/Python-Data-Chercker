from setuptools import setup, find_packages

setup(
    name='generator_data_checker',
    version='1.0.2',
    description='Python data checker withing a range',
    url='https://github.com/Noczio/Python-Data-Chercker.git',
    author='Devnocz / David Rey',
    author_email='devnocz@gmail.com',
    keywords='Python, data, check, generator',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7',
)
