# homelab

## ansible

There are some specific Ansible configuration choices that I have made.

### variable_naming

Variables that are used in roles, should prefix their role name, i.e. the role webserver is `webserver_port`.

Handlers should be named `<role>::<action>`. i.e. `nginx::restart`.

### hash_behaviour

The `hash_behaviour` has been set to `merge`; instead of replacing variables we join them together, this allows for nested or hierarchical data more easily remove duplicates.

For example, one might have two variables a `all.yaml` group_vars and a specific host var.

```yaml
users:
  admin: my-secret-admin-passwd
  operator: privileged-user
```

```yaml
users:
  operator: an-override
  user: no-access
```

This would produce the following:

```yaml
users:
  admin: my-secret-admin-passwd
  operator: an-override
  user: no-access
```

This is not the default behaviour and one must remain mindful when using other roles.

## eyaml

I've utilised `hiera-eyaml` to encrypt sensitive data. You can install it via `gem install hiera-eyaml`. There is a custom filter plugin found in `filter_plugins/eyaml.py` which is used to decrypt the data.

The customised `eyaml.py` file contains the path of the keys used to encrypt / decrypt the files. They are stored in `keys/` and are not included in this repository.

Run `eyaml createkeys` to generate the keys and edit the various `host_vars` and `group_vars` with your sensitive data.

## useful one-liners
- `ansible -m debug -a "var=vars" <your_host>` - debug all variables for a given host
