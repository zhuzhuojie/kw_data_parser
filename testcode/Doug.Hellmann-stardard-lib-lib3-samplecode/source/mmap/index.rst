===========================
 mmap --- Memory-map Files
===========================

.. module:: mmap
    :synopsis: Memory-map files

:Purpose: Memory-map files instead of reading the contents directly.

Memory-mapping a file uses the operating system virtual memory system
to access the data on the file system directly, instead of using normal
I/O functions.  Memory-mapping typically improves I/O performance
because it does not involve a separate system call for each access and
it does not require copying data between buffers -- the memory is
accessed directly by both the kernel and the user application.

Memory-mapped files can be treated as mutable strings or file-like
objects, depending on the need. A mapped file supports the expected
file API methods, such as ``close()``, ``flush()``, ``read()``,
``readline()``, ``seek()``, ``tell()``, and ``write()``. It
also supports the string API, with features such as slicing and
methods like ``find()``.

All of the examples use the text file ``lorem.txt``, containing a bit
of Lorem Ipsum. For reference, the text of the file is

.. literalinclude:: lorem.txt
   :caption:

.. note::

  There are differences in the arguments and behaviors for
  ``mmap()`` between Unix and Windows, which are not fully discussed
  here. For more details, refer to the standard library documentation.

Reading
=======

Use the ``mmap()`` function to create a memory-mapped file.  The
first argument is a file descriptor, either from the ``fileno()``
method of a ``file`` object or from ``os.open()``. The caller
is responsible for opening the file before invoking ``mmap()``, and
closing it after it is no longer needed.

The second argument to ``mmap()`` is a size in bytes for the portion
of the file to map. If the value is ``0``, the entire file is
mapped. If the size is larger than the current size of the file, the
file is extended.

.. note::

  Windows does not support creating a zero-length mapping.

An optional keyword argument, ``access``, is supported by both
platforms. Use ``ACCESS_READ`` for read-only access,
``ACCESS_WRITE`` for write-through (assignments to the memory go
directly to the file), or ``ACCESS_COPY`` for copy-on-write
(assignments to memory are not written to the file).

.. literalinclude:: mmap_read.py
   :caption:
   :start-after: #end_pymotw_header

The file pointer tracks the last byte accessed through a slice
operation.  In this example, the pointer moves ahead 10 bytes after
the first read.  It is then reset to the beginning of the file by the
slice operation, and moved ahead 10 bytes again by the slice.  After
the slice operation, calling ``read()`` again gives the bytes 11-20
in the file.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_read.py'))
.. }}}

.. code-block:: none

	$ python3 mmap_read.py
	
	First 10 bytes via read : b'Lorem ipsu'
	First 10 bytes via slice: b'Lorem ipsu'
	2nd   10 bytes via read : b'm dolor si'

.. {{{end}}}

Writing
=======

To set up the memory mapped file to receive updates, start by opening
it for appending with mode ``'r+'`` (not ``'w'``) before mapping
it. Then use any of the API methods that change the data
(``write()``, assignment to a slice, etc.).

The next example uses the default access mode of ``ACCESS_WRITE``
and assigning to a slice to modify part of a line in place.

.. literalinclude:: mmap_write_slice.py
   :caption:
   :start-after: #end_pymotw_header

The word "``consectetuer``" is replaced in the middle of the first
line in memory and in the file.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_write_slice.py'))
.. }}}

.. code-block:: none

	$ python3 mmap_write_slice.py
	
	Looking for    : b'consectetuer'
	Replacing with : b'reutetcesnoc'
	Before:
	b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'
	After :
	b'Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit.'
	File  :
	Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit.

.. {{{end}}}

Copy Mode
---------

Using the access setting ``ACCESS_COPY`` does not write changes
to the file on disk.

.. literalinclude:: mmap_write_copy.py
   :caption:
   :start-after: #end_pymotw_header

It is necessary to rewind the file handle in this example separately
from the ``mmap`` handle, because the internal state of the two
objects is maintained separately.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_write_copy.py'))
.. }}}

.. code-block:: none

	$ python3 mmap_write_copy.py
	
	Memory Before:
	b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'
	File Before  :
	Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
	
	Memory After :
	b'Lorem ipsum dolor sit amet, reutetcesnoc adipiscing elit.'
	File After   :
	Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

.. {{{end}}}

Regular Expressions
===================

Since a memory mapped file can act like a string, it can be used with
other modules that operate on strings, such as regular
expressions. This example finds all of the sentences with "``nulla``" in
them.

.. literalinclude:: mmap_regex.py
   :caption:
   :start-after: #end_pymotw_header

Because the pattern includes two groups, the return value from
``findall()`` is a sequence of tuples. The ``print``
statement pulls out the matching sentence and replaces newlines with
spaces so each result prints on a single line.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_regex.py'))
.. }}}

.. code-block:: none

	$ python3 mmap_regex.py
	
	b'Nulla facilisi.'
	b'Nulla feugiat augue eleifend nulla.'

.. {{{end}}}


.. seealso::

   * :pydoc:`mmap`

   * :ref:`Python 2 to 3 porting notes for mmap <porting-mmap>`

   * :mod:`os` -- The ``os`` module.

   * :mod:`re` -- Regular expressions.
