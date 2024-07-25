---
abstract: >-
    This role initializes a k8s Control Plane suitable for a high
    availability cluster.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-07-24
title: K8S HA Control Plane Init
---

{term}`HA` Clusters with Kubeadm is helped with use of the tool
{term}`kube-vip`.

## Tasks

The role uses {term}`kubeadm` to handle the initialization of the primary
control plane. It should be run after the reset role and before the join role.

```{literalinclude} /roles/init/tasks/main.yml
:language: yaml
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
