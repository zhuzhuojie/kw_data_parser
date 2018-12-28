=============================================
 urllib.parse --- Split URLs into Components
=============================================

.. module:: urllib.parse
    :synopsis: Split URL into components

:Purpose: Split URL into components

The ``urllib.parse`` module provides functions for manipulating
URLs and their component parts, to either break them down or build
them up.

Parsing
=======

The return value from the ``urlparse()`` function is a
``ParseResult`` object that acts like a ``tuple`` with six
elements.

.. literalinclude:: urllib_parse_urlparse.py
    :caption:
    :start-after: #end_pymotw_header

The parts of the URL available through the tuple interface are the
scheme, network location, path, path segment parameters (separated
from the path by a semicolon), query, and fragment.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urlparse.py', 
..                    line_break_mode='wrap'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urlparse.py
	
	ParseResult(scheme='http', netloc='netloc', path='/path',
	params='param', query='query=arg', fragment='frag')

.. {{{end}}}

Although the return value acts like a tuple, it is really based on a
``namedtuple``, a subclass of ``tuple`` that supports
accessing the parts of the URL via named attributes as well as
indexes.  In addition to being easier to use for the programmer, the
attribute API also offers access to several values not available in
the ``tuple`` API.

.. literalinclude:: urllib_parse_urlparseattrs.py
    :caption:
    :start-after: #end_pymotw_header

The ``username`` and ``password`` are available when present in the input
URL, and set to ``None`` when not. The ``hostname`` is the same value as
``netloc``, in all lower case and with the port value stripped.  And the
``port`` is converted to an integer when present and ``None`` when not.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urlparseattrs.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urlparseattrs.py
	
	scheme  : http
	netloc  : user:pwd@NetLoc:80
	path    : /path
	params  : param
	query   : query=arg
	fragment: frag
	username: user
	password: pwd
	hostname: netloc
	port    : 80

.. {{{end}}}

The ``urlsplit()`` function is an alternative to
``urlparse()``. It behaves a little differently, because it does not
split the parameters from the URL. This is useful for URLs following
:rfc:`2396`, which supports parameters for each segment of the path.

.. literalinclude:: urllib_parse_urlsplit.py
    :caption:
    :start-after: #end_pymotw_header

Since the parameters are not split out, the tuple API will show five
elements instead of six, and there is no ``params`` attribute.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urlsplit.py', 
..                    line_break_mode='wrap'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urlsplit.py
	
	SplitResult(scheme='http', netloc='user:pwd@NetLoc:80',
	path='/p1;para/p2;para', query='query=arg', fragment='frag')
	scheme  : http
	netloc  : user:pwd@NetLoc:80
	path    : /p1;para/p2;para
	query   : query=arg
	fragment: frag
	username: user
	password: pwd
	hostname: netloc
	port    : 80

.. {{{end}}}

To simply strip the fragment identifier from a URL, such as when
finding a base page name from a URL, use ``urldefrag()``.

.. literalinclude:: urllib_parse_urldefrag.py
    :caption:
    :start-after: #end_pymotw_header

The return value is a ``DefragResult``, based on
``namedtuple``, containing the base URL and the fragment.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urldefrag.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urldefrag.py
	
	original: http://netloc/path;param?query=arg#frag
	url     : http://netloc/path;param?query=arg
	fragment: frag

.. {{{end}}}

Unparsing
=========

There are several ways to assemble the parts of a split URL back
together into a single string. The parsed URL object has a
``geturl()`` method.

.. literalinclude:: urllib_parse_geturl.py
    :caption:
    :start-after: #end_pymotw_header

``geturl()`` only works on the object returned by
``urlparse()`` or ``urlsplit()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_geturl.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_geturl.py
	
	ORIG  : http://netloc/path;param?query=arg#frag
	PARSED: http://netloc/path;param?query=arg#frag

.. {{{end}}}

A regular tuple containing strings can be combined into a URL with
``urlunparse()``.

.. literalinclude:: urllib_parse_urlunparse.py
    :caption:
    :start-after: #end_pymotw_header

While the ``ParseResult`` returned by ``urlparse()`` can be
used as a tuple, this example explicitly creates a new tuple to show
that ``urlunparse()`` works with normal tuples, too.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urlunparse.py', 
..                    line_break_mode='wrap'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urlunparse.py
	
	ORIG  : http://netloc/path;param?query=arg#frag
	PARSED: <class 'urllib.parse.ParseResult'>
	ParseResult(scheme='http', netloc='netloc', path='/path',
	params='param', query='query=arg', fragment='frag')
	TUPLE : <class 'tuple'> ('http', 'netloc', '/path', 'param',
	'query=arg', 'frag')
	NEW   : http://netloc/path;param?query=arg#frag

.. {{{end}}}

If the input URL included superfluous parts, those may be dropped from the
reconstructed URL.

.. literalinclude:: urllib_parse_urlunparseextra.py
    :caption:
    :start-after: #end_pymotw_header

In this case, ``parameters``, ``query``, and ``fragment`` are all
missing in the original URL. The new URL does not look the same as the
original, but is equivalent according to the standard.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urlunparseextra.py', 
..                    line_break_mode='wrap'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urlunparseextra.py
	
	ORIG  : http://netloc/path;?#
	PARSED: <class 'urllib.parse.ParseResult'>
	ParseResult(scheme='http', netloc='netloc', path='/path',
	params='', query='', fragment='')
	TUPLE : <class 'tuple'> ('http', 'netloc', '/path', '', '', '')
	NEW   : http://netloc/path

.. {{{end}}}

Joining
=======

In addition to parsing URLs, :mod:`urlparse` includes
``urljoin()`` for constructing absolute URLs from relative
fragments.

.. literalinclude:: urllib_parse_urljoin.py
    :caption:
    :start-after: #end_pymotw_header

In the example, the relative portion of the path (``"../"``) is taken
into account when the second URL is computed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urljoin.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urljoin.py
	
	http://www.example.com/path/anotherfile.html
	http://www.example.com/anotherfile.html

.. {{{end}}}

Non-relative paths are handled in the same way as by
``os.path.join()``.

.. literalinclude:: urllib_parse_urljoin_with_path.py
   :caption:
   :start-after: #end_pymotw_header

If the path being joined to the URL starts with a slash (``/``), it
resets the URL's path to the top level.  If it does not start with a
slash, it is appended to the end of the path for the URL.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urljoin_with_path.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urljoin_with_path.py
	
	http://www.example.com/subpath/file.html
	http://www.example.com/path/subpath/file.html

.. {{{end}}}

.. _urllib-urlencode:

Encoding Query Arguments
========================

Before arguments can be added to a URL, they need to be encoded.

.. literalinclude:: urllib_parse_urlencode.py
    :caption:
    :start-after: #end_pymotw_header

Encoding replaces special characters like spaces to ensure they are
passed to the server using a format that complies with the standard.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urlencode.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urlencode.py
	
	Encoded: q=query+string&foo=bar

.. {{{end}}}

To pass a sequence of values using separate occurrences of the
variable in the query string, set ``doseq`` to ``True`` when calling
``urlencode()``.

.. literalinclude:: urllib_parse_urlencode_doseq.py
    :caption:
    :start-after: #end_pymotw_header

The result is a query string with several values associated with the
same name.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_urlencode_doseq.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_urlencode_doseq.py
	
	Single  : foo=%5B%27foo1%27%2C+%27foo2%27%5D
	Sequence: foo=foo1&foo=foo2

.. {{{end}}}

To decode the query string, use ``parse_qs()`` or ``parse_qsl()``.

.. literalinclude:: urllib_parse_parse_qs.py
   :caption:
   :start-after: #end_pymotw_header

The return value from ``parse_qs()`` is a dictionary mapping names
to values, while ``parse_qsl()`` returns a list of tuples containing
a name and a value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_parse_qs.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_parse_qs.py
	
	parse_qs : {'foo': ['foo1', 'foo2']}
	parse_qsl: [('foo', 'foo1'), ('foo', 'foo2')]

.. {{{end}}}

Special characters within the query arguments that might cause parse
problems with the URL on the server side are "quoted" when passed to
``urlencode()``. To quote them locally to make safe versions of
the strings, use the ``quote()`` or ``quote_plus()`` functions
directly.

.. literalinclude:: urllib_parse_quote.py
    :caption:
    :start-after: #end_pymotw_header

The quoting implementation in ``quote_plus()`` is more aggressive
about the characters it replaces.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_quote.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_quote.py
	
	urlencode() : url=http%3A%2F%2Flocalhost%3A8080%2F~hellmann%2F
	quote()     : http%3A//localhost%3A8080/~hellmann/
	quote_plus(): http%3A%2F%2Flocalhost%3A8080%2F~hellmann%2F

.. {{{end}}}


To reverse the quote operations, use ``unquote()`` or
``unquote_plus()``, as appropriate.

.. literalinclude:: urllib_parse_unquote.py
    :caption:
    :start-after: #end_pymotw_header

The encoded value is converted back to a normal string URL.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'urllib_parse_unquote.py'))
.. }}}

.. code-block:: none

	$ python3 urllib_parse_unquote.py
	
	http://localhost:8080/~hellmann/
	http://localhost:8080/~hellmann/

.. {{{end}}}


.. seealso::

   * :pydoc:`urllib.parse`

   * :mod:`urllib.request` -- Retrieve the contents of a resource
     identified by a URL.

   * :rfc:`1738` -- Uniform Resource Locator (URL) syntax

   * :rfc:`1808` -- Relative URLs

   * :rfc:`2396` -- Uniform Resource Identifier (URI) generic syntax

   * :rfc:`3986` -- Uniform Resource Identifier (URI) syntax

