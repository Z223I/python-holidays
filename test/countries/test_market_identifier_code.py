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


    def test_dignitary_funerals(self):
		# Aug. 8, 1885 -- Funeral of former President Grant.
		# Feb. 2, 1901 -- Funeral of Queen Victoria of England.
		# Sept. 14, 1901 -- Death of President McKinley.
		# Sept. 19, 1901 -- Funeral of President McKinley.
		# May 7, 1910 -- Closed 11 a.m. for the death of King Edward VII of England.
		# May 20, 1910 -- Closed 10 a.m. - noon for funeral of King Edward VII.
		# April 14, 1913 -- Closed from 10 a.m. to noon for funeral of J.P. Morgan.
		# Aug. 3, 1923 -- Death of President Harding.
		# Aug. 10, 1923 -- Funeral of President Harding at Marion, Ohio.
		# Feb. 6, 1924 -- Closed 12:30 p.m. for funeral of former President Wilson.
		# Jan. 28, 1936 -- Closed from 10 - 11 a.m. for funeral of King George V of England. April 14, 1945 -- National day of mourning for the death of President Franklin D. Roosevelt.

        """
		# Oct. 23, 1964 -- Closed at 2 p.m. for funeral of former President Hoover.
        holiday = holidays.MarketIdentifierCode(state="XNYS", observed=False, shortDay=False, shortDaysOnly=True)
        self.assertIn(date(1964, 10, 23), holiday)

		# April 9, 1968 -- National day of mourning for the assassination of Martin Luther King Jr.
        self.assertIn(date(1968, 4, 9), self.holidays)
		# June 6, 1968 -- Closed from 11 - 11:02 a.m. in memory of Sen. Robert F. Kennedy.
		# March 31, 1969 -- Closed for funeral of former President Eisenhower.
        self.assertIn(date(1969, 3, 31), self.holidays)
		# Dec. 28, 1972 -- Closed for funeral of former President Truman.
        self.assertIn(date(1972, 12, 28), self.holidays)
		# Jan. 25, 1973 -- Closed for funeral of former President Johnson.
        self.assertIn(date(1973, 1, 25), self.holidays)
		# April 27, 1994 -- Closed for funeral of former President Nixon.
        self.assertIn(date(1994, 4, 27), self.holidays)
        # https://www.orlandosentinel.com/news/os-xpm-2001-09-17-0109170093-story.html
        """

        self.assertIn(date(2007,  1, 2), self.holidays) # Gerald R. Ford
        self.assertIn(date(2018, 12, 5), self.holidays) # George H. W. Bush

    def test_other_notable_days(self):
        # NEW YORK -- The closing of the New York Stock Exchange after Tuesday's attack on the
        # World Trade Center is the longest since August 1914, when the exchange was closed pending
        # the outbreak of World War I.
        # 9/11 between September 10, 2001 and September 17, 2001
        self.assertIn(date(2001, 9, 11), self.holidays)
        self.assertIn(date(2001, 9, 12), self.holidays)
        self.assertIn(date(2001, 9, 13), self.holidays)
        self.assertIn(date(2001, 9, 14), self.holidays)
        self.assertIn(date(2001, 9, 17), self.holidays)

		# Following is a list of closings of the exchange:
		# April 29-May 1, 1889 -- Centennial celebration of President Washington's inauguration.
		# Sept. 29-30, 1899 -- Admiral Dewey celebration.
		# Aug. 9, 1902 -- Coronation of King Edward VII of England.
		# April 22, 1903 -- Opening of new NYSE building.
		# July 31-Nov. 28, 1914 -- Closed pending outbreak of World War I. Reopened for trading in bonds with price restrictions
		# Nov. 28, 1914; for trading in a limited number of stocks under price restrictions
		# Dec. 12, 1914; and for trading in all stocks, under price restrictions,
		# Dec. 15, 1914. All restrictions were removed
		# April 1, 1915.
		# Jan. 28, 1918 -- Heatless day.
		# Feb. 4, 1918 -- Heatless day.
		# Feb. 11, 1918 -- Heatless day.
		# June 13, 1927 -- Parade for Charles Lindbergh.
		# Feb. 20, 1934 -- Opened at 11 a.m. after a severe snowstorm.
		# Aug. 15-16, 1945 -- V-J Day. End of World War II.
		# May 25, 1946 -- Railroad strike. , Nov. 22, 1963 -- Closed at 2:07 p.m. after the assassination of President Kennedy. Nov. 25, 1963 -- Funeral of President Kennedy.
		# July 14, 1977 -- Closed because of blackout in New York.
		# Sept. 27, 1985 -- Closed because of Hurricane Gloria.
		# Oct. 27, 1997 -- "Circuit breakers" triggered for first time when the Dow Jones Industrial average dropped 350 points, closing the market at 2:35 p.m. for a half hour. Trading reopened at 3:05 p.m. and the Dow declined an additional 200 points, touching off another mandated trading halt at 3:30 p.m., ending trading for the day.
        # https://www.orlandosentinel.com/news/os-xpm-2001-09-17-0109170093-story.html

        # But these kind of closings are rare and far between. Besides national days of mourning,
        # the stock exchange has shut down for terrorist attacks, the Apollo II moon landing, and of
        # course bad weather, such as blizzards and hurricanes, according to Mother Jones.
        # Hurricane Sandy closed down the New York Stock Exchange for two whole days in the fall of 2012.

        # Apolo 11 - President Nixon decided to give the entire country a day off on July 22, 1969 – closing the NYSE.
        self.assertIn(date(1969,  7, 22), self.holidays)

        # Hurricane Sandy closed down the New York Stock Exchange for two whole days in the fall of 2012.
        # October 29, 2012 and October 30, 2012.
        self.assertIn(date(2012, 10, 29), self.holidays)
        self.assertIn(date(2012, 10, 30), self.holidays)

        # Paperwork Crisis: 1968
        # In the late 1960s, the volume of trading activity increased dramatically. With the drastic
        # increase in volume, the NYSE had $4 billion in unprocessed transactions by 1968. To catch up,
        # the exchange closed every Wednesday from June 12, 1968 to December 31, 1968.
        # https://www.dividend.com/dividend-education/7-events-that-closed-the-nyse/
        self.assertIn(date(1968,  6, 12), self.holidays)
        self.assertIn(date(1968,  6, 19), self.holidays)
        self.assertIn(date(1968,  6, 26), self.holidays)
        self.assertIn(date(1968,  7,  3), self.holidays)
        self.assertIn(date(1968,  7, 10), self.holidays)
        self.assertIn(date(1968,  7, 17), self.holidays)
        self.assertIn(date(1968,  7, 24), self.holidays)
        self.assertIn(date(1968,  7, 31), self.holidays)
        self.assertIn(date(1968,  8,  7), self.holidays)
        self.assertIn(date(1968,  8, 14), self.holidays)
        self.assertIn(date(1968,  8, 21), self.holidays)
        self.assertIn(date(1968,  8, 28), self.holidays)
        self.assertIn(date(1968,  9,  4), self.holidays)
        self.assertIn(date(1968,  9, 11), self.holidays)
        self.assertIn(date(1968,  9, 18), self.holidays)
        self.assertIn(date(1968,  9, 25), self.holidays)
        self.assertIn(date(1968, 10,  2), self.holidays)
        self.assertIn(date(1968, 10,  9), self.holidays)
        self.assertIn(date(1968, 10, 16), self.holidays)
        self.assertIn(date(1968, 10, 23), self.holidays)
        self.assertIn(date(1968, 10, 30), self.holidays)
        self.assertIn(date(1968, 11,  6), self.holidays)
        self.assertIn(date(1968, 11, 13), self.holidays)
        self.assertIn(date(1968, 11, 20), self.holidays)
        self.assertIn(date(1968, 11, 27), self.holidays)
        self.assertIn(date(1968, 12,  4), self.holidays)
        self.assertIn(date(1968, 12, 11), self.holidays)
        self.assertIn(date(1968, 12, 18), self.holidays)
        self.assertIn(date(1968, 12, 25), self.holidays)

    def test_new_years(self):
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2012, 1, 1), self.holidays)   # Sundays should not be in holidays
        self.assertIn(date(2012, 1, 2), self.holidays)      # 1/1 observed on Monday.

        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertNotIn(date(2010, 12, 31), self.holidays) # The XNYS is open.
        self.assertIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            if year != 2007:
                # Gerald R. Ford funeral 1/2/2007
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
        self.assertNotIn(date(2020, 7, 3), self.holidays) # Test case for July 4 on a Saturday 2020.  Should be holiday.
        self.holidays.observed = True
        self.assertIn(date(2020, 7, 3), self.holidays) # Test case for July 4 on a Saturday 2020.  Should be observed holiday.
        self.assertIn(date(2010, 7, 5), self.holidays)
        self.holidays.observed = False
        self.holidays.shortDay = True
        self.assertNotIn(date(2020, 7, 3), self.holidays)

    def test_independence_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 4)
            self.assertIn(dt, self.holidays)
            if year != 1968:
                # The Paperwork Crisis happened in 1968.
                self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2010, 7, 5), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 7, 5), self.holidays)
        self.assertIn(date(2020, 7, 3), self.holidays)
        self.holidays.observed = False
        self.holidays.shortDay = True

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



        self.assertNotIn(date(2020, 7, 4), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2020

        self.assertNotIn(date(2021, 7, 3), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2021
        self.assertNotIn(date(2021, 7, 4), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2021
        self.assertNotIn(date(2021, 7, 5), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2021

        self.assertIn(date(2019,  7,  3), self.holidays)
        self.assertNotIn(date(2019, 7, 4), self.holidays)    # https://en.wikipedia.org/wiki/Trading_day#2019
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
        for year in range(1990, 2022):
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
XXXexport PYTHONPATH=$PYTHONPATH:/home/bwilson/DL/holidays/countries
XXXexport PYTHONPATH=$PYTHONPATH:/home/bwilson/DL/holidays
python3 -m pip3 install -e .
python -m unittest discover -s test
python -m unittest test/countries/test_market_identifier_code.py
python test/countries/test_market_identifier_code.py TestMIC
python test/countries/test_market_identifier_code.py TestMIC.test_independence_day
"""

"""
if __name__ == "__main__":

    unittest.main()
"""