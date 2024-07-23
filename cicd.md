---
abstract: Basic information about the CI/CD processes in this repo.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-07-23
title: GitHub Actions configuration
---

## Dependabot

Stay away from zero days with Dependabot.

<!--
```{autoyaml} .github/dependabot.yml
```
-->

````{sidebar} Dependabot Config
To get started with Dependabot version updates, you'll need to specify which
package ecosystems to update and where the package manifests are located.

```{note}
Please see the documentation for all configuration
[options](https://docs.github.com/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file).
```

```{literalinclude} /.github/dependabot.yml
:language: yaml
```
````

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
