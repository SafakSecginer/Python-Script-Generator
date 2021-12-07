#!/bin/sh

echo -e -n "\x02" | dd of=/dev/mtd0 bs=1 count=1 seek=6
echo -e -n "\xA5" | dd of=/dev/mtd0 bs=1 count=1 seek=12
echo -e -n "\x10" | dd of=/dev/mtd0 bs=1 count=1 seek=13
reboot