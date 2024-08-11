# homelab

## design / overview

### devices

- net.chrisnethercott.co.uk: Raspberry Pi 4 4GB; network configuration, DNS, DHCP etc
- auth.chrisnethercott.co.uk: Raspberry Pi 4 8GB; ldap, kerberos
- home.chrisnethercott.co.uk: Raspberry Pi 5 8GB; home assistant, prometheus, graphing, database 
- media.chrisnethercott.co.uk: HP Microserver Gen 8; main media server / NAS
- web.nethercott.co.uk: Hetzner VM running Caddy and serving static nethercott.co.uk
- paperless.nethercott.co.uk: Hetzner VM (paperless-ngx)

## ansible

There are some specific Ansible configuration choices that I have made.

### inventories and hosts

If you have your `group_vars` and `host_vars` in the root directory, and the hosts file in a different directory, Ansible will not pick up the `group_vars` and `host_vars` files. This is because Ansible will look for the `group_vars` and `host_vars` in the same directory as the hosts file. This only appears when using playbooks in a different directory to the hosts file.

### variable_naming

Variables that are used in roles, should prefix their role name, i.e. the role webserver is `webserver_port`.

Handlers should be named `<role>::<action>`. i.e. `nginx::reload`.

## useful one-liners
- `ansible -m debug -a "var=vars" <your_host>` - debug all variables for a given host
