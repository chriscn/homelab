#!/usr/bin/env sh

ansible-playbook --ask-vault-pass --extra-vars @./extra_vars.yml -i inventory.ini main.yml