# GODEL data generator for dialog systems

## Introduction
This repository is used to interact with Microsoft's Large-Scale Pre-Training for Goal-Directed Dialog (GODEL) model (source code [here](https://github.com/microsoft/GODEL)).<br>
The main application is to generate data for dialog systems.

## Installation
Please install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (miniconda recommended) for the environment manager.<br>

Once conda is installed, you can create and activate the environment using the following commads.

```
conda env create -f godel-generate.yml
conda activate godel-generate
```

## Usage
To generate data from the model, please modify the generate.sh script to fit your use case. Then, simply run

```
bash generate.sh
```