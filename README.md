# kirstu

Collection of basic scripts and methods

**Copyright (c) 2019 Victor Hugo Souza**

## Installation

### Windows

Create an Anaconda environment. Using the Anaconda terminal go to the root folder and type:

    $ conda env create

It will create an environment named `kirstu`. To activate the enviornment type:

    $ activate kirstu

The installation may take a while depending on the internet connection. Many packages will be installed as indirect dependencies.

## Requirements

The following packages are recommended to run everything in `kirstu`:

* Python 3.7
* numpy
* scipy
* scikit-image
* ipython
* jupyter
* notebook
* matplotlib
* h5py
* pillow
* nibabel
* vtk

Download a compiled VTK 8.1 for Windows 64 bits provided [here](https://github.com/vhosouza/kirstu/releases/download/v0.0.1/vtk-8.1.2-cp37-cp37m-win_amd64.whl). To install VTK, using the command prompt, go to the folder containing the WHL file, and run the pip installation:

    $ pip install vtk-8.1.2-cp37-cp37m-win_amd64.whl

