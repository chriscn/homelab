# homelab
I run a small 'homelab' and wanted to begin documenting everything (for when I break it); this repository will eventually contain documentation and ansible playbooks.

## Overview

### Hardware

I recently purchased a new HP Microserver Gen 8; which will be my staging / playing around device. I'd like to deploy and manage it through [ansible](https://www.ansible.com/) although I've not used it before.

### Roadmap

Status: **Alpha**

- [ ] Add custom groups for location or machine type
- [ ] Connect and disconnect a VPN before contacting specific hosts

- [ ] Deploying common applications
- [ ] Deploying game applications: Factorio and Minecraft
- [ ] Automatic certificate management
- [ ] Automatic DNS updating
- [ ] Expose some internal services securely to the internet with [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/)
- [ ] Continous Integration / Deployment
- [ ] Status monitoring of individual components and applications

### Domain
Using the `chrisnethercott.co.uk` domain; each device in the student/mum location should have `<name>.chrisnethercott.co.uk` as an SSL certificate if it has any exposed web configuration
