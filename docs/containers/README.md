---
sort: 4
---

# Containers

Usually containers can be built with a standard workflow, using Miniconda,
as described in this website.

This section contains _package specific_ definition files,
for packages that have shown problems using the
standard workflow or for packages not yet available via Miniconda.

At the moment this section is automatially generated from the templates in the repository.

Some definition files will contain template tags like `{package}`, as they
can be used with the [fill_template]({{ '/scripts/fill-template.html' | prepend: site.baseurl }}) tool.

In particular, the **cron job** will check if a template is present with the name
of the required package (eg: `multiqc.tmp`) and use that instead of the default one
(`default.tmp`).


{% include list.liquid %}
