# This file is part of dnf-urpm
# Copyright (C) 2015 Neal Gompa
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
dnf_action = None

def opmodes_dnf_args(args):
    opmodes_args = []
    global dnf_action
    if args.auto_select is True:
        dnf_action = "upgrade"
        opmodes_args.append("--cacheonly")
    elif args.auto_update is True:
        dnf_action = "upgrade"
        opmodes_args.append("--refresh")

    if args.auto_orphans is True:
        opmodes_args.append("--allowerasing")

    return opmodes_args

def pkgselect_dnf_args(args):
    pkgselect_args = []
    global dnf_action
    if args.auto is True:
        pkgselect_args.append("-y")
    if args.no_recommends is True:
        pkgselect_args.append("--setopt=install_weak_deps=False")
    if args.allow_suggests is True:
        pkgselect_args.append("--setopt=install_weak_deps=True")
    if args.buildrequires is True:
        if dnf_action is None:
            dnf_action = "builddep"
        else:
            sys.exit("Invalid argument sequence!")

    return pkgselect_args


def pkgproc_dnf_args(args):
    pkgproc_args = []
    global dnf_action
    if args.downgrade is True:
        if dnf_action is None:
            dnf_action = "downgrade"
        else:
            sys.exit("Invalid argument sequence!")
    elif args.replacepkgs is True:
        if dnf_action is None:
            dnf_action = "reinstall"
        else:
            sys.exit("Invalid argument sequence!")
    return pkgproc_args


def process(args):
    global dnf_action
    dnf_install_args = opmodes_dnf_args(args) + pkgselect_dnf_args(args) + pkgproc_dnf_args(args)
    
    if (dnf_action is None) and (args.packages is not []):
        dnf_action = "install"

    if (dnf_action is "install") and (args.packages is []):
        sys.exit("Invalid argument sequence!")
        
    dnf_install_args.append(dnf_action)
    return dnf_install_args
