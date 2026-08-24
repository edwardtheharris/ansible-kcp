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

### Documentation

[![Documentation](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/documentation.yml/badge.svg)](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/documentation.yml)

Build and deploy the GitHub Pages docs.

```{literalinclude} /.github/workflows/documentation.yml
:language: yaml
```

### shell

[![ShellCheck](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/shell.yml/badge.svg)](https://github.com/edwardtheharris/ansible-kcp/actions/workflows/shell.yml)

And ShellCheck never hurt anybody either.

```{literalinclude} /.github/workflows/shell.yml
:language: yaml
```
