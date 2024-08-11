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

### codeql

The CodeQL workflow provided by GitHub is actually pretty good also.

```{literalinclude} /.github/workflows/codeql.yml
:language: yaml
```

### Documentation

Build and deploy the GitHub Pages docs.

```{literalinclude} /.github/workflows/documentation.yml
:language: yaml
```

### OSSAR

Build and deploy the GitHub Pages docs.

```{literalinclude} /.github/workflows/ossar.yml
:language: yaml
```

### shell

And ShellCheck never hurt anybody either.

```{literalinclude} /.github/workflows/shell.yml
:language: yaml
```

## Lint

This is the configuration for the various lint tools used here.

### ansible-lint

```{literalinclude} /.ansible-lint
:language: yaml
```
