from setuptools import setup, find_packages

setup(
    name='ssh_commander',
    version='0.0.1',
    packages=find_packages(),
    description='This tool helps to configure and test servers/network devices via SSH.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ray Bernard',
    author_email='ray.bernard@outlook.com',
    url='https://github.com/raymondbernard/sshcommander',
    install_requires=[
        # List your package dependencies here
        # e.g., 'requests', 'numpy>=1.13.1'
    ],
    classifiers=[
        # Choose your license and programming language versions here
        # For example:
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
