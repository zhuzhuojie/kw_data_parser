============================
 re --- Regular Expressions
============================

.. module:: re
    :synopsis: Searching within and changing text using formal patterns.

:Purpose: Searching within and changing text using formal patterns.

*Regular expressions* are text matching patterns described with a
formal syntax.  The patterns are interpreted as a set of instructions,
which are then executed with a string as input to produce a matching
subset or modified version of the original.  The term "regular
expressions" is frequently shortened to "regex" or "regexp" in
conversation.  Expressions can include literal text matching,
repetition, pattern composition, branching, and other sophisticated
rules.  A large number of parsing problems are easier to solve with a
regular expression than by creating a special-purpose lexer and
parser.

Regular expressions are typically used in applications that involve a
lot of text processing.  For example, they are commonly used as search
patterns in text editing programs used by developers, including vi,
emacs, and modern IDEs.  They are also an integral part of Unix
command-line utilities such as sed, grep, and awk.  Many programming
languages include support for regular expressions in the language
syntax (Perl, Ruby, Awk, and Tcl).  Other languages, such as C, C++,
and Python, support regular expressions through extension libraries.

Multiple open source implementations of regular expressions exist,
each sharing a common core syntax but with different extensions or
modifications to their advanced features.  The syntax used in Python's
``re`` module is based on the syntax used for regular expressions
in Perl, with a few Python-specific enhancements.

.. note::

    Although the formal definition of "regular expression" is limited
    to expressions that describe regular languages, some of the
    extensions supported by ``re`` go beyond describing regular
    languages.  The term "regular expression" is used here in a more
    general sense to mean any expression that can be evaluated by
    Python's ``re`` module.

Finding Patterns in Text
========================

The most common use for ``re`` is to search for patterns in text.
The ``search()`` function takes the pattern and text to scan, and
returns a ``Match`` object when the pattern is found.  If the
pattern is not found, ``search()`` returns ``None``.

Each ``Match`` object holds information about the nature of the
match, including the original input string, the regular expression
used, and the location within the original string where the pattern
occurs.

.. literalinclude:: re_simple_match.py
   :caption:
   :start-after: #end_pymotw_header

The ``start()`` and ``end()`` methods give the indexes into the
string showing where the text matched by the pattern occurs.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_simple_match.py'))
.. }}}

.. code-block:: none

	$ python3 re_simple_match.py
	
	Found "this"
	in "Does this text match the pattern?"
	from 5 to 9 ("this")

.. {{{end}}}

Compiling Expressions
=====================

Although ``re`` includes module-level functions for working with regular
expressions as text strings, it is more efficient to *compile* the
expressions a program uses frequently.  The ``compile()`` function
converts an expression string into a ``RegexObject``.

.. literalinclude:: re_simple_compiled.py
   :caption:
   :start-after: #end_pymotw_header

The module-level functions maintain a cache of compiled expressions,
but the size of the cache is limited and using compiled expressions
directly avoids the overhead associated with cache lookup.  Another advantage of using
compiled expressions is that by precompiling all of the expressions
when the module is loaded, the compilation work is shifted to
application start time, instead of occurring at a point where the program may be
responding to a user action.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_simple_compiled.py'))
.. }}}

.. code-block:: none

	$ python3 re_simple_compiled.py
	
	Text: 'Does this text match the pattern?'
	
	Seeking "this" -> match!
	Seeking "that" -> no match

.. {{{end}}}

Multiple Matches
================

So far, the example patterns have all used ``search()`` to look for
single instances of literal text strings.  The ``findall()``
function returns all of the substrings of the input that match the
pattern without overlapping.

.. literalinclude:: re_findall.py
   :caption:
   :start-after: #end_pymotw_header

This example input string includes two instances of ``ab``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_findall.py'))
.. }}}

.. code-block:: none

	$ python3 re_findall.py
	
	Found 'ab'
	Found 'ab'

.. {{{end}}}

The ``finditer()`` function returns an iterator that produces ``Match``
instances instead of the strings returned by ``findall()``.

.. literalinclude:: re_finditer.py
   :caption:
   :start-after: #end_pymotw_header

This example finds the same two occurrences of ``ab``, and the
``Match`` instance shows where they are found in the original input.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_finditer.py'))
.. }}}

.. code-block:: none

	$ python3 re_finditer.py
	
	Found 'ab' at 0:2
	Found 'ab' at 5:7

.. {{{end}}}

Pattern Syntax
==============

Regular expressions support more powerful patterns than simple literal
text strings.  Patterns can repeat, can be anchored to different
logical locations within the input, and can be expressed in compact
forms that do not require every literal character to be present in the
pattern.  All of these features are used by combining literal text
values with *meta-characters* that are part of the regular expression
pattern syntax implemented by ``re``.

.. literalinclude:: re_test_patterns.py
   :caption:
   :start-after: #end_pymotw_header

The following examples will use ``test_patterns()`` to explore how
variations in patterns change the way they match the same input text.
The output shows the input text and the substring range from each
portion of the input that matches the pattern.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_test_patterns.py'))
.. }}}

.. code-block:: none

	$ python3 re_test_patterns.py
	
	'ab' ('a' followed by 'b')
	
	  'abbaaabbbbaaaaa'
	  'ab'
	  .....'ab'
	

.. {{{end}}}

Repetition
----------

There are five ways to express repetition in a pattern.  A pattern
followed by the meta-character ``*`` is repeated zero or more times
(allowing a pattern to repeat zero times means it does not need to
appear at all to match).  If the ``*`` is replaced with ``+``, the pattern
must appear at least once.  Using ``?`` means the pattern appears zero
or one time.  For a specific number of occurrences, use ``{m}`` after
the pattern, where ``m`` is the number of times the pattern should
repeat.  Finally, to allow a variable but limited number of
repetitions, use ``{m,n}``, where ``m`` is the minimum number of
repetitions and ``n`` is the maximum.  Leaving out ``n`` (``{m,}``)
means the value must appear at least ``m`` times, with no maximum.

.. literalinclude:: re_repetition.py
   :caption:
   :start-after: #end_pymotw_header

There are more matches for ``ab*`` and ``ab?`` than ``ab+``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_repetition.py'))
.. }}}

.. code-block:: none

	$ python3 re_repetition.py
	
	'ab*' (a followed by zero or more b)
	
	  'abbaabbba'
	  'abb'
	  ...'a'
	  ....'abbb'
	  ........'a'
	
	'ab+' (a followed by one or more b)
	
	  'abbaabbba'
	  'abb'
	  ....'abbb'
	
	'ab?' (a followed by zero or one b)
	
	  'abbaabbba'
	  'ab'
	  ...'a'
	  ....'ab'
	  ........'a'
	
	'ab{3}' (a followed by three b)
	
	  'abbaabbba'
	  ....'abbb'
	
	'ab{2,3}' (a followed by two to three b)
	
	  'abbaabbba'
	  'abb'
	  ....'abbb'
	

.. {{{end}}}

When processing a repetition instruction, ``re`` will usually
consume as much of the input as possible while matching the pattern.
This so-called *greedy* behavior may result in fewer individual
matches, or the matches may include more of the input text than
intended.  Greediness can be turned off by following the repetition
instruction with ``?``.

.. literalinclude:: re_repetition_non_greedy.py
   :caption:
   :start-after: #end_pymotw_header

Disabling greedy consumption of the input for any of the patterns
where zero occurrences of ``b`` are allowed means the matched substring
does not include any ``b`` characters.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_repetition_non_greedy.py'))
.. }}}

.. code-block:: none

	$ python3 re_repetition_non_greedy.py
	
	'ab*?' (a followed by zero or more b)
	
	  'abbaabbba'
	  'a'
	  ...'a'
	  ....'a'
	  ........'a'
	
	'ab+?' (a followed by one or more b)
	
	  'abbaabbba'
	  'ab'
	  ....'ab'
	
	'ab??' (a followed by zero or one b)
	
	  'abbaabbba'
	  'a'
	  ...'a'
	  ....'a'
	  ........'a'
	
	'ab{3}?' (a followed by three b)
	
	  'abbaabbba'
	  ....'abbb'
	
	'ab{2,3}?' (a followed by two to three b)
	
	  'abbaabbba'
	  'abb'
	  ....'abb'
	

.. {{{end}}}

Character Sets
--------------

A *character set* is a group of characters, any one of which can match
at that point in the pattern.  For example, ``[ab]`` would match
either ``a`` or ``b``.

.. literalinclude:: re_charset.py
   :caption:
   :start-after: #end_pymotw_header

The greedy form of the expression (``a[ab]+``) consumes the entire
string because the first letter is ``a`` and every subsequent
character is either ``a`` or ``b``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_charset.py'))
.. }}}

.. code-block:: none

	$ python3 re_charset.py
	
	'[ab]' (either a or b)
	
	  'abbaabbba'
	  'a'
	  .'b'
	  ..'b'
	  ...'a'
	  ....'a'
	  .....'b'
	  ......'b'
	  .......'b'
	  ........'a'
	
	'a[ab]+' (a followed by 1 or more a or b)
	
	  'abbaabbba'
	  'abbaabbba'
	
	'a[ab]+?' (a followed by 1 or more a or b, not greedy)
	
	  'abbaabbba'
	  'ab'
	  ...'aa'
	

.. {{{end}}}

A character set can also be used to exclude specific characters.  The
carat (``^``) means to look for characters that are not in the set
following the carat.

.. literalinclude:: re_charset_exclude.py
   :caption:
   :start-after: #end_pymotw_header

This pattern finds all of the substrings that do not contain the
characters ``-``, ``.``, or a space.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_charset_exclude.py'))
.. }}}

.. code-block:: none

	$ python3 re_charset_exclude.py
	
	'[^-. ]+' (sequences without -, ., or space)
	
	  'This is some text -- with punctuation.'
	  'This'
	  .....'is'
	  ........'some'
	  .............'text'
	  .....................'with'
	  ..........................'punctuation'
	

.. {{{end}}}

As character sets grow larger, typing every character that should (or
should not) match becomes tedious.  A more compact format using
*character ranges* can be used to define a character set to include
all of the contiguous characters between the specified start and stop
points.

.. literalinclude:: re_charset_ranges.py
   :caption:
   :start-after: #end_pymotw_header

Here the range ``a-z`` includes the lowercase ASCII letters, and the
range ``A-Z`` includes the uppercase ASCII letters.  The ranges can
also be combined into a single character set.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_charset_ranges.py'))
.. }}}

.. code-block:: none

	$ python3 re_charset_ranges.py
	
	'[a-z]+' (sequences of lowercase letters)
	
	  'This is some text -- with punctuation.'
	  .'his'
	  .....'is'
	  ........'some'
	  .............'text'
	  .....................'with'
	  ..........................'punctuation'
	
	'[A-Z]+' (sequences of uppercase letters)
	
	  'This is some text -- with punctuation.'
	  'T'
	
	'[a-zA-Z]+' (sequences of letters of either case)
	
	  'This is some text -- with punctuation.'
	  'This'
	  .....'is'
	  ........'some'
	  .............'text'
	  .....................'with'
	  ..........................'punctuation'
	
	'[A-Z][a-z]+' (one uppercase followed by lowercase)
	
	  'This is some text -- with punctuation.'
	  'This'
	

.. {{{end}}}

As a special case of a character set, the meta-character dot, or period
(``.``), indicates that the pattern should match any single character
in that position.

.. literalinclude:: re_charset_dot.py
   :caption:
   :start-after: #end_pymotw_header

Combining the dot with repetition can result in very long matches, unless
the non-greedy form is used.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_charset_dot.py'))
.. }}}

.. code-block:: none

	$ python3 re_charset_dot.py
	
	'a.' (a followed by any one character)
	
	  'abbaabbba'
	  'ab'
	  ...'aa'
	
	'b.' (b followed by any one character)
	
	  'abbaabbba'
	  .'bb'
	  .....'bb'
	  .......'ba'
	
	'a.*b' (a followed by anything, ending in b)
	
	  'abbaabbba'
	  'abbaabbb'
	
	'a.*?b' (a followed by anything, ending in b)
	
	  'abbaabbba'
	  'ab'
	  ...'aab'
	

.. {{{end}}}



Escape Codes
------------

An even more compact representation uses escape codes for several
predefined character sets.  The escape codes recognized by ``re``
are listed in :table:`Regular Expression Escape Codes`.

.. table:: Regular Expression Escape Codes
   
   ======  =======
   Code    Meaning
   ======  =======
   ``\d``  a digit
   ``\D``  a non-digit
   ``\s``  whitespace (tab, space, newline, etc.)
   ``\S``  non-whitespace
   ``\w``  alphanumeric
   ``\W``  non-alphanumeric
   ======  =======
   
.. note::

  Escapes are indicated by prefixing the character with a backslash
  (``\``). Unfortunately, a backslash must itself be escaped in normal
  Python strings, and that results in difficult-to-read expressions.
  Using *raw* strings, which are created by prefixing the literal
  value with ``r``, eliminates this problem and maintains readability.

.. literalinclude:: re_escape_codes.py
   :caption:
   :start-after: #end_pymotw_header

These sample expressions combine escape codes with repetition to find
sequences of like characters in the input string.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_escape_codes.py'))
.. }}}

.. code-block:: none

	$ python3 re_escape_codes.py
	
	'\d+' (sequence of digits)
	
	  'A prime #1 example!'
	  .........'1'
	
	'\D+' (sequence of non-digits)
	
	  'A prime #1 example!'
	  'A prime #'
	  ..........' example!'
	
	'\s+' (sequence of whitespace)
	
	  'A prime #1 example!'
	  .' '
	  .......' '
	  ..........' '
	
	'\S+' (sequence of non-whitespace)
	
	  'A prime #1 example!'
	  'A'
	  ..'prime'
	  ........'#1'
	  ...........'example!'
	
	'\w+' (alphanumeric characters)
	
	  'A prime #1 example!'
	  'A'
	  ..'prime'
	  .........'1'
	  ...........'example'
	
	'\W+' (non-alphanumeric)
	
	  'A prime #1 example!'
	  .' '
	  .......' #'
	  ..........' '
	  ..................'!'
	

.. {{{end}}}

To match the characters that are part of the regular expression
syntax, escape the characters in the search pattern.

.. literalinclude:: re_escape_escapes.py
   :caption:
   :start-after: #end_pymotw_header

The pattern in this example escapes the backslash and plus characters,
since both are meta-characters and have special meaning in a regular
expression.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_escape_escapes.py'))
.. }}}

.. code-block:: none

	$ python3 re_escape_escapes.py
	
	'\\.\+' (escape code)
	
	  '\d+ \D+ \s+'
	  '\d+'
	  .....'\D+'
	  ..........'\s+'
	

.. {{{end}}}


Anchoring
---------

In addition to describing the content of a pattern to match, the
relative location can be specified in the input text where the pattern
should appear by using *anchoring* instructions.  :table:`Regular
Expression Anchoring Codes` lists valid anchoring codes.

.. table:: Regular Expression Anchoring Codes
   
   ======  =======
   Code    Meaning
   ======  =======
   ``^``   start of string, or line
   ``$``   end of string, or line
   ``\A``  start of string
   ``\Z``  end of string
   ``\b``  empty string at the beginning or end of a word
   ``\B``  empty string not at the beginning or end of a word
   ======  =======

.. literalinclude:: re_anchoring.py
   :caption:
   :start-after: #end_pymotw_header

The patterns in the example for matching words at the beginning and the
end of the string are different because the word at the end of the
string is followed by punctuation to terminate the sentence.  The
pattern ``\w+$`` would not match, since ``.`` is not considered an
alphanumeric character.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_anchoring.py'))
.. }}}

.. code-block:: none

	$ python3 re_anchoring.py
	
	'^\w+' (word at start of string)
	
	  'This is some text -- with punctuation.'
	  'This'
	
	'\A\w+' (word at start of string)
	
	  'This is some text -- with punctuation.'
	  'This'
	
	'\w+\S*$' (word near end of string)
	
	  'This is some text -- with punctuation.'
	  ..........................'punctuation.'
	
	'\w+\S*\Z' (word near end of string)
	
	  'This is some text -- with punctuation.'
	  ..........................'punctuation.'
	
	'\w*t\w*' (word containing t)
	
	  'This is some text -- with punctuation.'
	  .............'text'
	  .....................'with'
	  ..........................'punctuation'
	
	'\bt\w+' (t at start of word)
	
	  'This is some text -- with punctuation.'
	  .............'text'
	
	'\w+t\b' (t at end of word)
	
	  'This is some text -- with punctuation.'
	  .............'text'
	
	'\Bt\B' (t, not start or end of word)
	
	  'This is some text -- with punctuation.'
	  .......................'t'
	  ..............................'t'
	  .................................'t'
	

.. {{{end}}}

Constraining the Search
=======================

In situations where it is known in advance that only a subset of the
full input should be searched, the regular expression match can be
further constrained by telling ``re`` to limit the search range.
For example, if the pattern must appear at the front of the input,
then using ``match()`` instead of ``search()`` will anchor the
search without having to explicitly include an anchor in the search
pattern.

.. literalinclude:: re_match.py
   :caption:
   :start-after: #end_pymotw_header

Since the literal text ``is`` does not appear at the start of the
input text, it is not found using ``match()``.  The sequence appears
two other times in the text, though, so ``search()`` finds it.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_match.py'))
.. }}}

.. code-block:: none

	$ python3 re_match.py
	
	Text   : This is some text -- with punctuation.
	Pattern: is
	Match  : None
	Search : <re.Match object; span=(2, 4), match='is'>

.. {{{end}}}

The ``fullmatch()`` method requires that the entire input string
match the pattern.

.. literalinclude:: re_fullmatch.py
   :caption:
   :start-after: #end_pymotw_header

Here ``search()`` shows that the pattern does appear in the input,
but it does not consume all of the input so ``fullmatch()`` does not
report a match.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_fullmatch.py'))
.. }}}

.. code-block:: none

	$ python3 re_fullmatch.py
	
	Text       : This is some text -- with punctuation.
	Pattern    : is
	Search     : <re.Match object; span=(2, 4), match='is'>
	Full match : None

.. {{{end}}}

The ``search()`` method of a compiled regular expression accepts
optional ``start`` and ``end`` position parameters to limit the search
to a substring of the input.

.. literalinclude:: re_search_substring.py
   :caption:
   :start-after: #end_pymotw_header

This example implements a less efficient form of ``iterall()``.
Each time a match is found, the end position of that match is used for
the next search.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_search_substring.py'))
.. }}}

.. code-block:: none

	$ python3 re_search_substring.py
	
	Text: This is some text -- with punctuation.
	
	   0 :  3 = "This"
	   5 :  6 = "is"

.. {{{end}}}


Dissecting Matches with Groups
==============================

Searching for pattern matches is the basis of the powerful
capabilities provided by regular expressions.  Adding *groups* to a
pattern isolates parts of the matching text, expanding those
capabilities to create a parser.  Groups are defined by enclosing
patterns in parentheses.

.. literalinclude:: re_groups.py
   :caption:
   :start-after: #end_pymotw_header

Any complete regular expression can be converted to a group and nested
within a larger expression.  All of the repetition modifiers can be
applied to a group as a whole, requiring the entire group pattern to
repeat.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_groups.py'))
.. }}}

.. code-block:: none

	$ python3 re_groups.py
	
	'a(ab)' (a followed by literal ab)
	
	  'abbaaabbbbaaaaa'
	  ....'aab'
	
	'a(a*b*)' (a followed by 0-n a and 0-n b)
	
	  'abbaaabbbbaaaaa'
	  'abb'
	  ...'aaabbbb'
	  ..........'aaaaa'
	
	'a(ab)*' (a followed by 0-n ab)
	
	  'abbaaabbbbaaaaa'
	  'a'
	  ...'a'
	  ....'aab'
	  ..........'a'
	  ...........'a'
	  ............'a'
	  .............'a'
	  ..............'a'
	
	'a(ab)+' (a followed by 1-n ab)
	
	  'abbaaabbbbaaaaa'
	  ....'aab'
	

.. {{{end}}}

To access the substrings matched by the individual groups within a
pattern, use the ``groups()`` method of the ``Match`` object.

.. literalinclude:: re_groups_match.py
   :caption:
   :start-after: #end_pymotw_header

``Match.groups()`` returns a sequence of strings in the order of the
groups within the expression that matches the string.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_groups_match.py'))
.. }}}

.. code-block:: none

	$ python3 re_groups_match.py
	
	This is some text -- with punctuation.
	
	'^(\w+)' (word at start of string)
	
	   ('This',)
	
	'(\w+)\S*$' (word at end, with optional punctuation)
	
	   ('punctuation',)
	
	'(\bt\w+)\W+(\w+)' (word starting with t, another word)
	
	   ('text', 'with')
	
	'(\w+t)\b' (word ending with t)
	
	   ('text',)
	

.. {{{end}}}

To ask for the match of a single group, use the ``group()`` method.  This is
useful when grouping is being used to find parts of the string, but
some of the parts matched by groups are not needed in the results.

.. literalinclude:: re_groups_individual.py
   :caption:
   :start-after: #end_pymotw_header

Group ``0`` represents the string matched by the entire expression,
and subgroups are numbered starting with ``1`` in the order that their
left parenthesis appears in the expression.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_groups_individual.py'))
.. }}}

.. code-block:: none

	$ python3 re_groups_individual.py
	
	Input text            : This is some text -- with punctuation.
	Pattern               : (\bt\w+)\W+(\w+)
	Entire match          : text -- with
	Word starting with "t": text
	Word after "t" word   : with

.. {{{end}}}

Python extends the basic grouping syntax to add *named groups*.  Using
names to refer to groups makes it easier to modify the pattern over
time, without having to also modify the code using the match results.
To set the name of a group, use the syntax ``(?P<name>pattern)``.

.. literalinclude:: re_groups_named.py
   :caption:
   :start-after: #end_pymotw_header

Use ``groupdict()`` to retrieve the dictionary mapping group names
to substrings from the match.  Named patterns are included in the
ordered sequence returned by ``groups()`` as well.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_groups_named.py'))
.. }}}

.. code-block:: none

	$ python3 re_groups_named.py
	
	This is some text -- with punctuation.
	
	'^(?P<first_word>\w+)'
	   ('This',)
	   {'first_word': 'This'}
	
	'(?P<last_word>\w+)\S*$'
	   ('punctuation',)
	   {'last_word': 'punctuation'}
	
	'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)'
	   ('text', 'with')
	   {'t_word': 'text', 'other_word': 'with'}
	
	'(?P<ends_with_t>\w+t)\b'
	   ('text',)
	   {'ends_with_t': 'text'}
	

.. {{{end}}}

An updated version of ``test_patterns()`` that shows the numbered
and named groups matched by a pattern will make the following examples
easier to follow.

.. literalinclude:: re_test_patterns_groups.py
   :caption:
   :start-after: #end_pymotw_header

Since a group is itself a complete regular expression, groups can be
nested within other groups to build even more complicated expressions.

.. literalinclude:: re_groups_nested.py
   :caption:
   :start-after: #end_pymotw_header

In this case, the group ``(a*)`` matches an empty string, so the
return value from ``groups()`` includes that empty string as the
matched value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_groups_nested.py'))
.. }}}

.. code-block:: none

	$ python3 re_groups_nested.py
	
	'a((a*)(b*))' (a followed by 0-n a and 0-n b)
	
	  'abbaabbba'
	  'abb'        ('bb', '', 'bb')
	     'aabbb'   ('abbb', 'a', 'bbb')
	          'a'  ('', '', '')
	

.. {{{end}}}

Groups are also useful for specifying alternative patterns.  Use the
pipe symbol (``|``) to separate two patterns and indicate that either pattern should
match.  Consider the placement of the pipe carefully, though.  The
first expression in this example matches a sequence of ``a`` followed
by a sequence consisting entirely of a single letter, ``a`` or ``b``.
The second pattern matches ``a`` followed by a sequence that may
include *either* ``a`` or ``b``.  The patterns are similar, but the
resulting matches are completely different.

.. literalinclude:: re_groups_alternative.py
   :caption:
   :start-after: #end_pymotw_header

When an alternative group is not matched, but the entire pattern does
match, the return value of ``groups()`` includes a ``None`` value at
the point in the sequence where the alternative group should appear.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_groups_alternative.py'))
.. }}}

.. code-block:: none

	$ python3 re_groups_alternative.py
	
	'a((a+)|(b+))' (a then seq. of a or seq. of b)
	
	  'abbaabbba'
	  'abb'        ('bb', None, 'bb')
	     'aa'      ('a', 'a', None)
	
	'a((a|b)+)' (a then seq. of [ab])
	
	  'abbaabbba'
	  'abbaabbba'  ('bbaabbba', 'a')
	

.. {{{end}}}

Defining a group containing a subpattern is also useful in cases
where the string matching the subpattern is not part of what should
be extracted from the full text.  These kinds of groups are called
*non-capturing*.  Non-capturing groups can be used to describe
repetition patterns or alternatives, without isolating the matching
portion of the string in the value returned.  To create a
non-capturing group, use the syntax ``(?:pattern)``.

.. literalinclude:: re_groups_noncapturing.py
   :caption:
   :start-after: #end_pymotw_header

In the following example, compare the groups returned for the capturing and non-capturing forms
of a pattern that matches the same results.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_groups_noncapturing.py'))
.. }}}

.. code-block:: none

	$ python3 re_groups_noncapturing.py
	
	'a((a+)|(b+))' (capturing form)
	
	  'abbaabbba'
	  'abb'        ('bb', None, 'bb')
	     'aa'      ('a', 'a', None)
	
	'a((?:a+)|(?:b+))' (noncapturing)
	
	  'abbaabbba'
	  'abb'        ('bb',)
	     'aa'      ('a',)
	

.. {{{end}}}


Search Options
==============

Option flags are used to change the way the matching engine processes
an expression.  The flags can be combined using a bitwise OR
operation, then passed to ``compile()``, ``search()``, ``match()``,
and other functions that accept a pattern for searching.

Case-insensitive Matching
-------------------------

``IGNORECASE`` causes literal characters and character ranges in
the pattern to match both uppercase and lowercase characters.

.. literalinclude:: re_flags_ignorecase.py
   :caption:
   :start-after: #end_pymotw_header

Since the pattern includes the literal ``T``, if ``IGNORECASE`` is not
set, the only match is the word ``This``.  When case is ignored,
``text`` also matches.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_flags_ignorecase.py'))
.. }}}

.. code-block:: none

	$ python3 re_flags_ignorecase.py
	
	Text:
	  'This is some text -- with punctuation.'
	Pattern:
	  \bT\w+
	Case-sensitive:
	  'This'
	Case-insensitive:
	  'This'
	  'text'

.. {{{end}}}

Input with Multiple Lines
-------------------------

Two flags affect how searching in multi-line input
works: ``MULTILINE`` and ``DOTALL``.  The ``MULTILINE``
flag controls how the pattern matching code processes anchoring
instructions for text containing newline characters.  When multiline
mode is turned on, the anchor rules for ``^`` and ``$`` apply at the
beginning and end of each line, in addition to the entire string.

.. literalinclude:: re_flags_multiline.py
   :caption:
   :start-after: #end_pymotw_header

The pattern in the example matches the first or last word of the
input.  It matches ``line.`` at the end of the string, even though
there is no newline.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_flags_multiline.py'))
.. }}}

.. code-block:: none

	$ python3 re_flags_multiline.py
	
	Text:
	  'This is some text -- with punctuation.\nA second line.'
	Pattern:
	  (^\w+)|(\w+\S*$)
	Single Line :
	  ('This', '')
	  ('', 'line.')
	Multline    :
	  ('This', '')
	  ('', 'punctuation.')
	  ('A', '')
	  ('', 'line.')

.. {{{end}}}

``DOTALL`` is the other flag related to multiline text.  Normally,
the dot character (``.``) matches everything in the input text except a
newline character.  The flag allows the dot to match newlines as well.

.. literalinclude:: re_flags_dotall.py
   :caption:
   :start-after: #end_pymotw_header

Without the flag, each line of the input text matches the pattern
separately.  Adding the flag causes the entire string to be consumed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_flags_dotall.py'))
.. }}}

.. code-block:: none

	$ python3 re_flags_dotall.py
	
	Text:
	  'This is some text -- with punctuation.\nA second line.'
	Pattern:
	  .+
	No newlines :
	  'This is some text -- with punctuation.'
	  'A second line.'
	Dotall      :
	  'This is some text -- with punctuation.\nA second line.'

.. {{{end}}}

Unicode
-------

Under Python 3, ``str`` objects use the full Unicode character
set, and regular expression processing on a ``str`` assumes that the
pattern and input text are both Unicode.  The escape codes described
earlier are defined in terms of Unicode by default.  Those assumptions
mean that the pattern ``\w+`` will match both the words "French" and
"Français". To restrict escape codes to the ASCII character set, as
was the default in Python 2, use the ``ASCII`` flag when
compiling the pattern or when calling the module-level functions
``search()`` and ``match()``.

.. literalinclude:: re_flags_ascii.py
   :caption:
   :start-after: #end_pymotw_header

The other escape sequences (``\W``, ``\b``, ``\B``, ``\d``, ``\D``,
``\s``, and ``\S``) are also processed differently for ASCII text.
Instead of consulting the Unicode database to find the properties of
each character, ``re`` uses the ASCII definition of the character set.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_flags_ascii.py'))
.. }}}

.. code-block:: none

	$ python3 re_flags_ascii.py
	
	Text    : Français złoty Österreich
	Pattern : \w+
	ASCII   : ['Fran', 'ais', 'z', 'oty', 'sterreich']
	Unicode : ['Français', 'złoty', 'Österreich']

.. {{{end}}}

Verbose Expression Syntax
-------------------------

The compact format of regular expression syntax can become a hindrance
as expressions grow more complicated.  As the number of groups in an
expression increases, it will be more work to keep track of why each
element is needed and how exactly the parts of the expression
interact.  Using named groups helps mitigate these issues, but a
better solution is to use *verbose mode* expressions, which allow
comments and extra whitespace to be embedded in the pattern.

A pattern to validate email addresses will illustrate how verbose mode
makes working with regular expressions easier.  The first version
recognizes addresses that end in one of three top-level domains:
``.com``, ``.org``, or ``.edu``.

.. literalinclude:: re_email_compact.py
   :caption:
   :start-after: #end_pymotw_header

This expression is already complex.  There are several character
classes, groups, and repetition expressions.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_email_compact.py'))
.. }}}

.. code-block:: none

	$ python3 re_email_compact.py
	
	first.last@example.com          Matches
	first.last+category@gmail.com   Matches
	valid-address@mail.example.com  Matches
	not-valid@example.foo           No match

.. {{{end}}}

Converting the expression to a more verbose format will make it easier
to extend.

.. literalinclude:: re_email_verbose.py
   :caption:
   :start-after: #end_pymotw_header

The expression matches the same inputs, but in this extended format it
is easier to read.  The comments also help identify different parts of
the pattern so that it can be expanded to match more inputs.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_email_verbose.py'))
.. }}}

.. code-block:: none

	$ python3 re_email_verbose.py
	
	first.last@example.com          Matches
	first.last+category@gmail.com   Matches
	valid-address@mail.example.com  Matches
	not-valid@example.foo           No match

.. {{{end}}}

This expanded version parses inputs that include a person's name and
email address, as might appear in an email header.  The name comes
first and stands on its own, and the email address follows, surrounded
by angle brackets (``<`` and ``>``).

.. literalinclude:: re_email_with_name.py
   :caption:
   :start-after: #end_pymotw_header

As with other programming languages, the ability to insert comments
into verbose regular expressions helps with their maintainability.
This final version includes implementation notes to future maintainers
and whitespace to separate the groups from each other and highlight
their nesting level.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_email_with_name.py'))
.. }}}

.. code-block:: none

	$ python3 re_email_with_name.py
	
	Candidate: first.last@example.com
	  Name : None
	  Email: first.last@example.com
	Candidate: first.last+category@gmail.com
	  Name : None
	  Email: first.last+category@gmail.com
	Candidate: valid-address@mail.example.com
	  Name : None
	  Email: valid-address@mail.example.com
	Candidate: not-valid@example.foo
	  No match
	Candidate: First Last <first.last@example.com>
	  Name : First Last
	  Email: first.last@example.com
	Candidate: No Brackets first.last@example.com
	  Name : None
	  Email: first.last@example.com
	Candidate: First Last
	  No match
	Candidate: First Middle Last <first.last@example.com>
	  Name : First Middle Last
	  Email: first.last@example.com
	Candidate: First M. Last <first.last@example.com>
	  Name : First M. Last
	  Email: first.last@example.com
	Candidate: <first.last@example.com>
	  Name : None
	  Email: first.last@example.com

.. {{{end}}}

Embedding Flags in Patterns
---------------------------

In situations where flags cannot be added when compiling an
expression, such as when a pattern is passed as an argument to a
library function that will compile it later, the flags can be embedded
inside the expression string itself.  For example, to turn
case-insensitive matching on, add ``(?i)`` to the beginning of the
expression.

.. literalinclude:: re_flags_embedded.py
   :caption:
   :start-after: #end_pymotw_header

Because the options control the way the entire expression is evaluated
or parsed, they should always appear at the beginning of the expression.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_flags_embedded.py'))
.. }}}

.. code-block:: none

	$ python3 re_flags_embedded.py
	
	Text      : This is some text -- with punctuation.
	Pattern   : (?i)\bT\w+
	Matches   : ['This', 'text']

.. {{{end}}}

The abbreviations for all of the flags are listed in :table:`Regular
Expression Flag Abbreviations`.

.. list-table:: Regular Expression Flag Abbreviations
   :header-rows: 1

   - * Flag
     * Abbreviation
   - * ``ASCII``
     * ``a``
   - * ``IGNORECASE``
     * ``i``
   - * ``MULTILINE``
     * ``m``
   - * ``DOTALL``
     * ``s``
   - * ``VERBOSE``
     * ``x``

Embedded flags can be combined by placing them within the same group.
For example, ``(?im)`` turns on case-insensitive matching for
multiline strings.

Looking Ahead or Behind
=======================

In many cases, it is useful to match a part of a pattern
only if some other part will also match.  For example, in the email
parsing expression, the angle brackets were marked as optional.
Realistically, the brackets should be paired, and the expression
should match only if both are present, or neither is.  This modified
version of the expression uses a *positive look ahead* assertion to
match the pair.  The look ahead assertion syntax is ``(?=pattern)``.

.. literalinclude:: re_look_ahead.py
   :caption:
   :start-after: #end_pymotw_header

There are several important changes in this version of the expression.
First, the name portion is no longer optional.  That means stand-alone
addresses do not match, but it also prevents improperly formatted
name/address combinations from matching.  The positive look ahead rule
after the "name" group asserts that either the remainder of the string
is wrapped with a pair of angle brackets, or there is not a mismatched
bracket; either both of or neither of the brackets is present.  The look
ahead is expressed as a group, but the match for a look ahead group
does not consume any of the input text, so the rest of the pattern
picks up from the same spot after the look ahead matches.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_look_ahead.py'))
.. }}}

.. code-block:: none

	$ python3 re_look_ahead.py
	
	Candidate: First Last <first.last@example.com>
	  Name : First Last
	  Email: first.last@example.com
	Candidate: No Brackets first.last@example.com
	  Name : No Brackets
	  Email: first.last@example.com
	Candidate: Open Bracket <first.last@example.com
	  No match
	Candidate: Close Bracket first.last@example.com>
	  No match

.. {{{end}}}

A *negative look ahead* assertion (``(?!pattern)``) says that the
pattern does not match the text following the current point.  For
example, the email recognition pattern could be modified to ignore
the ``noreply`` mailing addresses commonly used by automated systems.

.. literalinclude:: re_negative_look_ahead.py
   :caption:
   :start-after: #end_pymotw_header

The address starting with ``noreply`` does not match the pattern,
since the look ahead assertion fails.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_negative_look_ahead.py'))
.. }}}

.. code-block:: none

	$ python3 re_negative_look_ahead.py
	
	Candidate: first.last@example.com
	  Match: first.last@example.com
	Candidate: noreply@example.com
	  No match

.. {{{end}}}

Instead of looking ahead for ``noreply`` in the username portion of
the email address, the pattern can alternatively be written using a *negative
look behind* assertion after the username is matched using the syntax
``(?<!pattern)``.

.. literalinclude:: re_negative_look_behind.py
   :caption:
   :start-after: #end_pymotw_header

Looking backward works a little differently than looking ahead, in
that the expression must use a fixed-length pattern.  Repetitions are
allowed, as long as there is a fixed number of them (no wildcards or ranges).

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_negative_look_behind.py'))
.. }}}

.. code-block:: none

	$ python3 re_negative_look_behind.py
	
	Candidate: first.last@example.com
	  Match: first.last@example.com
	Candidate: noreply@example.com
	  No match

.. {{{end}}}

A *positive look behind* assertion can be used to find text following
a pattern using the syntax ``(?<=pattern)``.  In the following example, the
expression finds Twitter handles.

.. literalinclude:: re_look_behind.py
   :caption:
   :start-after: #end_pymotw_header

The pattern matches sequences of characters that can make up a Twitter
handle, as long as they are preceded by an ``@``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_look_behind.py'))
.. }}}

.. code-block:: none

	$ python3 re_look_behind.py
	
	This text includes two Twitter handles.
	One for @ThePSF, and one for the author, @doughellmann.
	
	Handle: ThePSF
	Handle: doughellmann

.. {{{end}}}

Self-referencing Expressions
============================

Matched values can be used in later parts of an expression.  For
example, the email example can be updated to match only addresses
composed of the first and last names of the person by including
back-references to those groups.  The easiest way to achieve this is
by referring to the previously matched group by ID number, using
``\num``.

.. literalinclude:: re_refer_to_group.py
   :caption:
   :start-after: #end_pymotw_header

Although the syntax is simple, creating back-references by numerical
ID has a few disadvantages.  From a practical standpoint, as the
expression changes, the groups must be counted again and every
reference may need to be updated.  Another disadvantage is that only
99 references can be made using the standard back-reference syntax
``\n``, because if the ID number is three digits long, it will be
interpreted as an octal character value instead of a group
reference.  Of course, if there are more than 99 groups in an
expression, there will be more serious maintenance challenges than simply not
being able to refer to all of them.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_refer_to_group.py'))
.. }}}

.. code-block:: none

	$ python3 re_refer_to_group.py
	
	Candidate: First Last <first.last@example.com>
	  Match name : First Last
	  Match email: first.last@example.com
	Candidate: Different Name <first.last@example.com>
	  No match
	Candidate: First Middle Last <first.last@example.com>
	  Match name : First Last
	  Match email: first.last@example.com
	Candidate: First M. Last <first.last@example.com>
	  Match name : First Last
	  Match email: first.last@example.com

.. {{{end}}}

Python's expression parser includes an extension that uses
``(?P=name)`` to refer to the value of a named group matched earlier
in the expression.

.. literalinclude:: re_refer_to_named_group.py
   :caption:
   :start-after: #end_pymotw_header

The address expression is compiled with the ``IGNORECASE`` flag
on, since proper names are normally capitalized but email addresses
are not.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_refer_to_named_group.py'))
.. }}}

.. code-block:: none

	$ python3 re_refer_to_named_group.py
	
	Candidate: First Last <first.last@example.com>
	  Match name : First Last
	  Match email: first.last@example.com
	Candidate: Different Name <first.last@example.com>
	  No match
	Candidate: First Middle Last <first.last@example.com>
	  Match name : First Last
	  Match email: first.last@example.com
	Candidate: First M. Last <first.last@example.com>
	  Match name : First Last
	  Match email: first.last@example.com

.. {{{end}}}

The other mechanism for using back-references in expressions chooses a
different pattern based on whether a previous group matched.
The email pattern can be corrected so that the angle brackets are
required if a name is present, and not required if the email address is by
itself.  The syntax for testing whether if a group has matched is
``(?(id)yes-expression|no-expression)``, where ``id`` is the group
name or number, ``yes-expression`` is the pattern to use if the group
has a value, and ``no-expression`` is the pattern to use otherwise.

.. literalinclude:: re_id.py
   :caption:
   :start-after: #end_pymotw_header

This version of the email address parser uses two tests.  If the
``name`` group matches, then the look ahead assertion requires both
angle brackets and sets up the ``brackets`` group.  If ``name`` is not
matched, the assertion requires the rest of the text to not have angle
brackets around it.  Later, if the ``brackets`` group is set, the
actual pattern matching code consumes the brackets in the input using
literal patterns; otherwise, it consumes any blank space.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_id.py'))
.. }}}

.. code-block:: none

	$ python3 re_id.py
	
	Candidate: First Last <first.last@example.com>
	  Match name : First Last
	  Match email: first.last@example.com
	Candidate: No Brackets first.last@example.com
	  No match
	Candidate: Open Bracket <first.last@example.com
	  No match
	Candidate: Close Bracket first.last@example.com>
	  No match
	Candidate: no.brackets@example.com
	  Match name : None
	  Match email: no.brackets@example.com

.. {{{end}}}


Modifying Strings with Patterns
===============================

In addition to searching through text, ``re`` supports
modifying text using regular expressions as the search mechanism, and
the replacements can reference groups matched in the pattern as part of
the substitution text.  Use ``sub()`` to replace all occurrences of a
pattern with another string.

.. literalinclude:: re_sub.py
   :caption:
   :start-after: #end_pymotw_header

References to the text matched by the pattern can be inserted using
the ``\num`` syntax used for back-references.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_sub.py'))
.. }}}

.. code-block:: none

	$ python3 re_sub.py
	
	Text: Make this **bold**.  This **too**.
	Bold: Make this <b>bold</b>.  This <b>too</b>.

.. {{{end}}}

To use named groups in the substitution, use the syntax ``\g<name>``.

.. literalinclude:: re_sub_named_groups.py
   :caption:
   :start-after: #end_pymotw_header

The ``\g<name>`` syntax also works with numbered references, and using
it eliminates any ambiguity between group numbers and surrounding
literal digits.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_sub_named_groups.py'))
.. }}}

.. code-block:: none

	$ python3 re_sub_named_groups.py
	
	Text: Make this **bold**.  This **too**.
	Bold: Make this <b>bold</b>.  This <b>too</b>.

.. {{{end}}}

Pass a value to ``count`` to limit the number of substitutions
performed.

.. literalinclude:: re_sub_count.py
   :caption:
   :start-after: #end_pymotw_header

Only the first substitution is made because ``count`` is ``1``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_sub_count.py'))
.. }}}

.. code-block:: none

	$ python3 re_sub_count.py
	
	Text: Make this **bold**.  This **too**.
	Bold: Make this <b>bold</b>.  This **too**.

.. {{{end}}}

``subn()`` works just like ``sub()`` except that it returns both
the modified string and the count of substitutions made.

.. literalinclude:: re_subn.py
   :caption:
   :start-after: #end_pymotw_header

The search pattern matches twice in the example.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_subn.py'))
.. }}}

.. code-block:: none

	$ python3 re_subn.py
	
	Text: Make this **bold**.  This **too**.
	Bold: ('Make this <b>bold</b>.  This <b>too</b>.', 2)

.. {{{end}}}

Splitting with Patterns
=======================

``str.split()`` is one of the most frequently used methods for
breaking apart strings to parse them.  It supports only the use of literal
values as separators, though, and sometimes a regular expression is
necessary if the input is not consistently formatted.  For example,
many plain text markup languages define paragraph separators as two or
more newline (``\n``) characters.  In this case, ``str.split()``
cannot be used because of the "or more" part of the definition.

A strategy for identifying paragraphs using ``findall()`` would use
a pattern like ``(.+?)\n{2,}``.

.. literalinclude:: re_paragraphs_findall.py
   :caption:
   :start-after: #end_pymotw_header

That pattern fails for paragraphs at the end of the input text, as
illustrated by the fact that "Paragraph three." is not part of the
output.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_paragraphs_findall.py'))
.. }}}

.. code-block:: none

	$ python3 re_paragraphs_findall.py
	
	0 'Paragraph one\non two lines.'
	
	1 'Paragraph two.'
	

.. {{{end}}}

Extending the pattern to say that a paragraph ends with two or more
newlines or the end of input fixes the problem, but makes the pattern
more complicated.  Converting to ``re.split()`` instead of
``re.findall()`` handles the boundary condition automatically and
keeps the pattern simpler.

.. literalinclude:: re_split.py
   :caption:
   :start-after: #end_pymotw_header

The pattern argument to ``split()`` expresses the markup
specification more precisely. Two or more newline characters mark a
separator point between paragraphs in the input string.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_split.py'))
.. }}}

.. code-block:: none

	$ python3 re_split.py
	
	With findall:
	0 ('Paragraph one\non two lines.', '\n\n')
	
	1 ('Paragraph two.', '\n\n\n')
	
	2 ('Paragraph three.', '')
	
	
	With split:
	0 'Paragraph one\non two lines.'
	
	1 'Paragraph two.'
	
	2 'Paragraph three.'
	

.. {{{end}}}

Enclosing the expression in parentheses to define a group causes
``split()`` to work more like ``str.partition()``, so it returns
the separator values as well as the other parts of the string.

.. literalinclude:: re_split_groups.py
   :caption:
   :start-after: #end_pymotw_header

The output now includes each paragraph, as well as the sequence of
newlines separating them.

.. {{{cog
.. cog.out(run_script(cog.inFile, 're_split_groups.py'))
.. }}}

.. code-block:: none

	$ python3 re_split_groups.py
	
	With split:
	0 'Paragraph one\non two lines.'
	
	1 '\n\n'
	
	2 'Paragraph two.'
	
	3 '\n\n\n'
	
	4 'Paragraph three.'
	

.. {{{end}}}

.. seealso::

   * :pydoc:`re`

   * `Regular Expression HOWTO
     <https://docs.python.org/3.5/howto/regex.html>`__ -- Andrew
     Kuchling's introduction to regular expressions for Python
     developers.

   * `Kodos <http://kodos.sourceforge.net/>`_ -- An interactive
     regular expression testing tool by Phil Schwartz.

   * `pythex <http://pythex.org>`_ -- A web-based tool for testing
     regular expressions created by Gabriel Rodríguez.  Inspired by
     Rubular.

   * `Wikipedia: Regular expression
     <https://en.wikipedia.org/wiki/Regular_expressions>`__ -- General
     introduction to regular expression concepts and techniques.

   * :mod:`locale` -- Use the ``locale`` module to set the language
     configuration when working with Unicode text.

   * :mod:`unicodedata` -- Programmatic access to the Unicode
     character property database.
