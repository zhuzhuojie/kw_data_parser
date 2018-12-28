=========================================
 platform --- System Version Information
=========================================

.. module:: platform
    :synopsis: System version information

:Purpose: Probe the underlying platform's hardware, operating system,
          and interpreter version information.

Although Python is often used as a cross-platform language, it is
occasionally necessary to know what sort of system a program is
running on. Build tools need that information, but an application
might also know that some of the libraries or external commands it
uses have different interfaces on different operating systems. For
example, a tool to manage the network configuration of an operating
system can define a portable representation of network interfaces,
aliases, IP addresses, etc. But when the time comes to edit the
configuration files, it must know more about the host so it can use
the correct operating system configuration commands and files.  The
``platform`` module includes the tools for learning about the
interpreter, operating system, and hardware platform where a program
is running.

.. note::

    The example output in this section was generated on three systems:
    a Mac mini running macOS 10.14, a Dell PC running Ubuntu Linux
    14.04, and a VirtualBox VM running Windows 10.  Python was
    installed on the OS X and Windows systems using the pre-compiled
    installers from python.org. The Linux system is running a version
    in a system package.

    .. only:: html

      *Special thanks to Patrick Kettner (@patrickkettner) for helping
      to collect the example output on Windows.*

Interpreter
===========

There are four functions for getting information about the current
Python interpreter. ``python_version()`` and
``python_version_tuple()`` return different forms of the interpreter
version with major, minor, and patch level components.
``python_compiler()`` reports on the compiler used to build the
interpreter. And ``python_build()`` gives a version string for the
build of the interpreter.

.. literalinclude:: platform_python.py
    :caption:
    :start-after: #end_pymotw_header

OS X:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'platform_python.py'))
.. }}}

.. code-block:: none

	$ python3 platform_python.py
	
	Version      : 3.7.1
	Version tuple: ('3', '7', '1')
	Compiler     : Clang 6.0 (clang-600.0.57)
	Build        : ('v3.7.1:260ec2c36a', 'Oct 20 2018 03:13:28')

.. {{{end}}}

Linux:

.. code-block:: none

   $ python3 platform_python.py

   Version      : 3.5.2
   Version tuple: ('3', '5', '2')
   Compiler     : GCC 4.8.4
   Build        : ('default', 'Jul 17 2016 00:00:00')

Windows:

.. code-block:: none

   C:\>Desktop\platform_python.py

   Version      : 3.5.1
   Version tuple: ('3', '5', '1')
   Compiler     : MSC v.1900 64 bit (AMD64)
   Build        : ('v3.5.1:37a07cee5969', 'Dec  6 2015 01:54:25')

Platform
========

The ``platform()`` function returns a string containing a general
purpose platform identifier.  The function accepts two optional
Boolean arguments. If ``aliased`` is True, the names in the return value
are converted from a formal name to their more common form. When
``terse`` is true, a minimal value with some parts dropped is returned
instead of the full string.

.. literalinclude:: platform_platform.py
    :caption:
    :start-after: #end_pymotw_header

OS X:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'platform_platform.py'))
.. }}}

.. code-block:: none

	$ python3 platform_platform.py
	
	Normal : Darwin-18.0.0-x86_64-i386-64bit
	Aliased: Darwin-18.0.0-x86_64-i386-64bit
	Terse  : Darwin-18.0.0

.. {{{end}}}

Linux:

.. code-block:: none

   $ python3 platform_platform.py

   Normal : Linux-3.13.0-55-generic-x86_64-with-Ubuntu-14.04-trusty
   Aliased: Linux-3.13.0-55-generic-x86_64-with-Ubuntu-14.04-trusty
   Terse  : Linux-3.13.0-55-generic-x86_64-with-glibc2.9

Windows:

.. code-block:: none

   C:\>platform_platform.py

   Normal : Windows-10-10.0.10240-SP0
   Aliased: Windows-10-10.0.10240-SP0
   Terse  : Windows-10

Operating System and Hardware Info
==================================

More detailed information about the operating system and hardware the
interpreter is running under can be retrieved as well. ``uname()``
returns a tuple containing the system, node, release, version,
machine, and processor values.  Individual values can be accessed
through functions of the same names, listed in :table:`Platform
Information Functions`.

.. list-table:: Platform Information Functions
   :header-rows: 1
   :widths: 20 60

   - * Function
     * Return Value
   - * ``system()``
     * operating system name
   - * ``node()``
     * host name of the server, not fully qualified
   - * ``release()``
     * operating system release number
   - * ``version()``
     * more detailed system version
   - * ``machine()``
     * a hardware-type identifier, such as ``'i386'``
   - * ``processor()``
     * a real identifier for the processor (the same value as ``machine()`` in many cases)

.. literalinclude:: platform_os_info.py
    :caption:
    :start-after: #end_pymotw_header

OS X:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'platform_os_info.py',
..                    line_break_mode='wrap'))
.. }}}

.. code-block:: none

	$ python3 platform_os_info.py
	
	uname: uname_result(system='Darwin', node='hubert.local',
	release='18.0.0', version='Darwin Kernel Version 18.0.0: Wed Aug
	22 20:13:40 PDT 2018; root:xnu-4903.201.2~1/RELEASE_X86_64',
	machine='x86_64', processor='i386')
	
	system   : Darwin
	node     : hubert.local
	release  : 18.0.0
	version  : Darwin Kernel Version 18.0.0: Wed Aug 22 20:13:40 PDT
	2018; root:xnu-4903.201.2~1/RELEASE_X86_64
	machine  : x86_64
	processor: i386

.. {{{end}}}

Linux:

.. code-block:: none

   $ python3 platform_os_info.py

   uname: uname_result(system='Linux', node='apu',
   release='3.13.0-55-generic', version='#94-Ubuntu SMP Thu Jun 18
   00:27:10 UTC 2015', machine='x86_64', processor='x86_64')
   
   system   : Linux
   node     : apu
   release  : 3.13.0-55-generic
   version  : #94-Ubuntu SMP Thu Jun 18 00:27:10 UTC 2015
   machine  : x86_64
   processor: x86_64

Windows:

.. code-block:: none

   C:\>Desktop\platform_os_info.py

   uname: uname_result(system='Windows', node='IE11WIN10', 
   release='10', version='10.0.10240', machine='AMD64', 
   processor='Intel64 Family 6 Model 70 Stepping 1, GenuineIntel')
   
   system   : Windows
   node     : IE11WIN10
   release  : 10
   version  : 10.0.10240
   machine  : AMD64
   processor: Intel64 Family 6 Model 70 Stepping 1, GenuineIntel

Executable Architecture
=======================

Individual program architecture information can be probed using the
``architecture()`` function. The first argument is the path to an
executable program (defaulting to ``sys.executable``, the Python
interpreter). The return value is a tuple containing the bit
architecture and the linkage format used.

.. literalinclude:: platform_architecture.py
    :caption:
    :start-after: #end_pymotw_header

OS X:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'platform_architecture.py'))
.. }}}

.. code-block:: none

	$ python3 platform_architecture.py
	
	interpreter: ('64bit', '')
	/bin/ls    : ('64bit', '')

.. {{{end}}}

Linux:

.. code-block:: none

   $ python3 platform_architecture.py

   interpreter: ('64bit', 'ELF')
   /bin/ls    : ('64bit', 'ELF')

Windows:

.. code-block:: none

   C:\>Desktop\platform_architecture.py

   interpreter: ('64bit', 'WindowsPE')
   /bin/ls    : ('64bit', '')

.. seealso::

   * :pydoc:`platform`

   * :ref:`Python 2 to 3 porting notes for platform <porting-platform>`

..
   3.6.0a4 output from Brad Threatt via
   https://docs.google.com/document/d/1qRfcpEDZjOojfusW4IPcdNbGr115DxTj1CAe1HZoWAc/edit

   Interpreter:

   Version      : 3.6.0a4
   Version tuple: ('3', '6', '0a4')
   Compiler     : MSC v.1900 64 bit (AMD64)
   Build        : ('v3.6.0a4:017cf260936b', 'Aug 16 2016 00:59:16')

   Platform:

   Normal : Windows-10-10.0.10586-SP0
   Aliased: Windows-10-10.0.10586-SP0
   Terse  : Windows-10

   OS & Hardware:

   system   : Windows
   node     : DESKTOP-JDHLQQV
   release  : 10
   version  : 10.0.10586
   machine  : AMD64
   processor: Intel64 Family 6 Model 78 Stepping 3, GenuineIntel

   Arch:

   interpreter: ('64bit', 'WindowsPE')
   /bin/ls    : ('64bit', '')
