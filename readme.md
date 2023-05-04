# CPACS Seminar

This project aims to introduce you to working with CPACS. You can download/clone it and run the [*Jupyter Notebooks*](https://jupyter.org/) on your local PC or you can run it directly in your browser via *Binder*:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DLR-SL/CPACS_Seminar/HEAD)

If this does not work:
  - go to [mybinder.org](https://mybinder.org/) 
  - copy `https://github.com/DLR-SL/CPACS_Seminar` into the `GitHub repository name or URL` field
  - click `launch` and get a coffee (it may take a while)...

## Setting up Conda environments and run the examples

It is recommended to use [Conda](https://docs.conda.io) as a Python package and environment manager. Create a new environment from the `environment.yml` file:
```
conda env create -f environment.yml
```

Activate our new python-environment via:
```
conda activate cpacsSeminar
```

Call JupyterLab:
```
jupyter lab
```

A browser should open automatically (if not, copy and paste the URL shown in the conda terminal into your browser). Navigate to the Notebook exercises (`*.ipynb`) and open it.

## Helpful material

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
