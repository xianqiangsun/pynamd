PyNAMD
======

Python tools for NAMD

Description
===========

PyNAMD is a package meant to provide a flexible, lightweight interface to NAnoscale Molecular Dynamics ([NAMD](http://www.ks.uiuc.edu/Research/namd/)) input and output. Since many powerful and mature packages exist for trajectory analysis, the focus is almost exclusively on energy based output.

The PyNAMD library is also accompanied by several scripts for common tasks useful in molecular dynamics (MD) simulations, such as rapidly computing averages and fluctuations - all directly from NAMD output. Developments are ongoing to provide considerably more complicated analysis tools such as multistate reweighting methods (e.g., WHAM) for generalized ensemble, replica exchange, and stratified umbrella sampling simulations.

Installation
============

To install PyNAMD, clone this git repository and change into the new "pynamd" directory:

```bash
git clone git@github.com:xianqiangsun/pynamd.git
cd pynamd
```

Before installing, ensure that the `future` package is installed, as it is required for compatibility:

```bash
pip install future
```

PyNAMD can then be installed with the command:

```bash
pip install ./pynamd
```

Alternatively, you can install in development mode if you plan to modify the code:

```bash
pip install -e ./pynamd
```

If you are using the Python distribution that comes with your operating system, you may need to run the above commands with administrative privileges or use the `--user` flag -- the latter is recommended:

```bash
pip install --user ./pynamd
```

**Note:** This code has been tested using Python 3.12.2.

It is expected that this project will utilize a considerable amount of "bleeding edge" numerical tools, so it would also be a good idea to use a customizable Python environment that has the latest numpy and scipy, such as that provided by [Anaconda](https://www.continuum.io/downloads).


Examples
========

```python
import pynamd

log = pynamd.NamdLog("00001.log", "00002.log")

#info contains information about time-steps, temperatures etc...
log.info

#energy contains the time-series data in a dictionary
log.energy

#log.energy can easily be converted into a pandas dataframe
import pandas as pd 
df =  pd.DataFrame(log.energy)
```

Further examples are in the [examples](examples/) subfolder. 


Tests
=====

Tests can be run using the [pytest](http://doc.pytest.org/en/latest/) framework. Install pytest using conda `conda install pytest` or pip `pip install pytest`.

Run with `pytest` in the root of the repository.  

Distribution
============

This code is forked from the original PyNAMD repository: git@github.com:radakb/pynamd.git

Authors and Contributors
========================

* **Brian Radak** | brian.radak@gmail.com  
  *Original author and primary developer*

* **Xianqiang Sun** | xianqiang.sun@autodrug.ai  
  *Contributor - Updated the `validate_state_dict()` function in cphlog.py and resolved compatibility errors for Python 3.12.2*  
  *Founder of [AutoDrug.ai](https://autodrug.ai)*



