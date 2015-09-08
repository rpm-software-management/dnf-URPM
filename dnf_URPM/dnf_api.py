# This file is part of dnf-urpm
# Copyright (C) 2015 Neal Gompa
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import pathlib
import subprocess


def dnf_exists():
    """
    For now, this function checks for
    /usr/bin/dnf existing. If it doesn't
    exist, it'll return false. Otherwise,
    it returns true. Eventually this will
    change to also check for DNF API once
    it is used to power this application.

    @return boolean Success/failure of DNF's existence
    """
    return pathlib.Path("/usr/bin/dnf").exists()


def dnf_action(action):
    """
    This function will pass actions to DNF,
    provided it exists.

    FIXME: Eventually this will use DNF 
           Python API instead of the CLI.
    """

    if not dnf_exists():
        sys.exit("DNF not detected. Please install DNF!")

    command = ["/usr/bin/dnf"] + action
    subprocess.call(command)

