# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date
from dateutil.relativedelta import relativedelta

import holidays


class TestMIC(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MarketIdentifierCode(state="XNYS", observed=False, shortDay=False)

    def test_new_years(self):
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        #self.assertIn(date(2010, 12, 31), self.holidays) # The XNYS is open.
        self.assertIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_martin_luther(self):
        for dt in [
            date(1986, 1, 20),
            date(1999, 1, 18),
            date(2000, 1, 17),
            date(2012, 1, 16),
            date(2013, 1, 21),
            date(2014, 1, 20),
            date(2015, 1, 19),
            date(2016, 1, 18),
            date(2020, 1, 20),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(
            "Martin Luther King Jr. Day", holidays.MarketIdentifierCode(years=[1985], state="XNYS", observed=False, shortDay=False).values()
        )
        self.assertIn(
            "Martin Luther King Jr. Day", holidays.MarketIdentifierCode(years=[1986], state="XNYS", observed=False, shortDay=False).values()
        )

    def test_washingtons_birthday(self):
        for dt in [
            date(1969, 2, 22),
            date(1970, 2, 22),
            date(1971, 2, 15),
            date(1997, 2, 17),
            date(1999, 2, 15),
            date(2000, 2, 21),
            date(2012, 2, 20),
            date(2013, 2, 18),
            date(2014, 2, 17),
            date(2015, 2, 16),
            date(2016, 2, 15),
            date(2020, 2, 17),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_good_friday(self):
        for dt in [
            #date(1900, 4, 13),
            #date(1901, 4, 5),
            #date(1902, 3, 28),
            date(1999, 4, 2),
            date(2000, 4, 21),
            date(2010, 4, 2),
            date(2018, 3, 30),
            date(2019, 4, 19),
            date(2020, 4, 10),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_memorial_day(self):
        for dt in [
            date(1969, 5, 30),
            date(1970, 5, 30),
            date(1971, 5, 31),
            date(1997, 5, 26),
            date(1999, 5, 31),
            date(2000, 5, 29),
            date(2012, 5, 28),
            date(2013, 5, 27),
            date(2014, 5, 26),
            date(2015, 5, 25),
            date(2016, 5, 30),
            date(2020, 5, 25),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_independence_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 4)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2010, 7, 5), self.holidays)
        self.assertNotIn(date(2020, 7, 3), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 7, 5), self.holidays)
        self.holidays.observed = False
        self.shortDay = True
        self.assertIn(date(2020, 7, 3), self.holidays)

    def test_labor_day(self):
        for dt in [
            date(1997, 9, 1),
            date(1999, 9, 6),
            date(2000, 9, 4),
            date(2012, 9, 3),
            date(2013, 9, 2),
            date(2014, 9, 1),
            date(2015, 9, 7),
            date(2016, 9, 5),
            date(2020, 9, 7),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_thanksgiving_day(self):
        for dt in [
            date(1997, 11, 27),
            date(1999, 11, 25),
            date(2000, 11, 23),
            date(2012, 11, 22),
            date(2013, 11, 28),
            date(2014, 11, 27),
            date(2015, 11, 26),
            date(2016, 11, 24),
            date(2020, 11, 26),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotIn(date(2016, 12, 26), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 24), self.holidays)
        self.assertIn(date(2016, 12, 26), self.holidays)


"""
Run from finnhub directory
export PYTHONPATH=$PYTHONPATH:/home/bwilson/DL/holidays/countries
export PYTHONPATH=$PYTHONPATH:/home/bwilson/DL/holidays
python3 -m pip install -e .
python -m unittest discover -s test
python test/countries/test_market_identifier_code.py TestMIC
"""

"""
if __name__ == "__main__":

    unittest.main()
"""