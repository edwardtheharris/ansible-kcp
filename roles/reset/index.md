---
abstract: This role resets the control planes in your inventory with Kubeadm.
authors:
   - name: Xander Harris
     email: xandertheharris@gmail.com
date: 2024-07-23
title: Reset Cluster
---

## Reset Role Usage

This role should generally be executed first to attempt to create a fresh
environment.

```{literalinclude} /roles/reset/tasks/main.yml
:language: yaml
```

```{index} role; reset
```
