# stage3 specfile
# used to build a stage4
subarch: amd64
version_stamp: qemu-x86_64-nomultilib-20150521
target: stage4
rel_type: container
profile: steveeJ:container/linux/amd64-native/qemu-x86_64
snapshot: 20150521
source_subpath: ../download/stage3-amd64-nomultilib-20150521
portage_confdir: /var/tmp/catalyst/confdir
pkgcache_path: packages/container/amd64-nomultilib
portage_overlay: /var/tmp/catalyst/overlay
stage4/packages: @profile
stage4/fsscript: /var/tmp/catalyst/builds/container.fsscript
#stage4/root_overlay: qemu-x86_64_root_overlay
stage4/empty: /var/tmp /var/cache
