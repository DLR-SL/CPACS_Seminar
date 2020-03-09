# CPACS Seminar

The content of this page is used to introduce in working with CPACS. For this I like jupyter notebooks which you can run on your local PC to better followo and modify the examples.

### Setting up Conda environments to run the examples

If you have not set up your own Python environment I recommend using Conda as package and environment manager. In our case Miniconda is sufficient because we will set up our own environments indiviually. After installing Conda create a new environment (`conda create -n`) called `python3_cpacs` and install the `tigl3` and `tixi3` packages from `-c dlr-sc`:

```
conda create -n python3_cpacs python=3.5 tigl3 tixi3 -c dlr-sc
```

Now we need to install jupyter to run the notebooks. Activate our new python-environmen and type:
```
conda activate python3_cpacs
conda install jupyter
```

I recommend to have a look at the [Conda cheat sheet](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&ved=2ahUKEwiritrFk43oAhW0QUEAHTi_CH0QFjAFegQIAhAB&url=https%3A%2F%2Fdocs.conda.io%2Fprojects%2Fconda%2Fen%2F4.6.0%2F_downloads%2F52a95608c49671267e40c689e0bc00ca%2Fconda-cheatsheet.pdf&usg=AOvVaw3uUYEqas7NMuAmCCWAx_yl) to get a brief overview on Conda.

### Running Jupyter notebooks
Within your active conda environment (remember: `conda activate python3_cpacs`) navigate to your tutorial directory and active the notebook (`*.ipynb`) with:
```
jupyter-notebook notebookName.ipynb
```
Your browser will automatically open and connect to a local Conda host. 

### Trouble shooting
With Miniconda I experienced [this bug](https://github.com/jupyter/notebook/issues/4079#issuecomment-429475420) which was solved by giving the correct path to the python.exe.

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
  - [Documentation](http://tigl.sourceforge.net/Doc/tigl_usage.html)
  - [More examples and tutorials](https://github.com/rainman110/tigl-workshop)
