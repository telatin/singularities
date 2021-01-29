---
sort: 8
---
# Eggnog-mapper

 eggnog mapper requires the same version of (diamond)[https://github.com/bbuchfink/diamond] used to build the database, and the download of its database via `download_eggnog_data.py`.

To be used with the [fill_template]({{ '/scripts/fill-template.html' | prepend: site.baseurl }}) tool.

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
    /opt/software/conda/bin/conda create -p /opt/software/conda_env -y {package}={version}
    source /opt/software/conda/bin/activate /opt/software/conda_env
    wget https://github.com/bbuchfink/diamond/releases/download/v0.9.32/diamond-linux64.tar.gz
    tar xvfz diamond-linux64.tar.gz
    rm diamond-linux64.tar.gz
    mv ./diamond $(which diamond)
    mkdir -p /opt/software/conda_env/lib/python2.7/site-packages/data
    printf "y\ny\ny"  | download_eggnog_data.py
    cd /opt/software

%runscript
    exec emapper.py "$@"

```

This page has been automatically generated from a template file from the [repository](https://github.com/telatin/singularities).
Please, report [issues](https://github.com/telatin/singularities/issues) if you think this template could or should be improved.
