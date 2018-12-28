===============================================
 datetime --- Date and Time Value Manipulation
===============================================

.. module:: datetime
    :synopsis: Date and time value manipulation.

:Purpose: The datetime module includes functions and classes for doing
          date and time parsing, formatting, and arithmetic.

``datetime`` contains functions and classes for working with dates
and times, separately and together.

Times
=====

Time values are represented with the ``time`` class. A
``time`` instance has attributes for :attr:`hour`,
:attr:`minute`, :attr:`second`, and :attr:`microsecond` and can also
include time zone information.

.. literalinclude:: datetime_time.py
    :caption:
    :start-after: #end_pymotw_header

The arguments to initialize a ``time`` instance are optional, but
the default of ``0`` is unlikely to be correct.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_time.py
	
	01:02:03
	hour       : 1
	minute     : 2
	second     : 3
	microsecond: 0
	tzinfo     : None

.. {{{end}}}

A ``time`` instance only holds values of time, and not a date
associated with the time.

.. literalinclude:: datetime_time_minmax.py
    :caption:
    :start-after: #end_pymotw_header

The :attr:`min` and :attr:`max` class attributes reflect the valid
range of times in a single day.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time_minmax.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_time_minmax.py
	
	Earliest  : 00:00:00
	Latest    : 23:59:59.999999
	Resolution: 0:00:00.000001

.. {{{end}}}

The resolution for ``time`` is limited to whole microseconds.

.. literalinclude:: datetime_time_resolution.py
    :caption:
    :start-after: #end_pymotw_header

Floating point values for microseconds cause a ``TypeError``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time_resolution.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_time_resolution.py
	
	1.0 : 00:00:00.000001
	0.0 : 00:00:00
	ERROR: integer argument expected, got float
	ERROR: integer argument expected, got float

.. {{{end}}}


Dates
=====

Calendar date values are represented with the ``date``
class. Instances have attributes for :attr:`year`, :attr:`month`, and
:attr:`day`. It is easy to create a date representing the current date
using the ``today()`` class method.

.. literalinclude:: datetime_date.py
    :caption:
    :start-after: #end_pymotw_header

This example prints the current date in several formats:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date.py', break_lines_at=69))
.. }}}

.. code-block:: none

	$ python3 datetime_date.py
	
	2018-12-09
	ctime  : Sun Dec  9 00:00:00 2018
	tuple  : tm_year  = 2018
	         tm_mon   = 12
	         tm_mday  = 9
	         tm_hour  = 0
	         tm_min   = 0
	         tm_sec   = 0
	         tm_wday  = 6
	         tm_yday  = 343
	         tm_isdst = -1
	ordinal: 737037
	Year   : 2018
	Mon    : 12
	Day    : 9

.. {{{end}}}

There are also class methods for creating instances from POSIX
timestamps or integers representing date values from the Gregorian
calendar, where January 1 of the year 1 is ``1`` and each subsequent
day increments the value by 1.

.. literalinclude:: datetime_date_fromordinal.py
    :caption:
    :start-after: #end_pymotw_header

This example illustrates the different value types used by
``fromordinal()`` and ``fromtimestamp()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_fromordinal.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_date_fromordinal.py
	
	o               : 733114
	fromordinal(o)  : 2008-03-13
	t               : 1544370390.0430489
	fromtimestamp(t): 2018-12-09

.. {{{end}}}

As with ``time``, the range of date values supported can be
determined using the :attr:`min` and :attr:`max` attributes.

.. literalinclude:: datetime_date_minmax.py
    :caption:
    :start-after: #end_pymotw_header

The resolution for dates is whole days.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_minmax.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_date_minmax.py
	
	Earliest  : 0001-01-01
	Latest    : 9999-12-31
	Resolution: 1 day, 0:00:00

.. {{{end}}}

Another way to create new ``date`` instances uses the
``replace()`` method of an existing ``date``.

.. literalinclude:: datetime_date_replace.py
    :caption:
    :start-after: #end_pymotw_header

This example changes the year, leaving the day and month unmodified.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_replace.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_date_replace.py
	
	d1: Sat Mar 29 00:00:00 2008
	d2: Sun Mar 29 00:00:00 2009

.. {{{end}}}

timedeltas
==========

Future and past dates can be calculated using basic arithmetic on two
``datetime`` objects, or by combining a ``datetime`` with a
``timedelta``.  Subtracting dates produces a ``timedelta``,
and a ``timedelta`` can be added or subtracted from a date to
produce another date. The internal values for a ``timedelta`` are
stored in days, seconds, and microseconds.

.. literalinclude:: datetime_timedelta.py
    :caption:
    :start-after: #end_pymotw_header

Intermediate level values passed to the constructor are converted into
days, seconds, and microseconds.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_timedelta.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_timedelta.py
	
	microseconds: 0:00:00.000001
	milliseconds: 0:00:00.001000
	seconds     : 0:00:01
	minutes     : 0:01:00
	hours       : 1:00:00
	days        : 1 day, 0:00:00
	weeks       : 7 days, 0:00:00

.. {{{end}}}

The full duration of a ``timedelta`` can be retrieved as a number
of seconds using ``total_seconds()``.

.. literalinclude:: datetime_timedelta_total_seconds.py
   :caption:
   :start-after: #end_pymotw_header

The return value is a floating point number, to accommodate sub-second
durations.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_timedelta_total_seconds.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_timedelta_total_seconds.py
	
	0:00:00.000001  =    1e-06 seconds
	0:00:00.001000  =    0.001 seconds
	0:00:01         =      1.0 seconds
	0:01:00         =     60.0 seconds
	1:00:00         =   3600.0 seconds
	1 day, 0:00:00  =  86400.0 seconds
	7 days, 0:00:00 = 604800.0 seconds

.. {{{end}}}

Date Arithmetic
===============

Date math uses the standard arithmetic operators.

.. literalinclude:: datetime_date_math.py
    :caption:
    :start-after: #end_pymotw_header

This example with date objects illustrates using ``timedelta``
objects to compute new dates, and subtracting date instances to
produce timedeltas (including a negative delta value).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_math.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_date_math.py
	
	Today    : 2018-12-09
	One day  : 1 day, 0:00:00
	Yesterday: 2018-12-08
	Tomorrow : 2018-12-10
	
	tomorrow - yesterday: 2 days, 0:00:00
	yesterday - tomorrow: -2 days, 0:00:00

.. {{{end}}}

A ``timedelta`` object also supports arithmetic with integers,
floats, and other ``timedelta`` instances.

.. literalinclude:: datetime_timedelta_math.py
   :caption:
   :start-after: #end_pymotw_header

In this example, several multiples of a single day are computed, with
the resulting ``timedelta`` holding the appropriate number of
days or hours. The final example demonstrates how to compute values by
combining two ``timedelta`` objects. In this case, the result is
a floating point number.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_timedelta_math.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_timedelta_math.py
	
	1 day    : 1 day, 0:00:00
	5 days   : 5 days, 0:00:00
	1.5 days : 1 day, 12:00:00
	1/4 day  : 6:00:00
	meetings per day : 7.0

.. {{{end}}}

Comparing Values
================

Both date and time values can be compared using the standard
comparison operators to determine which is earlier or later.

.. literalinclude:: datetime_comparing.py
    :caption:
    :start-after: #end_pymotw_header

All comparison operators are supported.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_comparing.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_comparing.py
	
	Times:
	  t1: 12:55:00
	  t2: 13:05:00
	  t1 < t2: True
	
	Dates:
	  d1: 2018-12-09
	  d2: 2018-12-10
	  d1 > d2: False

.. {{{end}}}

Combining Dates and Times
=========================

Use the ``datetime`` class to hold values consisting of both date
and time components. As with ``date``, there are several
convenient class methods to make creating ``datetime`` instances
from other common values.

.. literalinclude:: datetime_datetime.py
    :caption:
    :start-after: #end_pymotw_header

As might be expected, the ``datetime`` instance has all of the
attributes of both a ``date`` and a ``time`` object.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_datetime.py
	
	Now    : 2018-12-09 10:46:30.494767
	Today  : 2018-12-09 10:46:30.494806
	UTC Now: 2018-12-09 15:46:30.494812
	
	year           : 2018
	month          : 12
	day            : 9
	hour           : 10
	minute         : 46
	second         : 30
	microsecond    : 495051

.. {{{end}}}

Just as with ``date``, ``datetime`` provides convenient
class methods for creating new instances. It also includes
``fromordinal()`` and ``fromtimestamp()``.

.. literalinclude:: datetime_datetime_combine.py
    :caption:
    :start-after: #end_pymotw_header

``combine()`` creates ``datetime`` instances from one
``date`` and one ``time`` instance.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime_combine.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_datetime_combine.py
	
	t : 01:02:03
	d : 2018-12-09
	dt: 2018-12-09 01:02:03

.. {{{end}}}

Formatting and Parsing
======================

The default string representation of a datetime object uses the
ISO-8601 format (``YYYY-MM-DDTHH:MM:SS.mmmmmm``). Alternate formats
can be generated using ``strftime()``.

.. literalinclude:: datetime_datetime_strptime.py
    :caption:
    :start-after: #end_pymotw_header

Use ``datetime.strptime()`` to convert formatted strings to
``datetime`` instances.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime_strptime.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_datetime_strptime.py
	
	ISO     : 2018-12-09 10:46:30.598115
	strftime: Sun Dec 09 10:46:30 2018
	strptime: Sun Dec 09 10:46:30 2018

.. {{{end}}}

The same formatting codes can be used with Python's `string formatting
mini-language`_ by placing them after the ``:`` in the field
specification of the format string.

.. literalinclude:: datetime_format.py
   :caption:
   :start-after: #end_pymotw_header

Each datetime format code must still be prefixed with ``%``, and
subsequent colons are treated as literal characters to include in the
output.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_format.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_format.py
	
	ISO     : 2018-12-09 10:46:30.659964
	format(): Sun Dec 09 10:46:30 2018

.. {{{end}}}

.. _string formatting mini-language: https://docs.python.org/3.5/library/string.html#formatspec


The following table demonstrates all of the formatting codes for 5:00
PM January 13, 2016 in the US/Eastern time zone.

.. {{{cog
.. import datetime
.. import pytz
.. tz = pytz.timezone('US/Eastern')
.. d = tz.localize(datetime.datetime(2016, 1, 13, 17, 0, 0))
.. symbols = [
..   ('%a', 'Abbreviated weekday name'),
..   ('%A', 'Full weekday name'),
..   ('%w', 'Weekday number -- 0 (Sunday) through 6 (Saturday)'),
..   ('%d', 'Day of the month (zero padded)'),
..   ('%b', 'Abbreviated month name'),
..   ('%B', 'Full month name'),
..   ('%m', 'Month of the year'),
..   ('%y', 'Year without century'),
..   ('%Y', 'Year with century'),
..   ('%H', 'Hour from 24-hour clock'),
..   ('%I', 'Hour from 12-hour clock'),
..   ('%p', 'AM/PM'),
..   ('%M', 'Minutes'),
..   ('%S', 'Seconds'),
..   ('%f', 'Microseconds'),
..   ('%z', 'UTC offset for time zone-aware objects'),
..   ('%Z', 'Time Zone name'),
..   ('%j', 'Day of the year'),
..   ('%W', 'Week of the year'),
..   ('%c', 'Date and time representation for the current locale'),
..   ('%x', 'Date representation for the current locale'),
..   ('%X', 'Time representation for the current locale'),
..   ('%%', 'A literal ``%`` character'),
.. ]
.. cog.out('\n')
.. cog.out('.. csv-table:: strptime/strftime format codes\n')
.. cog.out('   :widths: 10, 50, 40\n')
.. cog.out('   :header: "Symbol", "Meaning", "Example"\n')
.. cog.out('\n')
.. for sym, mean in symbols:
..     cog.out('   ``%s``, %s, ``%r``\n' % (sym, mean, d.strftime(sym)))
.. cog.out('\n')
.. }}}

.. csv-table:: strptime/strftime format codes
   :widths: 10, 50, 40
   :header: "Symbol", "Meaning", "Example"

   ``%a``, Abbreviated weekday name, ``'Wed'``
   ``%A``, Full weekday name, ``'Wednesday'``
   ``%w``, Weekday number -- 0 (Sunday) through 6 (Saturday), ``'3'``
   ``%d``, Day of the month (zero padded), ``'13'``
   ``%b``, Abbreviated month name, ``'Jan'``
   ``%B``, Full month name, ``'January'``
   ``%m``, Month of the year, ``'01'``
   ``%y``, Year without century, ``'16'``
   ``%Y``, Year with century, ``'2016'``
   ``%H``, Hour from 24-hour clock, ``'17'``
   ``%I``, Hour from 12-hour clock, ``'05'``
   ``%p``, AM/PM, ``'PM'``
   ``%M``, Minutes, ``'00'``
   ``%S``, Seconds, ``'00'``
   ``%f``, Microseconds, ``'000000'``
   ``%z``, UTC offset for time zone-aware objects, ``'-0500'``
   ``%Z``, Time Zone name, ``'EST'``
   ``%j``, Day of the year, ``'013'``
   ``%W``, Week of the year, ``'02'``
   ``%c``, Date and time representation for the current locale, ``'Wed Jan 13 17:00:00 2016'``
   ``%x``, Date representation for the current locale, ``'01/13/16'``
   ``%X``, Time representation for the current locale, ``'17:00:00'``
   ``%%``, A literal ``%`` character, ``'%'``

.. {{{end}}}

Time Zones
==========

Within ``datetime``, time zones are represented by subclasses of
``tzinfo``. Since ``tzinfo`` is an abstract base class,
applications need to define a subclass and provide appropriate
implementations for a few methods to make it useful.

``datetime`` does include a somewhat naive implementation in the
class ``timezone`` that uses a fixed offset from UTC, and does
not support different offset values on different days of the year,
such as where daylight savings time applies, or where the offset from
UTC has changed over time.

.. literalinclude:: datetime_timezone.py
   :caption:
   :start-after: #end_pymotw_header

To convert a datetime value from one time zone to another, use
``astimezone()``. In the example above, two separate time zones 6
hours on either side of UTC are shown, and the ``utc`` instance from
``datetime.timezone`` is also used for reference. The final output
line shows the value in the system timezone, acquired by calling
``astimezone()`` with no argument.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_timezone.py'))
.. }}}

.. code-block:: none

	$ python3 datetime_timezone.py
	
	UTC-06:00 : 2018-12-09 09:46:30.709455-06:00
	UTC : 2018-12-09 15:46:30.709455+00:00
	UTC+06:00 : 2018-12-09 21:46:30.709455+06:00
	EST       : 2018-12-09 10:46:30.709455-05:00

.. {{{end}}}


.. note::

   The third party module pytz_ is a better implementation for time
   zones. It supports named time zones, and the offset database is
   kept up to date as changes are made by political bodies around the
   world.

.. seealso::

   * :pydoc:`datetime`

   * :ref:`Python 2 to 3 porting notes for datetime <porting-datetime>`

   * :mod:`calendar` -- The ``calendar`` module.

   * :mod:`time` -- The ``time`` module.

   * `dateutil <http://labix.org/python-dateutil>`_ -- ``dateutil``
     from Labix extends the ``datetime`` module with additional
     features.

   * pytz_ -- World Time Zone database and classes for making
     ``datetime`` objects time zone-aware.

   * `WikiPedia: Proleptic Gregorian calendar
     <https://en.wikipedia.org/wiki/Proleptic_Gregorian_calendar>`_ --
     A description of the Gregorian calendar system.

   * `ISO 8601`_ -- The standard for numeric representation of Dates
     and Time

.. _ISO 8601: http://www.iso.org/iso/support/faqs/faqs_widely_used_standards/widely_used_standards_other/iso8601

.. _pytz: http://pytz.sourceforge.net/
