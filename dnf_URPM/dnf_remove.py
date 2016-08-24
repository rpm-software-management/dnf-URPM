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
dnf_action = "remove"

def opmodes_dnf_args(args):
    opmodes_args = []
    if args.auto_orphans is not True:
        opmodes_args.append("--setopt=clean_requirements_on_remove=False")
    else:
        opmodes_args.append("--setopt=clean_requirements_on_remove=True")

    return opmodes_args

def pkgselect_dnf_args(args):
    pkgselect_args = []
    if args.auto is True:
        pkgselect_args.append("-y")

    return pkgselect_args


def pkgproc_dnf_args(args):
    pkgproc_args = []

    return pkgproc_args


def process(args):
    dnf_install_args = opmodes_dnf_args(args) + pkgselect_dnf_args(args) + pkgproc_dnf_args(args)    
    dnf_install_args.append(dnf_action)

    return dnf_install_args
