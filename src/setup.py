from setuptools import setup, find_packages

setup(
    name="atcui",
    version='0.1.0',
    author="",
    description="",
    license="",
    url="",
    packages=find_packages(),
    install_requires=[
	"atc_thrift",
        "atcd",
        "django-atc-api",
        "django-atc-demo-ui",
        "django-atc-profile-storage"
    ],

    entry_points={
        'console_scripts': [
            'atcui = atcui.manage:main'
        ]
    },

    include_package_data = True
)
