import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="vmrunPacked",
    version="0.0.1",
    author="THAVASIGTI",
    author_email="ganeshanthavasigti1032000@gmail.com",
    description="VmWare-vmrun execute actions use python",
    long_description=long_description,
    long_description_content_type="text/markdown",
<<<<<<< HEAD
    url="https://github.com/THAVASIGTI/vmrunPacked.git",
=======
    url="https://github.com/THAVASIGTI/tn_radio.git",
>>>>>>> 5efc00f686058209f1e94c65452cbb0b4ed73b38
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)