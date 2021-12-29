# homelab
I run a small 'homelab' and wanted to begin documenting everything (for when I break it); this repository will eventually contain documentation and ansible playbooks.
## naming structure
**<location>/<name>**
- `location`: location in which the physical machine resides
- `name`: usually the hostname of the machine
## domain
Using the `chrisnethercott.co.uk` domain; each device in the student/mum location should have `<name>.chrisnethercott.co.uk` as an SSL certificate if it has any exposed web configuration