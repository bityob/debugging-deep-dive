from setuptools import Extension, setup

    setup(
        name='myextension',
        version='1.0',
        ext_modules=[Extension('myextension', sources=['myextension.c'])]
    )
