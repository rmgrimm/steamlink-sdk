#!/bin/bash
#

VERSION="3.1.2"
DOWNLOAD_URL="https://download.samba.org/pub/rsync/rsync-${VERSION}.tar.gz"

TOP=$(cd `dirname "${BASH_SOURCE[0]}"` && pwd)
if [ "${MARVELL_SDK_PATH}" = "" ]; then
	MARVELL_SDK_PATH="$(cd "${TOP}/../.." && pwd)"
fi
if [ "${MARVELL_ROOTFS}" = "" ]; then
	source "${MARVELL_SDK_PATH}/setenv.sh" || exit 1
fi
BUILD="${TOP}/rsync-build"
SRC="${TOP}/rsync-${VERSION}"

#
# Download the source
#
if [ ! -d "${SRC}" ]; then
	wget $DOWNLOAD_URL -O- | tar xzS || exit 1
fi

#
# Build it
#
mkdir -p "${BUILD}"
pushd "${BUILD}"
"${SRC}"/configure $STEAMLINK_CONFIGURE_OPTS || exit 1
make || exit 1
"${CROSS}"strip -s rsync
popd

#
# All done!
#
echo "Build complete!"
echo
echo "To copy rsync to the Steam Link, run:"
echo "scp \"${BUILD}/rsync\" root@192.168.1.50:/home/steam/bin/"
echo "    (be sure to replace 192.168.1.50 with the IP of your Steam Link!)"
