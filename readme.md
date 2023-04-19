# CPACS Seminar

The content of this page is used to introduce you to working with CPACS. You can run the Jupyter notebooks on your local PC or directly in your browser:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DLR-SL/CPACS_Seminar/HEAD)

### Setting up Conda environments to run the examples

If you do not have your own Python environment set up, I recommend using Conda as a package and environment manager. In our case, Miniconda is sufficient as we will be setting up our own environments individually. After installing Conda, create a new environment from the `environment.yml` file:

```
conda env create -f environment.yml
```

Activate our new python-environment via:
```
conda activate cpacsSeminar
```

I recommend to have a look at the [Conda cheat sheet](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&ved=2ahUKEwiritrFk43oAhW0QUEAHTi_CH0QFjAFegQIAhAB&url=https%3A%2F%2Fdocs.conda.io%2Fprojects%2Fconda%2Fen%2F4.6.0%2F_downloads%2F52a95608c49671267e40c689e0bc00ca%2Fconda-cheatsheet.pdf&usg=AOvVaw3uUYEqas7NMuAmCCWAx_yl) to get a quick overview of Conda.

### Running Jupyter notebooks
Within your active conda environment (remember: `conda activate python3_cpacs`) navigate to your tutorial directory and active the notebook (`*.ipynb`) with:
```
jupyter-notebook notebookName.ipynb
```
Your browser will automatically open and connect to a local Conda host. 

### Troubleshooting
With Miniconda I experienced [this bug](https://github.com/jupyter/notebook/issues/4079#issuecomment-429475420), which was fixed by specifying the correct path to the python.exe.

### CPACS links
  - [Download](https://cpacs.de/pages/download.html)
  - [GitHub repository](https://github.com/DLR-SL/CPACS)
  - [Documentation](https://cpacs.de/pages/documentation.html)

### Open source XSD viewer
- [XSDDiagram](http://regis.cosnier.free.fr/?page=XSDDiagram)
- [GitHub](https://github.com/dgis/xsddiagram)

### TiXI and TiGL links

- TiXI:
  - [Download](https://github.com/DLR-SC/tixi/wiki/Downloads)
  - [GitHub repository](https://github.com/DLR-SC/tixi)
  - [Documentation](http://tixi.sourceforge.net/Doc/index.html)
  - [Wiki](https://github.com/DLR-SC/tixi/wiki)
  
- TiGL:
  - [Download](https://github.com/DLR-SC/tigl/releases)
  - [Homepage](https://dlr-sc.github.io/tigl/)
  - [GitHub repository](https://github.com/DLR-SC/tigl/)
  - [Documentation](https://dlr-sc.github.io/tigl/doc/latest/index.html)
  - [More examples and tutorials](https://github.com/rainman110/tigl-workshop)
