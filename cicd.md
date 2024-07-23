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

```{autoyaml} .github/dependabot.yml
```

## Workflows

GitHub Actions provides a pretty complete CI/CD system and they'll let you
run a lot of pipelines for free.

### codeql

The CodeQL workflow provided by GitHub is actually pretty good also.

```{autoyaml} .github/workflows/codeql.yml
```

### pages

Build and deploy the GitHub Pages docs.

```{autoyaml} .github/workflows/pages.yml
```

### shell

And ShellCheck never hurt anybody either.

```{autoyaml} .github/workflows/shell.yml
```

## Lint

This is the configuration for the various lint tools used here.

### ansible-lint

```{autoyaml} .ansible-lint
```
