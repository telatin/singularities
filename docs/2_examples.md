---
sort: 2
permalink: /workflow
---

# Typical workflow

Given a tool, the general workflow will be:

1. Generate a Singularity [definition file](https://sylabs.io/guides/3.0/user-guide/definition_files.html).
2. Generation of a Singularity image from the definition file (generally `sudo singularity build <image> <definition_file>`.)
3. Generation of the wrapper and symlinks to make the tools seamlessly available to the user

# Example: spades

## Definition files

Spades is readily available from BioConda, so we can generate a definition
file using the templating scripts:

```bash
fill_template.pl package=spades version=3.14.1 > spades_3.14.1.def
```

This will look like:
```yaml
Bootstrap: docker
From: centos:centos7.6.1810


%environment
    source /opt/software/conda/bin/activate /opt/software/conda_env


%post
    yum -y install epel-release wget which nano curl zlib-devel
    yum -y groupinstall "Development Tools"

    mkdir -p /opt/software

    cd /opt/software
    curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    sh ./Miniconda3-latest-Linux-x86_64.sh -p /opt/software/conda -b

    /opt/software/conda/bin/conda config --add channels defaults
    /opt/software/conda/bin/conda config --add channels conda-forge
    /opt/software/conda/bin/conda config --add channels bioconda
    /opt/software/conda/bin/conda create -p /opt/software/conda_env -y spades=3.14.1    
    source /opt/software/conda/bin/activate /opt/software/conda_env

    cd /opt/software

%runscript
    exec spades.py "$@"
```


## Build the image

This step is very standard:
```
sudo singularity build spades~3.14.1 spades_3.14.1.def
```

## Run the image

### With entrypoint

We defined that `spades.py` is the entry point so the image itself
can be executed as:
```
spades~3.14.1 -1 file_R1.fq -2 file_R2.fq -o assembly
```
that is equivalent to
```
singularity run spades~3.14.1 -1 file_R1.fq -2 file_R2.fq -o assembly
```

### Without entrypoint

If the package has more binaries we want to use beyond the entrypoint
(in our case `spades.py`) each binary can be executed with `singularity exec IMAGE binary`:

```
singularity exec spades~3.14.1 spades-bwa
```

## Wrappers

To make the execution of a program seamless one can make a wrapper script like the following
(calling it, for example, `spades~3.14.1.sh`):

```bash
#!/bin/bash
IMAGE=/path/to/spades~3.14.1
singularity exec $IMAGE $(basename "$0") "$@"
```

and then generate a set of symlinks to it:
```
for BIN in spades.py spades-bwa;
do
  ln -s spades~3.14.1.sh $BIN
done
```

this way the execution of `spades.py` or `spades-bwa` will resemble the native
installation of the tool.
