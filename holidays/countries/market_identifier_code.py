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

        # TODO How to check if key exists before pop.
        self.shortDay = kwargs.pop("shortDay")
        self.shortDaysOnly = kwargs.pop("shortDaysOnly")
        if self.shortDaysOnly:
            self.shortDay = True

        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        if self.state in ["XNYS", "XNAS"]:
            if not self.shortDaysOnly:
                #
                # Dignitary funerals
                #

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

                if year == 2007:
                    self[date(2007, 1, 2)] = 'Gerald R. Ford'

                if year == 2018:
                    self[date(2018, 12, 5)] = 'George H. W. Bush'

                #
                # Other notable days
                #

                # NEW YORK -- The closing of the New York Stock Exchange after Tuesday's attack on the 
                # World Trade Center is the longest since August 1914, when the exchange was closed pending 
                # the outbreak of World War I.
                # 9/11 between September 10, 2001 and September 17, 2001
                if year == 2001:
                    self[date(2001, 9, 11)] = '911 attack'
                    self[date(2001, 9, 12)] = '911 attack'
                    self[date(2001, 9, 13)] = '911 attack'
                    self[date(2001, 9, 14)] = '911 attack'
                    self[date(2001, 9, 17)] = '911 attack'

                # Apolo 11 - President Nixon decided to give the entire country a day off on July 22, 1969 – closing the NYSE.
                if year == 1969:
                    self[date(1969, 7, 22)] = 'Apolo 11 landing'

                # Hurricane Sandy closed down the New York Stock Exchange for two whole days in the fall of 2012. 
                # October 29, 2012 and October 30, 2012.
                if year == 2012:
                    self[date(2012, 10, 29)] = 'Hurricane Sandy'
                    self[date(2012, 10, 30)] = 'Hurricane Sandy'

                # Paperwork Crisis: 1968
                # In the late 1960s, the volume of trading activity increased dramatically. With the drastic 
                # increase in volume, the NYSE had $4 billion in unprocessed transactions by 1968. To catch up, 
                # the exchange closed every Wednesday from June 12, 1968 to December 31, 1968.
                # https://www.dividend.com/dividend-education/7-events-that-closed-the-nyse/
                if year == 1968:
                    for weekNum in range(1, 30):
                        self[date(year, JUN, 6) + rd(weekday=WE(+weekNum))] = "Paperwork Crisis"



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
                    if ((date(year, JAN, 1).weekday() == MON) or
                        (date(year, JAN, 1).weekday() == TUE) or
                        (date(year, JAN, 1).weekday() == WED) or
                        (date(year, JAN, 1).weekday() == THU) or
                        (date(year, JAN, 1).weekday() == FRI)):
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
                    if ((date(year, FEB, 22).weekday() == MON) or
                        (date(year, FEB, 22).weekday() == TUE) or
                        (date(year, FEB, 22).weekday() == WED) or
                        (date(year, FEB, 22).weekday() == THU) or
                        (date(year, FEB, 22).weekday() == FRI)):
                            self[date(year, FEB, 22)] = name

                # Good Friday
                self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

                # Memorial Day
                if year > 1970:
                    self[date(year, MAY, 31) + rd(weekday=MO(-1))] = "Memorial Day"
                elif year >= 1888:
                    if ((date(year, MAY, 30).weekday() == MON) or
                        (date(year, MAY, 30).weekday() == TUE) or
                        (date(year, MAY, 30).weekday() == WED) or
                        (date(year, MAY, 30).weekday() == THU) or
                        (date(year, MAY, 30).weekday() == FRI)):
                        self[date(year, MAY, 30)] = "Memorial Day"

                # Independence Day
                if year > 1870:
                    name = "Independence Day"
                    if ((date(year, JUL, 4).weekday() == MON) or
                        (date(year, JUL, 4).weekday() == TUE) or
                        (date(year, JUL, 4).weekday() == WED) or
                        (date(year, JUL, 4).weekday() == THU) or
                        (date(year, JUL, 4).weekday() == FRI)):
                        self[date(year, JUL, 4)] = name
                    elif self.observed and date(year, JUL, 4).weekday() == SAT:
                        self[date(year, JUL, 4) + rd(days=-1)] = name + " (Observed)"
                    elif self.observed and date(year, JUL, 4).weekday() == SUN:
                        self[date(year, JUL, 4) + rd(days=+1)] = name + " (Observed)"

                # Labor Day
                if year >= 1894:
                    self[date(year, SEP, 1) + rd(weekday=MO)] = "Labor Day"

                # Thanksgiving
                if year > 1870:
                    self[date(year, NOV, 1) + rd(weekday=TH(+4))] = "Thanksgiving"

                # Christmas Day
                if year > 1870:
                    name = "Christmas Day"
                    if ((date(year, DEC, 25).weekday() == MON) or
                        (date(year, DEC, 25).weekday() == TUE) or
                        (date(year, DEC, 25).weekday() == WED) or
                        (date(year, DEC, 25).weekday() == THU) or
                        (date(year, DEC, 25).weekday() == FRI)):
                        self[date(year, DEC, 25)] = "Christmas Day"
                    elif self.observed and date(year, DEC, 25).weekday() == SAT:
                        self[date(year, DEC, 25) + rd(days=-1)] = name + " (Observed)"
                    elif self.observed and date(year, DEC, 25).weekday() == SUN:
                        self[date(year, DEC, 25) + rd(days=+1)] = name + " (Observed)"




            #
            # Allows do this section.
            #

            # Independence Day Eve
            # Partial day on July 3 if July 4 lands on Tues. - Fri.  This is verified true for 2021.
            # Per https://www.nyse.com/markets/hours-calendars July 4, 2022 lands on a Monday 
            # and the market has a full session the previous Friday.
            if year > 1870:
                name = "Independence Day Eve (Short Trading Day)"
                if ((self.shortDay and date(year, JUL, 3).weekday() == MON) or
                    (self.shortDay and date(year, JUL, 3).weekday() == TUE) or
                    (self.shortDay and date(year, JUL, 3).weekday() == WED) or
                    (self.shortDay and date(year, JUL, 3).weekday() == THU)):
                    self[date(year, JUL, 3)] = name

            # Partial day on Friday after Thanksgiving
            name = "Friday After Thanksgiving (Short Trading Day)"
            if self.shortDay:
                dt = date(year, NOV, 1) + rd(weekday=TH(+4))
                self[dt + rd(days=+1)] = name


            # 2020 There are two shortened trading sessions: on Friday, November 27 (the day after Thanksgiving Day), 
            # and on Thursday, December 24 (Christmas Eve).
            # https://en.wikipedia.org/wiki/Trading_day#2020

            # Christmas Eve
            if year > 1870:
                name = "Christmas Eve (Short Trading Day)"
                if ((self.shortDay and date(year, DEC, 24).weekday() == MON) or
                    (self.shortDay and date(year, DEC, 24).weekday() == TUE) or
                    (self.shortDay and date(year, DEC, 24).weekday() == WED) or
                    (self.shortDay and date(year, DEC, 24).weekday() == THU)):
                    self[date(year, DEC, 24)] = name


            """ Partial trading day?  Does not look like it.
            # New Year's Eve
            # For Tues. December 31, 2020, the XNYS and XNAS had full sessions.
            """
"""
class MIC(MarketIdentifierCode):
    pass
"""