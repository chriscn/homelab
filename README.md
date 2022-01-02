# homelab
I run a small 'homelab' and wanted to begin documenting everything (for when I break it); this repository will eventually contain documentation and ansible playbooks.

## Overview

### Hardware

#### Felix

I recently purchased a new HP Microserver Gen 8; which will be my staging / playing around device. I'd like to deploy and manage it through [ansible](https://www.ansible.com/) although I've not used it before.

This HP Microserver runs an Intel Xeon E2-1265v2 with 16GB of ram; along with a 500GB SSD. It is a general purpose server with limited storage, any storage required can be mounted over an NFS share to Tritium.

#### Tritium

My older HP Microserver Gen 8; containing 16GB of ram, Xeon E3-1260L and 16TB (4x4TB) of raw storage. It is managed through unRAID which one parity disk.

#### Raspberry Pi

I manage approximately 10-12 Raspberry Pi's between three family locations. Some have duplicated functions (PiHole, PiVPN etc). One location has six which where I will leverage ansible the most.

### Roadmap

Status: **Alpha**

- [ ] Create custom inventory system (that works will VPN etc) see [#1](https://github.com/chriscn/issues/1)
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
