import setuptools

with open('README.rst', 'r') as file:
    read_me = file.read()

setuptools.setup (
    name="hr",
    version="1.0",
    author="Saket Kumar",
    author_email="saketkumar1994@outlook.com",
    description="manage users on a server based on an 'inventory' JSON file",
    long_description=read_me,
    long_description_content_type="text/markdown",
    url="https://github.com/pullubros/hr",
    packages=setuptools.find_packages(),
    package_dir={'':'src'},
)
