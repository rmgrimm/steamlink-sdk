
This is an example of building rsync, a useful tool for backing up files across a network (among many other things). For example, this facilitates full system backups from a backuppc server.

To build, just run ./build_steamlink.sh and it should download, configure, and compile rsync. The output can be found inside the rsync-build subdirectory.

You should then enable ssh on your device and use scp to copy it on and then run it from an ssh session on the Steam Link.
