#!/usr/bin/env python3
"""
Generates kokoro config files based on template.
"""

DEFAULT_ARTIFACTS = """\
    regex: "**/*result*.xml"
    regex: "**/*sponge_log.xml"
    regex: "**/.ninja_log"
    regex: "**/pack.log"
    regex: "**/place.log"
    regex: "**/route.log"
    regex: "**/*_sv2v.v.log"
    regex: "**/*_qor.csv"
    regex: "**/vivado.log"
    regex: "**/core"
    regex: "**/*.bit"\
"""

INSTALL = """\
    regex: "**/symbiflow-*.tar.xz"\
"""

DB_FULL = """\
# Format: //devtools/kokoro/config/proto/build.proto

# Generated from .github/kokoro/kokoro-cfg.py
# To regenerate run:
# cd .github/kokoro/ && python3 kokoro-cfg.py

build_file: "symbiflow-arch-defs-%(kokoro_type)s-%(arch)s/.github/kokoro/%(arch)s.sh"

timeout_mins: 1200

action {
  define_artifacts {
    # File types
%(artifacts)s
    strip_prefix: "github/symbiflow-arch-defs-%(kokoro_type)s-%(arch)s/"
  }
}

env_vars {
  key: "KOKORO_TYPE"
  value: "%(kokoro_type)s"
}

env_vars {
  key: "KOKORO_DIR"
  value: "symbiflow-arch-defs-%(kokoro_type)s-%(arch)s"
}

env_vars {
  key: "SYMBIFLOW_ARCH"
  value: "%(arch)s"
}
"""

for type in ['tests', 'docs', 'ice40', 'testarch', 'xc7', 'xc7-vendor',
             'xc7a200t', 'xc7a200t-vendor', 'ql', 'install', 'install-200t']:
    if 'install' in type:
        artifacts = INSTALL
    else:
        artifacts = DEFAULT_ARTIFACTS

    with open("continuous-%s.cfg" % type, "w") as f:
        f.write(
            DB_FULL % {
                'arch': type,
                'artifacts': artifacts,
                'kokoro_type': 'continuous',
            }
        )

    with open("presubmit-%s.cfg" % type, "w") as f:
        f.write(
            DB_FULL % {
                'arch': type,
                'artifacts': artifacts,
                'kokoro_type': 'presubmit',
            }
        )
