# homelab
I run a small 'homelab' and wanted to begin documenting everything (for when I break it); this repository will eventually contain documentation and ansible playbooks.

## Hardware

### Felix (HP Microserver Gen 8)

I recently purchased a new HP Microserver Gen 8; which will be my staging / playing around device. I'd like to deploy and manage it through [ansible](https://www.ansible.com/) although I've not used it before.

This HP Microserver runs an Intel Xeon E2-1265v2 with 16GB of ram; along with a 500GB SSD. It is a general purpose server with limited storage, any storage required can be mounted over an NFS share to Tritium.

### Tritium (HP Microserver Gen 8)

My older HP Microserver Gen 8; containing 16GB of ram, Xeon E3-1260L and 16TB (4x4TB) of raw storage. It is managed through unRAID with one parity disk. There are a few NFS shares that will be mounted

### TBC (Dell R720)

This is my latest addition to the rack; it is currently powered off since I haven't yet found a use for it however it is my most powerful server. The other issue is that it is stored in a cupboard and quite out of the way. I'd like to dust it off when I move house and try and get it to work with the rest of the Network. I believe it has 16Cores and 256GB of Ram.
