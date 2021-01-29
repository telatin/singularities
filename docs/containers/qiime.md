---
sort: 9
---
# Qiime

 Qiime2 requires the download of a conda environment file

To be used with the [fill_template]({{ '/scripts/fill-template.html' | prepend: site.baseurl }}) tool.

```yaml
BootStrap: yum
OSVersion: 7
MirrorURL: http://yum-repos.hpccluster/centos/7/os/x86_64/
Include: yum
UpdateURL: http://yum-repos.hpccluster/centos/7/updates/x86_64/

    
%environment
  source /opt/software/conda/bin/activate /opt/software/conda_env


%post
  yum -y install epel-release
  yum -y groupinstall "Development Tools"

  mkdir -p /opt/software
  cd /opt/software

  curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  sh ./Miniconda3-latest-Linux-x86_64.sh -p /opt/software/conda -b
  /opt/software/conda/bin/conda config --add channels r
  /opt/software/conda/bin/conda config --add channels defaults
  /opt/software/conda/bin/conda config --add channels conda-forge
  /opt/software/conda/bin/conda config --add channels bioconda

  curl -OL https://raw.githubusercontent.com/qiime2/environment-files/master/{version}/release/qiime2-{version}-py36-linux-conda.yml
  /opt/software/conda/bin/conda env create -p /opt/software/conda_env -f /opt/software/qiime2-{version}-py36-linux-conda.yml

%runscript
  exec qiime "$@"

```

This page has been automatically generated from a template file from the [repository](https://github.com/telatin/singularities).
Please, report [issues](https://github.com/telatin/singularities/issues) if you think this template could or should be improved.
