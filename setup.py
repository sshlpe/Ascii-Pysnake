from setuptools import setup, find_packages

setup(
    name='Ascii PySnake',
    version='1.0',
    author='Sshlpe',
    description='Snake Game made with AsciiMatics',
    long_description='Simple terminal based snake game that follow the terminal size',
    url='https://github.com/sebalepe/Ascii-Pysnake.git',
    keywords='ascii, asciimatics, python, snake',
    python_requires='>=3.7, <4',
    packages=find_packages(include=['snake.py', 'files.*']),
    install_requires=['asciimatics>=1.5.0'],
    package_data={
        'score': ['files/score.txt'],
    }
)