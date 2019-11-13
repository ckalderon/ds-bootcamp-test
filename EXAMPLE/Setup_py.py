import setuptools


with open('README.md') as readme_file:
    readme = readme_file.read()


requirements = []
setup_requirements = []
test_requirements = ['pytest']
extra_requirements = {
    'dev': ['pre-commit', 'flake8']
}


setuptools.setup(
    name='ds-bootcamp-test',
    author='Cem Kalderon',
    author_email='cemkalderon@gmail.com',
    description='JPEG implementation in Python.',
    url='https://github.com/JCZuurmond/pyjpeg',
    license='Open source',
    packages=setuptools.find_packages('.'),
    version='0.1.0',
    install_requires=requirements,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require=extra_requirements,
)
