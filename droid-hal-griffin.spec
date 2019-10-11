# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device griffin
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto Z

%define installable_zip 1
%define droid_target_aarch64 1
%define makefstab_skip_entries /vendor /dev/stune /sys/fs/pstore /dev/cpuctl
%define straggler_files \
/property_contexts \
/service_contexts \
/vendor \
/wlan_carrier_bin.sh \
<<<<<<< HEAD
/init.mmi.boot.sh \
/init.mmi.laser.sh \
/init.mmi.touch.sh \
=======
>>>>>>> a7663c638876957eb055a4175194c670c01a9cef
%{nil}

%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

