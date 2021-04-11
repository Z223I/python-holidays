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
        self.holidays = holidays.MarketIdentifierCode(state="XNYS", observed=False, shortDay=False, shortDaysOnly=False)


    def test_presidents_funerals(self):
        self.assertIn(date(2018, 12, 5), self.holidays) # George H. W. Bush









    def test_new_years(self):
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertNotIn(date(2010, 12, 31), self.holidays) # The XNYS is open.
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
            "Martin Luther King Jr. Day", holidays.MarketIdentifierCode(years=[1985], state="XNYS", observed=False, shortDay=False, shortDaysOnly=False).values()
        )
        self.assertIn(
            "Martin Luther King Jr. Day", holidays.MarketIdentifierCode(years=[1986], state="XNYS", observed=False, shortDay=False, shortDaysOnly=False).values()
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
            self.assertIn(dt, self.holidays)

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


    # Independence Day Eve
    # Partial day on July 3 if July 4 lands on Tues. - Fri.  This is verified true for 2021.
    # Per https://www.nyse.com/markets/hours-calendars July 4, 2022 lands on a Monday 
    # and the market has a full session the previous Friday.

    def test_independence_eve(self):
        self.holidays.shortDay = True
        self.assertNotIn(date(2020, 7, 3), self.holidays) # Test case for July 4 on a Saturday.  Should be a full trading day.
        self.holidays.observed = True
        self.assertIn(date(2010, 7, 5), self.holidays)
        self.holidays.observed = False
        self.holidays.shortDay = True
        self.assertNotIn(date(2020, 7, 3), self.holidays)

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
        self.holidays.shortDay = True
        self.assertNotIn(date(2020, 7, 3), self.holidays)

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


    # 2019 Out of a possible 365 days, 104 days are weekend days (Saturday and Sunday) when the stock exchanges 
    # are closed. All nine holidays which close the exchanges fall on weekdays. There are three shortened trading 
    # sessions: on Wednesday, July 3 (the day before Independence Day), on Friday, November 29 (the day after 
    # Thanksgiving Day), and on Tuesday, December 24 (Christmas Eve).
    # https://en.wikipedia.org/wiki/Trading_day#2019

    # 2020 There are two shortened trading sessions: on Friday, November 27 (the day after Thanksgiving Day), 
    # and on Thursday, December 24 (Christmas Eve).
    # https://en.wikipedia.org/wiki/Trading_day#2020
    def test_day_after_thanksgiving(self):
        self.holidays.shortDay = True
        for dt in [
            date(1997, 11, 28),
            date(1999, 11, 26),
            date(2000, 11, 24),
            date(2012, 11, 23),
            date(2013, 11, 29),
            date(2014, 11, 28),
            date(2015, 11, 27),
            date(2016, 11, 25),
            date(2020, 11, 27),
        ]:
            self.assertIn(dt, self.holidays)


    def test_christmas_eve(self):
        self.holidays.shortDay = True
        self.assertIn(date(2019, 12, 24), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2019
        self.assertIn(date(2020, 12, 24), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2020
        self.assertNotIn(date(2021, 12, 24), self.holidays) # https://www.nyse.com/markets/hours-calendars
        self.assertNotIn(date(2022, 12, 24), self.holidays) # https://www.nyse.com/markets/hours-calendars
        self.assertNotIn(date(2023, 12, 24), self.holidays) # https://www.nyse.com/markets/hours-calendars

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


    # 2019 Out of a possible 365 days, 104 days are weekend days (Saturday and Sunday) when the stock exchanges 
    # are closed. All nine holidays which close the exchanges fall on weekdays. There are three shortened trading 
    # sessions: on Wednesday, July 3 (the day before Independence Day), on Friday, November 29 (the day after 
    # Thanksgiving Day), and on Tuesday, December 24 (Christmas Eve).
    # https://en.wikipedia.org/wiki/Trading_day#2019

    # 2020 There are two shortened trading sessions: on Friday, November 27 (the day after Thanksgiving Day), 
    # and on Thursday, December 24 (Christmas Eve).
    # https://en.wikipedia.org/wiki/Trading_day#2020
    def test_short_days_only(self):
        self.holidays.shortDaysOnly = True  # TODO: How do they get an assignment to work?
        self.holidays = holidays.MarketIdentifierCode(state="XNYS", observed=False, shortDay=False, shortDaysOnly=True)

        self.assertIn(date(2019,  7,  3), self.holidays)
        self.assertIn(date(2019, 11, 29), self.holidays)
        self.assertIn(date(2019, 12, 24), self.holidays)

        self.assertNotIn(date(2020,  7,  3), self.holidays)
        self.assertNotIn(date(2020, 7, 5), self.holidays)
        self.assertIn(date(2020, 11, 27), self.holidays)
        self.assertIn(date(2020, 12, 24), self.holidays)

        self.assertIn(date(2021, 11, 26), self.holidays)
        self.assertIn(date(2020, 12, 24), self.holidays)

        # New Year's Day
        self.holidays.observed = False
        for year in range(1990, 2020):
            dt = date(year, 1, 1)
            self.assertNotIn(dt, self.holidays)

        # MLK
        for dt in [
            date(1986, 1, 20),
            date(2020, 1, 20),
        ]:
            self.assertNotIn(dt, self.holidays)

        # Washington's Birthday'
        for dt in [
            date(1969, 2, 22),
            date(2020, 2, 17),
        ]:
            self.assertNotIn(dt, self.holidays)

        # Good Friday
        for dt in [
            date(1999, 4, 2),
            date(2018, 3, 30),
        ]:
            self.assertNotIn(dt, self.holidays)

        # Memorial Day
        for dt in [
            date(1971, 5, 31),
            date(2020, 5, 25),
        ]:
            self.assertNotIn(dt, self.holidays)

        # Independence Day
        for year in range(2010, 2014):
            dt = date(year, 7, 4)
            self.assertNotIn(dt, self.holidays)

        # Labor day
        for dt in [
            date(2014, 9, 1),
            date(2015, 9, 7),
            date(2016, 9, 5),
            date(2020, 9, 7),
        ]:
            self.assertNotIn(dt, self.holidays)

        # Thanksgiving Day
        for dt in [
            date(1997, 11, 27),
            date(1999, 11, 25),
            date(2000, 11, 23),
        ]:
            self.assertNotIn(dt, self.holidays)

        # Christmas
        self.assertIn(date(2019, 12, 24), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2019
        self.assertIn(date(2020, 12, 24), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2020
        self.assertNotIn(date(2021, 12, 24), self.holidays) # https://www.nyse.com/markets/hours-calendars
        self.assertNotIn(date(2022, 12, 24), self.holidays) # https://www.nyse.com/markets/hours-calendars
        self.assertNotIn(date(2023, 12, 24), self.holidays) # https://www.nyse.com/markets/hours-calendars

        self.assertNotIn(date(2023, 12, 25), self.holidays)


"""
Run from finnhub directory
export PYTHONPATH=$PYTHONPATH:/home/bwilson/DL/holidays/countries
export PYTHONPATH=$PYTHONPATH:/home/bwilson/DL/holidays
python3 -m pip install -e .
python -m unittest discover -s test
python -m unittest test/countries/test_market_identifier_code.py
python test/countries/test_market_identifier_code.py TestMIC
"""

"""
if __name__ == "__main__":

    unittest.main()
"""