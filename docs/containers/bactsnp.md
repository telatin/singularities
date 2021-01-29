---
sort: 6
---
# Bactsnp


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
    /opt/software/conda/bin/conda create -p /opt/software/conda_env -y samtools picard art mummer
    source /opt/software/conda/bin/activate /opt/software/conda_env
    wget https://github.com/IEkAdN/BactSNP/releases/download/v1.1.0/bactsnp-1.1.0.linux64.tgz
    tar xf bactsnp-1.1.0.linux64.tgz 
    rm bactsnp-1.1.0.linux64.tgz
    cd bactsnp-1.1.0.linux64
    make
    mv bactsnp /opt/software/conda_env/bin/
    cd /opt/software

%runscript
    exec bactsnp "$@"

```

This page has been automatically generated from a template file from the [repository](https://github.com/telatin/singularities).
Please, report [issues](https://github.com/telatin/singularities/issues) if you think this template could or should be improved.
