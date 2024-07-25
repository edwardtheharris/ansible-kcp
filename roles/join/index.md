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

## Tasks

This role joins remaining control planes to the new cluster. It should be run
after the init role and before the kv role.

```{literalinclude} /roles/join/tasks/main.yml
:language: yaml
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
