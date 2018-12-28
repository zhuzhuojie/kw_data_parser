===============================================
 io --- Text, Binary, and Raw Stream I/O Tools
===============================================

.. module:: io
    :synopsis: Implements file I/O and provides classes for working
               with buffers using file-like API.

:Purpose: Implements file I/O and provides classes for working with
          buffers using file-like API.

The ``io`` module implements the classes behind the interpreter's
built-in ``open()`` for file-based input and output operations. The
classes are decomposed in such a way that they can be recombined for
alternate purposes, for example to enable writing Unicode data to a
network socket.

In-memory Streams
=================

``StringIO`` provides a convenient means of working with text in
memory using the file API (``read()``, ``write()``, etc.). Using
:mod:`StringIO` to build large strings can offer performance savings
over some other string concatenation techniques in some
cases. In-memory stream buffers are also useful for testing, where
writing to a real file on disk may slow down the test suite.

Here are a few standard examples of using ``StringIO`` buffers:

.. literalinclude:: io_stringio.py
    :caption:
    :start-after: #end_pymotw_header

This example uses ``read()``, but the ``readline()`` and
``readlines()`` methods are also available. The ``StringIO``
class also provides a ``seek()`` method for jumping
around in a buffer while reading, which can be useful for rewinding if
a look-ahead parsing algorithm is being used.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'io_stringio.py'))
.. }}}

.. code-block:: none

	$ python3 io_stringio.py
	
	This goes into the buffer. And so does this.
	
	Inital value for read buffer

.. {{{end}}}

To work with raw bytes instead of Unicode text, use ``BytesIO``.

.. literalinclude:: io_bytesio.py
   :caption:
   :start-after: #end_pymotw_header

The values written to the ``BytesIO`` must be ``bytes``
rather than ``str``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'io_bytesio.py'))
.. }}}

.. code-block:: none

	$ python3 io_bytesio.py
	
	b'This goes into the buffer. \xc3\x81\xc3\x87\xc3\x8a'
	b'Inital value for read buffer'

.. {{{end}}}

Wrapping Byte Streams for Text Data
===================================

Raw byte streams such as sockets can be wrapped with a layer to handle
string encoding and decoding, making it easier to use them with text
data. The ``TextIOWrapper`` class supports writing as well as
reading.  The ``write_through`` argument disables buffering, and
flushes all data written to the wrapper through to the underlying
buffer immediately.

.. literalinclude:: io_textiowrapper.py
   :caption:
   :start-after: #end_pymotw_header

This example uses a ``BytesIO`` instance as the stream. Examples
for :mod:`bz2`, :mod:`http.server`, and :mod:`subprocess` demonstrate
using ``TextIOWrapper`` with other types of file-like objects.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'io_textiowrapper.py'))
.. }}}

.. code-block:: none

	$ python3 io_textiowrapper.py
	
	b'This goes into the buffer. \xc3\x81\xc3\x87\xc3\x8a'
	Inital value for read buffer with unicode characters ÁÇÊ

.. {{{end}}}

.. seealso::

   * :pydoc:`io`

   * :ref:`HTTP POST example <http_server_post>` -- Uses the
     ``detach()`` of ``TextIOWrapper`` to manage the wrapper
     separately from the wrapped socket.

   * `Efficient String Concatenation in Python
     <http://www.skymind.com/%7Eocrow/python_string/>`_ -- Examines
     various methods of combining strings and their relative merits.
