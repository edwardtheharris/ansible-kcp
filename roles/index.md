---
abstract: >-
   This is the index for roles to use Kubeadm to configure or reset a
   bare metal Kubernetes cluster.
authors:
   - name: Xander Harris
     email: xandertheharris@gmail.com
date: 2024-07-23
title: Bare Metal HA k8s roles
---

## Roles

There are three roles here, they should be run in a specific order as described
in the usage section below.

### HA K8S Ansible Usage

To use these roles effectively, you'll need have an inventory file available
at {file}`/etc/ansible/hosts.yml` that describes all of the groups listed
in the {file}`site.yml` at the root of this repository. With that in hand,
the way to use these roles is this.

1. Reset any existing cluster.

   ```{code-block} shell
   ansible-playbook -t reset site.yml
   ```

2. Initialize the primary control plane.

   ```{code-block} shell
   ansible-playbook -t init site.yml
   ```

3. Join remaining control planes.

   ```{code-block} shell
   ansible-playbook -t join site.yml
   ```

4. Copy your updated {term}`kubeconfig` from the init role's file folder to
   the appropriate directory.

   ```{code-block} shell
   cp roles/init/files/admin.conf $HOME/.kube/config
   ```

5. Verify that your connection works and the cluster is up.

   ```{code-block} shell
   kubectl get nodes
   ```

   If everything worked you should see output similar to this.

   ```{code-block} shell
   NAME                STATUS   ROLES           AGE   VERSION
   kcp01.example.com   Ready    control-plane   51m   v1.30.3
   kcp02.example.com   Ready    control-plane   50m   v1.30.3
   kcp03.example.com   Ready    control-plane   50m   v1.30.3
   ```

### Individual role details

```{toctree}
:maxdepth: 1
:caption: roles

init/index
join/index
reset/index
```

```{index} roles init
```

```{index} roles; join
```

```{index} roles; reset
```
