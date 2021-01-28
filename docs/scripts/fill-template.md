---
sort: 2
---
# Generate definition file

A very naive templating system allows to generate definition files for
tools available via Miniconda.

Given the assumption that we need to install a specific version of a tool, we
can use a template and a `fill_template.pl` script to generate a basic definition
file.

### Template

We need three variables filled: the tool name in conda (_e.g._ `spades`),
the version we want to install (_e.g._ `3.14.1`) and the name of the
binary to execute with the image (_e.g._ `spades.py`).

```text
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

    cd /opt/software

%runscript
    exec {binary} "$@"
```

### Fill template script

```perl
#!/usr/bin/env perl
use 5.012;
use FindBin qw($RealBin);
my $template = shift @ARGV;
die "USAGE:
  templater.pl TemplateFile Var=Value  V2=Value2...
" if (! -e "$template");
my %values = ();

for (my $i = 0; $i <= $#ARGV; $i++) {
  my ($var, $value) = split /=/, $ARGV[$i];
  die "Syntax error: expecting var=value\n" unless ($value);
  say STDERR "$var=$value";
  $values{$var} = $value;
}
# Override template
if (-e "$RealBin/templates/$values{'package'}.tmp") {
 print STDERR " * Using custom template $RealBin/templates/$values{package}.tmp";
 $template =  "$RealBin/templates/$values{'package'}.tmp";
}


my $template = load_template($template);
say $template;
sub load_template {
 my $file = shift @_;
 open(my $i, '<', "$file") || die "Unable to open file: $file\n";
 while (my $line = readline($i) ) {
  while ($line =~/{(\w+)}/g) {
   my $t = $1;
   say STDERR "template_requires> $1";
   if ($values{$t}) {
      $line =~s/{$t}/$values{$t}/g;
   }
  }
  $template .= $line;


 }
 return ($template);
}

```

Example usage:
```bash
perl fill_template.pl package=spades binary=spades.py version=3.14.1 > spades-3.14.1.def

sudo singularity buid spades_3.14.1 spades-3.14.1.def
```
