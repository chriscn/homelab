# homelab
I run a small 'homelab' and wanted to begin documenting everything (for when I break it); this repository will eventually contain documentation and ansible playbooks.

## Overview

### Hardware

I recently purchased a new HP Microserver Gen 8; which will be my staging / playing around device. I'd like to deploy and manage it through [ansible](https://www.ansible.com/) although I've not used it before.

### Features

Status: **Beta**

- [ ] Deploying common applications
- [ ] Deploying game applications: Factorio and Minecraft
- [ ] Automatic certificate management
- [ ] Automatic DNS updating
- [ ] Expose some internal services securely to the internet with [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/)
- [ ] Continous Integration / Deployment
- [ ] Status monitoring of individual components and applications

### Folder directory structure
`<location>/<name>`
- `location`: location in which the physical machine resides
- `name`: usually the hostname of the machine

### Domain
Using the `chrisnethercott.co.uk` domain; each device in the student/mum location should have `<name>.chrisnethercott.co.uk` as an SSL certificate if it has any exposed web configuration
