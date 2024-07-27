---
abstract: >-
    This role creates and installs a Kube-VIP manifest onto all control planes.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-07-24
title: HA K8S Kube-VIP
---

Deployment of HA K8S Clusters with Kubeadm is helped with use of the tool
{term}`kube-vip`. This role uses the static pods version of the network,
which is best for bare metal deployments.

## Tasks

This role enables {term}`kube-vip` for cluster networking. This role should
be run after the join role and before the flannel role.

```{literalinclude} /roles/kv/tasks/main.yml
:language: yaml
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
