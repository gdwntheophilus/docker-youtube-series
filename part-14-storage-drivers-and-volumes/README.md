# Docker storage drivers and volumes

| Storage Driver | Description
|---|---|
overlay2 |	overlay2 is the preferred storage driver for all currently supported Linux distributions, and requires no extra configuration.
fuse-overlayfs	| fuse-overlayfsis preferred only for running Rootless Docker on a host that does not provide support for rootless overlay2. On Ubuntu and Debian 10, the fuse-overlayfs driver does not need to be used, and overlay2 works even in rootless mode. Refer to the rootless mode documentation for details.
btrfs and zfs	|The btrfs and zfs storage drivers allow for advanced options, such as creating “snapshots”, but require more maintenance and setup. Each of these relies on the backing filesystem being configured correctly.
vfs	|The vfs storage driver is intended for testing purposes, and for situations where no copy-on-write filesystem can be used. Performance of this storage driver is poor, and is not generally recommended for production use.
aufs	|The aufs storage driver Was the preferred storage driver for Docker 18.06 and older, when running on Ubuntu 14.04 on kernel 3.13 which had no support for overlay2. However, current versions of Ubuntu and Debian now have support for overlay2, which is now the recommended driver.
devicemapper	|The devicemapper storage driver requires direct-lvm for production environments, because loopback-lvm, while zero-configuration, has very poor performance. devicemapper was the recommended storage driver for CentOS and RHEL, as their kernel version did not support overlay2. However, current versions of CentOS and RHEL now have support for overlay2, which is now the recommended driver.
overlay	|The legacy overlay driver was used for kernels that did not support the “multiple-lowerdir” feature required for overlay2 All currently supported Linux distributions now provide support for this, and it is therefore deprecated.

## Overlay Driver
The overlay2 driver natively supports up to 128 lower OverlayFS layers. This capability provides better performance for layer-related Docker commands such as docker build and docker commit , and consumes fewer inodes on the backing filesystem.

![](overlay_constructs.jpg)

## Recommendations provided by docker

|Linux | distribution	|Recommended storage drivers	Alternative drivers
|---|---|---|
Ubuntu	|overlay2	|overlay¹, devicemapper², aufs³, zfs, vfs
Debian	|overlay2	|overlay¹, devicemapper², aufs³, vfs
CentOS	|overlay2	|overlay¹, devicemapper², zfs, vfs
Fedora	|overlay2	|overlay¹, devicemapper², zfs, vfs
SLES 15	|overlay2	|overlay¹, devicemapper², vfs
RHEL	|overlay2	|overlay¹, devicemapper², vfs

## How to check what is the storage driver used by docker

```docker
docker info 
(or)
docker info | grep -i storage
```