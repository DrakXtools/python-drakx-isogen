from drakx.isoimage import IsoImage
from drakx.releaseconfig import ReleaseConfig
from drakx.media import Media
from drakx.distribution import Distribution
import os

config = ReleaseConfig(distribution="Mageia", version="6", codename="Midgetty", product="LXDE", subversion="Stable", medium="CD", outdir=".", repopath="http://ftp.acc.umu.se/mirror/mageia/distrib/6")

srcdir = "./"
rpmsrate = "/usr/share/meta-task/rpmsrate-raw"
compssusers = "/usr/share/meta-task/compssUsers.pl"
filedeps = srcdir + "file-deps"


media = []
for m in ["core"]:#, "nonfree", "tainted":#, "moondrake": #"main", "main-updates", "contrib", "contrib-updates", "non-free", "non-free-updates", "restricted", "restricted-updates":
    media.append(Media(m))

includelist = []
for l in ["basesystem_minimal"]:#, "languages", "firmware_nonfree", "theme-moondrake"]:
    includelist.append(srcdir + "lists/" + l)

includelist64 = includelist + [srcdir + "lists/" + "kernel64_mini"]

excludelist = []
for e in ["exclude", "exclude_mini", "exclude_tofix", "exclude_nonfree"]:
    excludelist.append(srcdir + "lists/" + e)

x86_64 = Distribution(config, "x86_64", media, includelist64, excludelist, rpmsrate, compssusers, filedeps, synthfilter=".xz:xz --text",  root="/usr/lib64/drakx-installer-stage2", stage1="/usr/lib64/drakx-installer-images/isolinux/x86_64/all.rdz", stage2="/usr/lib64/drakx-installer-stage2/install/stage2/mdkinst.sqfs", advertising="/usr/share/drakx-installer-advertising/install/extra/advertising")

distrib=[x86_64]

image = IsoImage(config, distrib, maxsize=800)
