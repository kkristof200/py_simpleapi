import setuptools, os

readme_path = os.path.join(os.getcwd(), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        long_description = f.read()
else:
    long_description = 'ksimpleapi'

setuptools.setup(
    name="ksimpleapi",
    version="0.0.41",
    author="Kristof",
    description="ksimpleapi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/py_simpleapi",
    packages=setuptools.find_packages(),
    install_requires=[
        'cloudscraper>=1.2.58',
        'kcu>=0.0.72',
        'requests>=2.26.0',
        'tldextract>=3.1.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)