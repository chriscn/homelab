# homelab

## eyaml

I've utilised `hiera-eyaml` to encrypt sensitive data. You can install it via `gem install hiera-eyaml`. There is a custom filter plugin found in `filter_plugins/eyaml.py` which is used to decrypt the data.

The customised `eyaml.py` file contains the path of the keys used to encrypt / decrypt the files. They are stored in `keys/` and are not included in this repository.

Run `eyaml createkeys` to generate the keys and edit the various `host_vars` and `group_vars` with your sensitive data.

## useful one-liners
- `ansible -m debug -a "var=vars" <your_host>` - debug all variables for a given host
