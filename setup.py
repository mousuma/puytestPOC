from setuptools import setup, find_packages

setup(
    name='pythonProject',
    version='1.0',
    url='',
    license='',
    author='mousuma',
    author_email='mousuma.roy@gmail.com',
    description='pytest project',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "pytest==6.2.5",
        "pytest-html==2.1.1",
        "requests==2.23.0",
        "requests-oauthlib==1.3.0",
        "PyMySQL==0.9.3",
        "WooCommerce==2.1.1",
    ],
)
