Installation Guide
==================

This guide covers the installation of MSUthemes and its dependencies.

Requirements
------------

MSUthemes requires:

* Python 3.8 or higher
* NumPy >= 1.20.0
* matplotlib >= 3.5.0
* pandas >= 1.3.0

Optional dependencies:

* seaborn >= 0.12.0 (for seaborn integration)
* plotly >= 5.0.0 (for plotly support)

Installing MSUthemes
--------------------

Via pip (Recommended)
^^^^^^^^^^^^^^^^^^^^^

Once published to PyPI, install MSUthemes using pip:

.. code-block:: bash

   pip install msuthemes

To install with optional dependencies:

.. code-block:: bash

   # Install with seaborn support
   pip install msuthemes[seaborn]

   # Install with all optional dependencies
   pip install msuthemes[all]

From Source
^^^^^^^^^^^

To install the latest development version from GitHub:

.. code-block:: bash

   git clone https://github.com/emilioxavier/msuthemes-py.git
   cd msuthemes-py
   pip install -e .

For development with all dev dependencies:

.. code-block:: bash

   pip install -e .[dev]

Verifying Installation
----------------------

To verify that MSUthemes is installed correctly:

.. code-block:: python

   import msuthemes
   print(msuthemes.__version__)

   # Check available modules
   from msuthemes import colors, palettes, themes, bigten, data
   print("✓ MSUthemes installed successfully!")

Font Installation
-----------------

MSUthemes includes the Metropolis font, which is automatically bundled with the package.
The font needs to be registered with matplotlib:

.. code-block:: python

   from msuthemes import register_metropolis_fonts, is_metropolis_available

   # Register Metropolis fonts
   register_metropolis_fonts()

   # Verify font is available
   if is_metropolis_available():
       print("✓ Metropolis font is ready!")
   else:
       print("⚠ Metropolis font not available. You may need to:")
       print("  1. Clear matplotlib font cache")
       print("  2. Restart Python")

Clearing matplotlib Font Cache
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the Metropolis font is not recognized after registration, you may need to clear
matplotlib's font cache:

**On Linux/macOS:**

.. code-block:: bash

   rm -rf ~/.cache/matplotlib
   rm -rf ~/.matplotlib

**On Windows:**

.. code-block:: bash

   del /s %USERPROFILE%\.matplotlib\*
   del /s %LOCALAPPDATA%\matplotlib\*

After clearing the cache, restart Python and register the fonts again.

Troubleshooting
---------------

Import Errors
^^^^^^^^^^^^^

If you encounter import errors:

.. code-block:: python

   ModuleNotFoundError: No module named 'msuthemes'

Make sure MSUthemes is installed in your current Python environment:

.. code-block:: bash

   pip list | grep msuthemes

Font Not Found
^^^^^^^^^^^^^^

If matplotlib doesn't recognize the Metropolis font:

1. Clear matplotlib's font cache (see above)
2. Restart your Python session
3. Re-register the fonts:

.. code-block:: python

   from msuthemes import register_metropolis_fonts
   register_metropolis_fonts(verbose=True)

The ``verbose=True`` option will print detailed information about font registration.

Dataset Not Found
^^^^^^^^^^^^^^^^^

If you get a "Dataset not found" error when loading BigTen data:

.. code-block:: python

   FileNotFoundError: BigTen dataset not found

This usually means the package wasn't installed correctly. Try reinstalling:

.. code-block:: bash

   pip uninstall msuthemes
   pip install msuthemes --no-cache-dir

Dependency Conflicts
^^^^^^^^^^^^^^^^^^^^

If you encounter dependency conflicts, create a fresh virtual environment:

.. code-block:: bash

   # Using venv
   python -m venv msu_env
   source msu_env/bin/activate  # On Windows: msu_env\\Scripts\\activate
   pip install msuthemes

   # Using conda
   conda create -n msu_env python=3.11
   conda activate msu_env
   pip install msuthemes

Platform-Specific Notes
-----------------------

Windows
^^^^^^^

On Windows, you may need to install Microsoft Visual C++ 14.0 or greater for some dependencies.
Download it from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

macOS
^^^^^

On macOS, make sure you have Xcode command line tools installed:

.. code-block:: bash

   xcode-select --install

Linux
^^^^^

On Linux, you may need to install additional system dependencies:

.. code-block:: bash

   # Ubuntu/Debian
   sudo apt-get install python3-dev build-essential

   # Fedora/RHEL
   sudo dnf install python3-devel gcc

Getting Help
------------

If you encounter issues not covered here:

1. Check the `GitHub Issues <https://github.com/emilioxavier/msuthemes-py/issues>`_
2. Search for similar problems in closed issues
3. Open a new issue with:
   * Your Python version (``python --version``)
   * Your MSUthemes version (``pip show msuthemes``)
   * The complete error message
   * A minimal reproducible example

Next Steps
----------

Now that MSUthemes is installed, check out the :doc:`quickstart` guide to start creating
MSU-branded visualizations!
