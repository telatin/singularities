---
sort: 1
---
# Definition files

This section is automatically generated and currently **under costruction**:
some new files will be added soon and a cleanup will remove some files that
are no longer necessary.

Some definition files will contain template tags like `{package}`, as they
can be used with the [fill_template]({{ '/scripts/fill-template.html' | prepend: site.baseurl }}) tool.

In particular, the **cron job** will check if a template is present with the name
of the required package (eg: `multiqc.tmp`) and use that instead of the default one
(`default.tmp`).
