#/usr/bin/env python3
import os, re
from string import Template
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

scriptdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.realpath(os.path.join(scriptdir, os.pardir))
templates = os.path.join(parentdir, 'scripts/templates')
outputdir = os.path.join(parentdir, 'docs/containers')
basenumber = 1
template = """---
sort: $progressive
---
# $title

$description
To be used with the [fill_template]({{ '/scripts/fill-template.html' | prepend: site.baseurl }}) tool.

```yaml
$yaml
```

This page has been automatically generated from a template file from the [repository](https://github.com/telatin/singularities).
Please, report [issues](https://github.com/telatin/singularities/issues) if you think this template could or should be improved.
"""
temp_obj = Template(template)

def dumpDefinition(deffile, outfile):
    global basenumber
    basenumber += 1
    filebasename = os.path.basename(os.path.splitext(deffile)[0])
    inputfile = open(deffile, "r")
    header = ""
    yaml = ""
    for line in inputfile.readlines():
        if line[:2] == '##':
            # comment -> md
            header += line[2:]
        else:
            yaml += line
    inputfile.close()

    writer = open(outfile, 'wt', encoding='utf-8')
    writer.write(temp_obj.substitute(
        progressive=basenumber,
        title=filebasename.capitalize(),
        description=header,
        yaml=yaml))


# Parse all .tmp files in ../scripts/templates/
for (dirpath, dirnames, filenames) in os.walk(templates):
    filenames = sorted(filenames)
    for f in filenames:
        if re.search('.tmp', f):
            inputfile  = os.path.join(templates,f)
            outputfile = os.path.join(outputdir, os.path.basename(os.path.splitext(inputfile)[0] + '.md'))
            eprint(f"{inputfile} --> {outputfile}")
            dumpDefinition(inputfile, outputfile)
