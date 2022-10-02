<div align="center">

# Christopher's Homelab

<!-- ANCHOR: introduction -->

This project aims to be a fully document, and redeploy my local homelab. It achieves this by using [Infrastructure as Code](https://en.wikipedia.org/wiki/Infrastructure_as_code) and [GitOps](https://www.weave.works/technologies/gitops) to automate provisioning, deploying, operating, and self updating. With the aim being that everything is documented within service files.

It is heavily inspired by [khuedon](https://github.com/khuedoan/homelab) in terms of project structure and setup.

<!-- ANCHOR_END: introduction -->

</div>

## Overview

Status: **Early Alpha**

This section provides a high level overview of the project. Please see the [documentation](#deployment) for further information.

### Hardware

Each server at the moment has a specific role; one is Storage, one is for running services such as [Home Assistant](https://home-assistant.io), and one just sits for me to play with.

All three are `HP Microserver Gen8` with the following specs:

- CPU: `Xeon E3-1265L v3`
- RAM: `16GB DDR3 ECC`
- Storage: `SSD`
- Network: `2x 1GB Port Bonded` + `iLO Management`

Eventually I'd like to standardize all their configurations, just to have a singular SSD and then block storage. Ultimately to mount over the network with [GlusterFS](https://www.gluster.org/) across all three nodes. This should lead me with ~48TB of raw storage across the network.

In the future I'd likely fit all three with a 10GB Network Card linking with a [MikroTik](https://mikrotik.com/product/crs305_1g_4s_in) switch, so that they can operate at 10GB over an internal network.

### Deployment

Currently all applications are detailed in [docker-compose.yml](./docker-compose.yml). There is an ansible [playbook](./playbook/deploy-docker.yml); which is responsible for deploying the new changes in the compose file.

```zsh
ansible-playbook playbook/deploy-docker.yml -K 
```

The above command will deploy the changes to the `docker` node.
