---
abstract: Basic information about the CI/CD processes in this repo.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-07-23
title: CI/CD
---

```{contents}
```

## Dependabot

Stay away from zero days with Dependabot.

```{literalinclude} /.github/dependabot.yml
:language: yaml
```

## Workflows

GitHub Actions provides a pretty complete CI/CD system and they'll let you
run a lot of pipelines for free.

### Ansible Lint

[![Ansible Lint](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/ansible.yml/badge.svg)](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/ansible.yml)

This is the configuration for the various lint tools used here.

```{literalinclude} /.ansible-lint
:language: yaml
```

### codeql

[![CodeQL](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/codeql.yml/badge.svg)](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/codeql.yml)

The CodeQL workflow provided by GitHub is actually pretty good also.

```{literalinclude} /.github/workflows/codeql.yml
:language: yaml
```

### Documentation

[![Documentation](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/documentation.yml/badge.svg)](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/documentation.yml)

Build and deploy the GitHub Pages docs.

```{literalinclude} /.github/workflows/documentation.yml
:language: yaml
```

### OSSAR

[![OSSAR](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/ossar.yml/badge.svg)](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/ossar.yml)

Build and deploy the GitHub Pages docs.

```{literalinclude} /.github/workflows/ossar.yml
:language: yaml
```

### shell

[![ShellCheck](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/shell.yml/badge.svg)](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/shell.yml)

And ShellCheck never hurt anybody either.

```{literalinclude} /.github/workflows/shell.yml
:language: yaml
```
