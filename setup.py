from setuptools import find_packages
from setuptools import setup

version = "1.0"


long_description=open("README.txt").read() + "\n" + open("HISTORY.txt").read()
    
setup(name="osha.hwctheme",
      version=version,
      description="Theme for OSHA HW Campaign 2014",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        ],
      keywords="",
      author="",
      author_email="",
      url="https://github.com/syslabcom/osha.hwctheme",
      license="gpl",
      packages=find_packages("src"),
      package_dir={"": "src"},
      namespace_packages=["osha", ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "setuptools",
          "collective.mtrsetup",
          "plone.api",
          "plone.app.contenttypes",
          "plone.namedfile[blobs]",
          "plone.app.multilingual[dexterity]>=1.0",
          "plone.multilingual>=1.0",
          "plone.multilingualbehavior>=1.0",
          'plone.app.theming',
          'webcouturier.dropdownmenu',
          "z3c.jbot",
      ],
      extras_require={"test": ["plone.app.testing[robot]>=4.2.2",
                               "plone.app.robotframework[reload]"]},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
