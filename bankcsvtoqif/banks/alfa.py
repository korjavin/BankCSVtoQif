# -*- coding: utf-8 -*-


# BankCSVtoQif - Smart conversion of csv files from a bank to qif
# Copyright (C) 2015-2016  Nikolai Nowaczyk
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from bankcsvtoqif.banks import BankAccountConfig
from datetime import datetime


class VRBank(BankAccountConfig):
    """ Alfa """

    def __init__(self):
        BankAccountConfig.__init__(self)

        # self.encoding = 'windows-1251'
        self.delimiter = ';'
        self.quotechar = '"'
        self.dropped_lines = 1
        self.default_source_account = 'Assets:Current Assets:Checking Account'
        self.default_target_account = 'Imbalance-RUR'

    def get_date(self, line):
        (day, month, year) = map(int, line[3].split('.'))
        return datetime(2000+year, month, day)

    def get_target_account(self, line):
        s = line[5].split()
        return (s[1] + ' ' + s[2])

    def get_description(self, line):
        return line[5]

    def get_debit(self, line):
        val = self.get_amount(line[7])
        val1 = self.get_amount(line[6])
        return val if val >= 0 else val1

    def get_credit(self, line):
        val = self.get_amount(line[6])
        return val
