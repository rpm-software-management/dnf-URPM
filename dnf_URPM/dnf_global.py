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


def general_dnf_args(args):
    """Process general arguments and convert to DNF equivalents"""
    general_args = []
    if args.force is True:
        general_args.append("--assumeyes")
    if args.quiet is True:
        general_args.append("--quiet")
    if args.verbose is True:
        general_args.append("--verbose")

    return general_args


def mediaselect_dnf_args(args):
    mediaselect_args = []
    if args.media is not None:
        mediaselect_args = ["--disablerepo=*",("--enablerepo="+args.media)]
    if args.excludemedia is not None:
        mediaselect_args = [("--disablerepo="+args.excludemedia)]

    return mediaselect_args


def dbopts_dnf_args(args):
    dbopts_args = []
    if args.root is not None:
        dbopts_args = [("--installroot="+args.root)]
    if args.urpmi_root is not None:
        dbopts_args = [("--installroot="+args.urpmi_root), ("--config="+args.urpmi_root+"/etc/dnf.conf"), ("--setopt=reposdir="+args.urpmi_root+"/etc/distro.repos.d")]

    return dbopts_args


def process(args):
    return general_dnf_args(args) + mediaselect_dnf_args(args) + dbopts_dnf_args(args)

def get_packages(args):
    if args.packages is not None:
        return args.packages
    else:
        return []
