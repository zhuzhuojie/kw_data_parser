Implementing MapReduce
======================

The ``Pool`` class can be used to create a simple single-server
MapReduce implementation.  Although it does not give the full benefits
of distributed processing, it does illustrate how easy it is to break
some problems down into distributable units of work.

In a MapReduce-based system, input data is broken down into chunks for
processing by different worker instances.  Each chunk of input data is
*mapped* to an intermediate state using a simple transformation.  The
intermediate data is then collected together and partitioned based on
a key value so that all of the related values are together.  Finally,
the partitioned data is *reduced* to a result set.

.. literalinclude:: multiprocessing_mapreduce.py
    :caption:
    :start-after: #end_pymotw_header

The following example script uses SimpleMapReduce to counts the
"words" in the reStructuredText source for this article, ignoring some
of the markup.

.. literalinclude:: multiprocessing_wordcount.py
    :caption:
    :start-after: #end_pymotw_header

The ``file_to_words()`` function converts each input file to a
sequence of tuples containing the word and the number ``1`` (representing
a single occurrence). The data is divided up by ``partition()``
using the word as the key, so the resulting structure consists of a key
and a sequence of ``1`` values representing each occurrence of the word.
The partitioned data is converted to a set of tuples containing a word
and the count for that word by ``count_words()`` during the
reduction phase.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u multiprocessing_wordcount.py'))
.. }}}

.. code-block:: none

	$ python3 -u multiprocessing_wordcount.py
	
	ForkPoolWorker-1 reading basics.rst
	ForkPoolWorker-2 reading communication.rst
	ForkPoolWorker-3 reading index.rst
	ForkPoolWorker-4 reading mapreduce.rst
	
	TOP 20 WORDS BY FREQUENCY
	
	process         :    83
	running         :    45
	multiprocessing :    44
	worker          :    40
	starting        :    37
	now             :    35
	after           :    34
	processes       :    31
	start           :    29
	header          :    27
	pymotw          :    27
	caption         :    27
	end             :    27
	daemon          :    22
	can             :    22
	exiting         :    21
	forkpoolworker  :    21
	consumer        :    20
	main            :    18
	event           :    16

.. {{{end}}}
