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

import argparse

def add_general_urpm_args(parser):
    parser.add_argument("--force", help="Assume yes on all questions.", action="store_true", default=None)
    parser.add_argument("-q", "--quiet", help="Quiet mode: when calling rpm, no upgrade status is printed.", action="store_true", default=None)
    parser.add_argument("-v", "--verbose", help="Proposes a verbose mode with various messages.", action="store_true", default=None)
    return parser


def add_mediaselect_urpm_args(parser):
    parser.add_argument("--media", help="Select specific media to be used, instead of defaulting to all available media (or all update media if --update is used). No rpm will be fetched from other media.", default=None)
    parser.add_argument("--excludemedia", help="Do not use the specified media.", default=None)
    parser.add_argument("--searchmedia", help="(Unimplemented) Use only the specified media to search for packages that are specified on the command-line, or which are found when using --auto-select. Dependencies of those packages can still be found in other media.", default=None)
    parser.add_argument("--sortmedia", help="(Unimplemented) Sort the specified media. Substrings may be used to simplify grouping. This way, \"media1\" will be taken into account first, then \"media2\" and so on. Media which aren't listed are taken into account after the others.", default=None)
    return parser


def add_dbopts_urpm_args(parser):
    parser.add_argument("--root", help="Use the file system tree rooted for rpm install. All operations and scripts will run after chroot(2). The rpm database that lies in the rooted tree will be used, but the urpmi configuration comes from the normal system", default=None)
    parser.add_argument("--urpmi-root", help="Use the file system tree rooted for urpmi database and rpm install. Contrary to --root, the urpmi configuration comes from the rooted tree.", default=None)
    return parser


def add_package_list_args(parser):
    parser.add_argument("packages", nargs="*")
    return parser
