---
sort: 2
permalink: /install
---
# Install Singularity

## What version
Some HPC clusters still provide an outdated version of [Singularity](https://sylabs.io/docs/),
while it's tempting to install the latest version (currently [3.7](https://sylabs.io/guides/3.7/user-guide))
when installing it into a Virtual Machine (VM).

In this repository we describe definition files that have been tested with
**Singularity 2.4.2**. The oldest version that is documented in the offical
website is 2.5, so also that version has been tested for some containers.


## Installing Singularity 2.5

:link: [documentation](https://sylabs.io/guides/2.5/user-guide/)

Short guide:

```bash

sudo apt-get update && sudo apt-get install python dh-autoreconf build-essential libarchive-dev

git clone https://github.com/sylabs/singularity.git
cd singularity
git fetch --all
git checkout 2.5.0
./autogen.sh
./configure --prefix=/usr/local
make
sudo make install
```

## Installing Singularity 2.4

:link: [documentation](https://sylabs.io/guides/2.5/user-guide/installation.html#singularity-vagrant-box)
