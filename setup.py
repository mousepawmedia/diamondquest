import setuptools

setuptools.setup(
    # Metadata
    name="diamondquest",
    version="0.3",
    author="MousePaw Media",
    author_email="developers@mousepawmedia.com",
    description="A math-based mining adventure!",
    license="BSD 3-Clause License",
    keywords="game math education",
    # url="https://mousepawmedia.com/diamondquest",
    project_urls={
        "Source Code": "https://github.com/mousepawmedia/diamondquest",
        "Bug Tracker": "https://phabricator.mousepawmedia.net/maniphest"
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: X11 Applications",
        "Intended Audience :: Education",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games"
    ],

    # Packaging
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'diamondquest = diamondquest.__main__:main',
        ],
    },
    install_requires=[
        'pygame>=2.0.0.dev10'
    ],
)
