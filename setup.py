from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="WebApp Permission Map API",
    version=VERSION,
    description="Automatically assign webserver user permission to required folders",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="webapp webserver dev",
    url="https://github.com/danilocgsilva/webapp_permissionmap_api",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["webapp_permission_map_api"],
    include_package_data=True
)

