---
abstract: This is a collection of Ansible playbooks that will create a CA usable
   for Kubernetes and etcd clusters.
authors:
   - name: Xander Harris
     email: xandertheharris@gmail.com
date: 2024-03-08
title: Ansible Bare Metal K8S
---

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-kcp/ansible.yml?branch=main&style=flat-square&logo=ansible&label=Ansible%20Lint)
![GitHub CodeQL](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-kcp/codeql.yml?branch=main&style=flat-square&logo=githubactions&label=CodeQL)
[![GitHub Pages Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-kcp/pages.yml?branch=main&style=flat-square&logo=githubpages&label=GitHub%20Pages)](https://edwardtheharris.github.io/ansible-kcp/)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/ansible-kcp/shell.yml?branch=main&style=flat-square&logo=gnubash&label=ShellCheck)

## Playbook

```{rubric} site.yml
```

```{autoyaml} ./site.yml
```

### Roles

```{toctree}
:maxdepth: 1
:caption: roles

roles/index
```

```{index} ansible; roles
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

## Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
