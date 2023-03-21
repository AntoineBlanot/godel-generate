# godel-generate
This repository is used to interact with Microsoft's Large-Scale Pre-Training for Goal-Directed Dialog (GODEL) model.
The main application is to generate data for dialog systems.

# Installation

Install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (miniconda recommended)

Create and activate the environment using these lines

`
conda env create -f godel-generate.yml
conda activate godel-generate
`

# Usage

Simply modify the generate.sh script with your own variables. Then run

`bash generate.sh`