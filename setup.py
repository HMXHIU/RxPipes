from distutils.core import setup

from setuptools import find_packages

from rxpipes import __version__

setup(
    name="rxpipes",
    version=__version__,
    author="shirecoding",
    author_email="shirecoding@gmail.com",
    install_requires=["rx", "toolz"],
    extras_require={"test": ["numpy", "cv2"]},
    url="https://github.com/shirecoding/RxPipes",
    download_url=f"https://github.com/shirecoding/ModelMaker/archive/{__version__}.tar.gz",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages() + [],
    package_data={},
)
