---
abstract: >-
   This is a set of roles that will initialize a primary control plane,
   then join secondary and tertiary control planes to a HA k8s cluster.
authors:
   - name: Xander Harris
     email: xandertheharris@gmail.com
date: 2024-03-08
title: Ansible Bare Metal HA K8S
---

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-kcp/ansible.yml?branch=main&style=flat-square&logo=ansible&label=Ansible%20Lint)
![GitHub CodeQL](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-kcp/codeql.yml?branch=main&style=flat-square&logo=githubactions&label=CodeQL)
[![GitHub Pages Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-kcp/pages.yml?branch=main&style=flat-square&logo=githubpages&label=GitHub%20Pages)](https://edwardtheharris.github.io/ansible-kcp/)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-kcp/shell.yml?branch=main&style=flat-square&logo=gnubash&label=ShellCheck)

## Playbook

```{rubric} site.yml
```

```{literalinclude} ./site.yml
```

### Roles

```{toctree}
:maxdepth: 3
:caption: roles

roles/index
```

```{index} ansible; roles
```

```{graphviz}
digraph roles {
   reset -> init -> join -> kv
}
```

## Readme

```{toctree}
:maxdepth: 3

cicd
license
readme
security
```

```{index} metadata; repository
```

## References

- [community.crypto.x509_certificate](https://docs.ansible.com/ansible/latest/collections/community/crypto/x509_certificate_module.html)
- [How to create a small CA](https://docs.ansible.com/ansible/latest/collections/community/crypto/docsite/guide_ownca.html)

### Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`

### Glossary

```{glossary}
Calico
   Calico is a networking and security solution that enables Kubernetes
   workloads and non-Kubernetes/legacy workloads to communicate seamlessly and
   securely. More information is available
   [here](https://docs.tigera.io/calico/latest/about/).

CNI
   Container Network Interface used to manage networking between and inside
   clusters.

HA
   High Availability; in this context we mean specifically HA k8s clusters
   as described
   [here](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/).

kubeconfig
   A file that contains context and authentication information for one or more
   {term}`K8S` clusters. Usually kept in a folder in a user's home directory
   ({file}`.kube/config`).

kube-vip
   A network stack that can be used to enable cloud-style network resources
   on a bare metal {term}`K8S` cluster. More information is available
   [here](https://kube-vip.io/docs/installation/static/).

kubie
   A handy tool for switching k8s contexts and namespaces. More information is
   available [here](https://github.com/sbstp/kubie).

K8S
   Kubernetes; Ancient Greek for navigator or guide, in modern English usage
   it is a container orchestration system designed by Google and documented
   [here](https://kubernetes.io).
```
