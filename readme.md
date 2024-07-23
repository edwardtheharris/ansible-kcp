---

abstract: >-
  The readme for some Ansible roles for managing bare metal k8s clusters.
authors: Xander Harris
date: 2024-03-08
title: Ansible Bare Metal K8S
---

## Assumptions

The default configuration assumes a vault password exists at
{file}`/etc/ansible/vault`. It also assumes the inventory file is in YAML format
and located at {file}`/etc/ansible/hosts.yaml`

### Fact Caching

The default configuration uses fact caching with Redis running on the controller
with the default port.

## Usage

You can find an example inventory file below, this inventory is intended
to house a Kubernetes cluster with a pair of control planes that are members
of a Samba Active Directory Domain that contains a pair of controllers and
is responsible for authentication, file, and routing services.

```{code-block} yaml
:caption: /etc/ansible/hosts.yaml

kcp:
  hosts:
    kcp01.example.com:
      ansible_user: 1.2.3.4
    kcp02.example.com:
      ansible_user: 1.2.3.4
```

```{toctree}
:caption: Other Information

cicd
license
security
```
