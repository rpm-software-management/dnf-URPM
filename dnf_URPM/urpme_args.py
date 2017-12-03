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

def add_opmodes_urpme_args(parser):
    parser.add_argument("--auto-orphans", help="Removes orphans.", action="store_true", default=None)
    return parser


def add_pkgselect_urpme_args(parser):
    parser.add_argument("--auto", help="Removes packages non-interactively, without asking questions.", action="store_true", default=None)
    parser.add_argument("--test", help="(Unimplemented) Test deinstallation of packages but do not modify the system.", action="store_true", default=None)
    parser.add_argument("-a", help="If multiple packages match the given substring, deinstall them all.", action="store_true", default=None)
    return parser


def add_pkgproc_urpme_args(parser):
    #parser.add_argument("--force", help="(Unimplemented) Force invocation even if some packages do not exist.", action="store_true" default=None)
    parser.add_argument("--justdb", help="(Unimplemented) Update only the database, not the filesystem.", action="store_true", default=None)
    parser.add_argument("--noscripts", help="(Unimplemented) Don't execute the scriptlets. This is equivalent to rpm --noscripts.  This can be useful to remove packages where uninstall scriptlets fail for some reason.", action="store_true", default=None)
    return parser
