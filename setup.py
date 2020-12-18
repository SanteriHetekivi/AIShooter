import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AIShooter",
    version="0.0.1",
    author="Santeri Hetekivi",
    author_email="dev@hetekivi.com",
    description="Just simple AI shooter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanteriHetekivi/AIShooter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.3',
    install_requires=[
        'pygame',
    ]
)
