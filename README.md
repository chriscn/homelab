# Christopher's Homelab

This repository contains the code and configuration for my homelab. It is a collection of various services and applications that I run on my home network. The goal of this repository is to provide a central location for all of the code and configuration for my homelab.

## Bootstrapping

Unfortunately, there is a small amount of manual configuration that needs to be done to get everything up and running. I'm assuming that your network is setup. The initial user account on each device is `christopher`, the initial `playbook/bootstrap.yml` will create a passwordless sudo user, with a specific authorized ssh key.
