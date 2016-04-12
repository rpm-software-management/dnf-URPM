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

def add_opmodes_urpmi_args(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--auto-select", help="Select all packages that can be upgraded, according to already installed packages and packages listed in various registered media.", action="store_true", default=None)
    group.add_argument("--auto-update", help="Like --auto-select, but also updates all relevant media before selection of upgradeable packages is made. This avoids a previous call to \"urpmi.update\".", action="store_true", default=None)
    parser.add_argument("--auto-orphans", help="Remove all orphans without asking (see also \"urpme --auto-orphans\")", action="store_true", default=None)
    return parser


def add_pkgselect_urpmi_args(parser):
    parser.add_argument("--auto", help="Install all required dependencies without asking.", action="store_true", default=None)
    parser.add_argument("-y", "--fuzzy", help="(Unimplemented) Disable fast search on exact package name; that means that urpmi will propose all packages matching part of the name, even if one of them matches exactly the specified name.", action="store_true", default=None)
    parser.add_argument("--buildrequires", help="Select all the \"BuildRequires\" of the wanted source packages. (You can also install the build dependencies read directly from an rpm spec file.)", action="store_true", default=None)
    parser.add_argument("--install-src", help="(Unimplemented) Install only the source package (that is, no binary packages will be installed). You don't need to be root to use this option (if you have write access to your rpm build top directory).", action="store_true", default=None)
    parser.add_argument("--no-recommends", help="(Unimplemented) With this option, urpmi will not install \"recommended\" packages. By default, urpmi will install (newly) recommended packages.", action="store_true", default=None)
    parser.add_argument("--allow-suggests", help="(Unimplemented) With this option, urpmi will install \"suggested\" packages.", action="store_true", default=None)
    parser.add_argument("-a", help="(Unimplemented) If multiple packages match the given substring, install them all.", action="store_true", default=None)
    parser.add_argument("--skip", help="(Unimplemented) You can specify a list of packages which installation should be skipped. You can also include patterns between //.", default=None)
    return parser


def add_pkgproc_urpmi_args(parser):
    parser.add_argument("--clean", help="Remove all packages from the cache.", action="store_true", default=None)
    parser.add_argument("--downgrade", help="Force installing older packages to replace installed packages.", action="store_true", default=None)
    parser.add_argument("--replacepkgs", help="Force installing the packages even though they are already installed.", action="store_true", default=None)
    return parser
