# Welcome!

### Python setup

Recommended to install Anaconda. This is a free and open-source distribution of the
Python and R programming languages for scientific computing, aiming to simplify package
management and deployment

Installing conda

1. Get the distribution from https://www.anaconda.com/download#downloads (Win, Mac,
   Linux)
2. Install it, remember the path, e.g. `C:\opt\anaconda3`

Creating an environment

1. Open a command prompot
2. `cd C:\opt\anaconda3`
3. `condabin\conda create -n ml2 python=3.11`
4. `condabin\conda activate ml2`
5. `python --version`

### Open course notebooks

1. From start menu, open a new shell via "Anaconda" > "Anaconda Prompt"
2. `cd` into the base directory for this course, e.g. `C:\Users\Michael\Desktop\hslu\cas\ml2\01-py-refresher`
3. `conda activate ml2`
4. `pip install -r requirements.txt`
5. `jupyter notebook` and wait for browser to open `http://localhost:8888`

### Alternatives to web interface: Editors/IDEs of your choice

- [Visual Studio Code](https://visualstudio.microsoft.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Spyder](https://www.spyder-ide.org/)
