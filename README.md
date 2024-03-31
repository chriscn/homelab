# homelab

## eyaml

I've utilised `hiera-eyaml` to encrypt sensitive data. You can install it via `gem install hiera-eyaml`. There is a custom filter plugin found in `filter_plugins/eyaml.py` which is used to decrypt the data.

## useful one-liners
- `ansible -m debug -a "var=vars" <your_host>` - debug all variables for a given host
