# -*- coding: utf-8 -*-

# Copyright (C) 2012  Matias Bordese
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages


version = __import__('unrar').VERSION


setup(
    name='unrar',
    version=version,
    description="Wrapper for UnRAR library, ctypes-based.",
    keywords='unrar ctypes',
    author='Matias Bordese',
    author_email='mbordese@gmail.com',
    url='http://github.com/matiasb/python-unrar',
    license='GPL-3',
    packages=find_packages(),
)
