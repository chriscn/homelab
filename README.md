# homelab

## design / overview

### devices

- home.chrisnethercott.co.uk: Raspberry Pi 5 8GB; home assistant, prometheus, graphing, database 
- media.chrisnethercott.co.uk: HP Microserver Gen 8; main media server / NAS
- ?.chrisnethercott.co.uk: Think Station; prometheus, grafana - not sure what to call this yet.

## ansible

There are some specific Ansible configuration choices that I have made.

### variable naming

Variables that are used in roles, should prefix their role name, i.e. the role webserver is `webserver_port`.

Handlers should be named `<role>::<action>`. i.e. `nginx::reload`.

## useful one-liners
- `ansible -m debug -a "var=vars" <your_host>` - debug all variables for a given host
