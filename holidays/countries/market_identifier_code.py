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

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO, TU, WE, TH, FR

from holidays.constants import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.constants import MON, TUE, WED, THU, FRI, SAT, SUN, WEEKEND
from holidays.holiday_base import HolidayBase

# @dr-prodigy to keep with ISO standardization, I suggest we use ISO 10383 (the standard which "specifies a universal 
# method of identifying exchanges, trading platforms and regulated or non-regulated markets as sources of prices and 
# related information in order to facilitate automated processing"). These codes are at https://www.iso20022.org/market-identifier-codes.


# https://www.nyse.com/markets/hours-calendars
# 2021, 2022 and 2023 ** Each market will close early at 1:00 p.m. (1:15 p.m. for eligible options) on 
# Friday, November 26, 2021, Friday, November 25, 2022, and Friday, November 24, 2023 (the day after Thanksgiving). 
# Crossing Session orders will be accepted beginning at 1:00 p.m. for continuous executions until 1:30 p.m. on these dates, 
# and NYSE American Equities, NYSE Arca Equities, NYSE Chicago, and NYSE National late trading sessions will close at 5:00 pm. 
# All times are Eastern Time.

# 2023 07 03 * Each market will close early at 1:00 p.m. (1:15 p.m. for eligible options) on Monday, July 3, 2023. 
# Crossing Session orders will be accepted beginning at 1:00 p.m. for continuous executions until 1:30 p.m. on these dates, 
# and NYSE American Equities, NYSE Arca Equities, NYSE Chicago, and NYSE National late trading sessions will close at 5:00 pm.
# All times are Eastern Time.
class MarketIdentifierCode(HolidayBase):

    # Treat markets as if they are states or provinces.
    STATES = [
        "XNYS",  # NYSE started March 8, 1817 per Google on April 9, 2021.
        "XNAS",
    ]

    def __init__(self, **kwargs):
        self.country = "MIC"
        self.shortDay = kwargs.pop("shortDay")
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        if self.state in ["XNYS", "XNAS"]:
            # https://www.nyse.com/markets/hours-calendars

            # 2020
            # Out of a possible 366 days, 104 days are weekend days (Saturday and Sunday) when the stock exchanges are closed. 
            # Eight of the nine holidays which close the exchanges fall on weekdays, with Independence Day being observed on 
            # Friday, July 3. 
            # 
            # 
            # 
            # 
            # There are two shortened trading sessions: on Friday, November 27 (the day after Thanksgiving Day), 
            # and on Thursday, December 24 (Christmas Eve).
            # https://en.wikipedia.org/wiki/Trading_day#2020

            # New Year's Day
            if year > 1870:
                name = "New Year's Day"
                self[date(year, JAN, 1)] = name
                if self.observed and date(year, JAN, 1).weekday() == SUN:
                    self[date(year, JAN, 1) + rd(days=+1)] = name + " (Observed)"

                
                # XNYS (US NYSE) Saturday January 1, 2022 the market stays fully open on Friday December 31, 2021.
                # If this is true for all years for which New Year's Day falls on a Saturday, comment this out.
                """
                elif self.observed and date(year, JAN, 1).weekday() == SAT:
                    # Add Dec 31st from the previous year without triggering
                    # the entire year to be added
                    expand = self.expand
                    self.expand = False
                    self[date(year, JAN, 1) + rd(days=-1)] = name + " (Observed)"
                    self.expand = expand
                # The next year's observed New Year's Day can be in this year
                # when it falls on a Friday (Jan 1st is a Saturday)
                if self.observed and date(year, DEC, 31).weekday() == FRI:
                    self[date(year, DEC, 31)] = name + " (Observed)"
                """

            # Martin Luther King Jr. Day
            if year >= 1986:
                name = "Martin Luther King Jr. Day"
                self[date(year, JAN, 1) + rd(weekday=MO(+3))] = name

            # Washington's Birthday
            name = "Washington's Birthday"
            if year > 1970:
                self[date(year, FEB, 1) + rd(weekday=MO(+3))] = name
            elif year >= 1879:
                self[date(year, FEB, 22)] = name

            # Good Friday
            self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

            # Memorial Day
            if year > 1970:
                self[date(year, MAY, 31) + rd(weekday=MO(-1))] = "Memorial Day"
            elif year >= 1888:
                self[date(year, MAY, 30)] = "Memorial Day"

            # Independence Day Eve
            # Partial day on July 3 if July 4 lands on Tues. - Fri.  This is verified true for 2021.
            # TODO: Test case for July 4 on a Saturday.
            # Per https://www.nyse.com/markets/hours-calendars July 4, 2022 lands on a Monday 
            # and the market has a full session the previous Friday.
            if year > 1870:
                name = "Independence Day Eve (Short Trading Day)"
                if ((self.shortDay and date(year, JUL, 3).weekday() == MON) or
                    (self.shortDay and date(year, JUL, 3).weekday() == TUE) or
                    (self.shortDay and date(year, JUL, 3).weekday() == WED) or
                    (self.shortDay and date(year, JUL, 3).weekday() == THU)):
                    self[date(year, JUL, 3)] = name

            # Independence Day
            if year > 1870:
                name = "Independence Day"
                self[date(year, JUL, 4)] = name
                if self.observed and date(year, JUL, 4).weekday() == SAT:
                    self[date(year, JUL, 4) + rd(days=-1)] = name + " (Observed)"
                elif self.observed and date(year, JUL, 4).weekday() == SUN:
                    self[date(year, JUL, 4) + rd(days=+1)] = name + " (Observed)"

            # Labor Day
            if year >= 1894:
                self[date(year, SEP, 1) + rd(weekday=MO)] = "Labor Day"

            # Thanksgiving
            if year > 1870:
                self[date(year, NOV, 1) + rd(weekday=TH(+4))] = "Thanksgiving"

            # Partial day on Friday
            # Day After Thanksgiving
            name = "Day After Thanksgiving (Short Trading Day)"
            if self.shortDay:
               dt = date(year, NOV, 1) + rd(weekday=TH(+4))
               self[dt + rd(days=+1)] = name


            # TODO:
            # 2020 There are two shortened trading sessions: on Friday, November 27 (the day after Thanksgiving Day), 
            # and on Thursday, December 24 (Christmas Eve).
            # https://en.wikipedia.org/wiki/Trading_day#2020




            

            # Christmas Day
            if year > 1870:
                name = "Christmas Day"
                self[date(year, DEC, 25)] = "Christmas Day"
                if self.observed and date(year, DEC, 25).weekday() == SAT:
                    self[date(year, DEC, 25) + rd(days=-1)] = name + " (Observed)"
                elif self.observed and date(year, DEC, 25).weekday() == SUN:
                    self[date(year, DEC, 25) + rd(days=+1)] = name + " (Observed)"

            """ Partial trading day?  Does not look like it.
            # New Year's Eve
            # For Tues. December 31, 2020, the XNYS and XNAS had full sessions.
            """

"""
class US(UnitedStates):
    pass


class USA(UnitedStates):
    pass
"""