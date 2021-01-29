
---
sort: 15
---
# virsorter_2

 This is an example of using mamba instead of conda for faster image generation.

To be used with the [fill_template]({{ '/scripts/fill-template.html' | prepend: site.baseurl }}) tool.

```yaml
Bootstrap: docker
From: centos:centos7.6.1810


%environment
    export PATH=$PATH:/opt/software/conda/bin/
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
    /opt/software/conda/bin/conda install -y -c conda-forge mamba
    /opt/software/conda/bin/mamba create -p /opt/software/conda_env -y "python>=3.6" scikit-learn=0.22.1 imbalanced-learn pandas seaborn hmmer prodigal screed ruamel.yaml "snakemake>=5.16,<=5.26" click virsorter=2.0
    source /opt/software/conda/bin/activate /opt/software/conda_env
    #virsorter setup -d /opt/software/conda_env/virsorter-db -j 2
    #ls -l /opt/software/conda_env/virsorter-db/
    #find /opt/software/conda_env/virsorter-db/ -type d -exec chmod a+rx '{}' \;
    #find /opt/software/conda_env/virsorter-db/ -type f -exec chmod a+r  '{}' \;
    cd /opt/software

%runscript
    exec virsorter "$@"

```

This page has been automatically generated from a template file from the [repository](https://github.com/telatin/singularities).
Please, report [issues](https://github.com/telatin/singularities/issues) if you think this template could or should be improved.
