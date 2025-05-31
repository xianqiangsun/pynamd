from setuptools import setup
from setuptools.command.build_py import build_py
import subprocess
import sys

def check_and_install_future():
    try:
        import future
        print("future package is already installed")
    except ImportError:
        print("future package not found, installing...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'future'])
            print("future package installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install future package: {e}")
            sys.exit(1)

if __name__ == '__main__':
    check_and_install_future()
    
    setup(
        name='pynamd',
        version='1.0',
        description='Python Tools for NAMD',
        author='Brian K. Radak',
        license='MIT',
        packages=['pynamd', 'pynamd.msmle'],
        cmdclass={'build_py': build_py},
    )
