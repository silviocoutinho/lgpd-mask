from setuptools import setup, find_packages

setup(
    name='mascararLgpd',
    version='1.0',
    python_requires='>=3.6',  
    packages=find_packages(),
    install_requires=[
        'PyMuPDF==1.21.1',  
        'tk==0.1.0',  
    ],
)
