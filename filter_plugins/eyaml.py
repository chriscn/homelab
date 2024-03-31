"""Decrypt secrets using Hiera's EYAML."""
# Credit: https://github.com/epfl-si/ansible-module-eyaml

import os
import re
import subprocess

from ansible.errors import AnsibleFilterError


def eyaml(encrypted, keys):
    os.environ["PRIVKEY"] = slurp(keys["priv"])
    os.environ["PUBKEY"] = slurp(keys["pub"])
    encrypted = re.sub(r"\s", "", encrypted, re.MULTILINE)
    cmd = [
        "eyaml",
        "decrypt",
        "--pkcs7-private-key-env-var=PRIVKEY",
        "--pkcs7-public-key-env-var=PUBKEY",
    ]

    proc = subprocess.run(
        cmd + ["-s", encrypted],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        check=True,
    )

    # What a nice surprise: eyaml doesn't manage its exit code correctly.
    output = proc.stdout

    if (not output) and " @ " in proc.stderr:
        raise AnsibleFilterError(
            "Error running %s: %s" % (" ".join(cmd + ["-s", "..."]), proc.stderr)
        )

    if "\n" not in output.rstrip():
        output = output.rstrip()

    return output


def slurp(path):
    return open(path).read()


class FilterModule(object):
    def filters(self):
        return {"eyaml": eyaml}
