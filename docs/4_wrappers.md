---
sort: 4
permalink: /wrappers
---

# Wrappers and launchers

```note
Under costruction
```

A basic wrapper can be as follows:
```bash launcher.sh
#!/bin/bash
DIR=`dirname $(readlink -f $0)`
IMG=/path/to/singularity_image.simg
singularity exec $IMG $(basename "$0") "$@"
```

In this way if we have a single image with multiple binaries to expose, we can make as many symbolic links as needed to the launcher that will execute `$(basename "$0")` as binary.
