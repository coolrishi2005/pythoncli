from setuptools import setup
setup(
    name = 'pythoncli',
    version = '0.1.0',
    packages = ['pcv2_baseline'],
    entry_points = {
        'console_scripts': [
            'pcv2_baseline = pcv2_baseline.__main__:main'
        ]
    })
