---
abstract: >-
    This role joins additional control planes to a high availability k8s
    cluster.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-07-24
title: HA K8S Join Control Planes
---

[HA Clusters with Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)
is helped with use of the tool
[kube-vip](https://kube-vip.io/docs/installation/static/).

More information about the process for HA setup is available
[here](https://github.com/kubernetes/kubeadm/blob/main/docs/ha-considerations.md#kube-vip).

A handy tool for switching k8s contexts is called
[kubie](https://github.com/sbstp/kubie).

## Tasks

```{literalinclude} /roles/join/tasks/main.yml
:language: yaml
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
