from setuptools import setup

def requirements():
    with open("requirements.txt", encoding="utf-8") as f:
        install_requires = f.readlines()
    return install_requires

def readme():
    with open("zombie_calculator/pack_resources/help/help.md", encoding="utf-8") as f:
        context = f.read()
    return context

setup(
    name = "zombie_calculator",
    version = "0.0.4.3",
    author = "kndy666",
    author_email = "kndy_666@163.com",
    description = "A program used to calculate specific pvz spawn seed.",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    keywords = "pvz",
    url = "https://github.com/Kndy666/zombie_calculator",
    packages = ["zombie_calculator", "zombie_calculator/gui", "zombie_calculator/pack_resources"],
    install_requires = requirements(),
    license = "GNU Lesser General Public License",
    extras_require = {"nuitka" : "nuitka>=1.0.4"},
    #python_requires = ">=3.8, <=3.9",
    entry_points = {
        "console_scripts" : [
            "zombie_calculator = zombie_calculator.__main__:main"
            ]
        },
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Win32 (MS Windows)",
        "Natural Language :: Chinese (Simplified)",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: C++",
        "Programming Language :: Python :: 3.8",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"
        ],
    include_package_data = True
    )