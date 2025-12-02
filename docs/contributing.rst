Contributing to MSUthemes
=========================

Thank you for your interest in contributing to MSUthemes!

Ways to Contribute
------------------

* Report bugs and issues
* Suggest new features or enhancements
* Improve documentation
* Submit bug fixes or new features via pull requests
* Share example visualizations

Getting Started
---------------

1. Fork the repository on GitHub
2. Clone your fork locally:

   .. code-block:: bash

      git clone https://github.com/YOUR-USERNAME/msuthemes-py.git
      cd msuthemes-py

3. Install development dependencies:

   .. code-block:: bash

      pip install -e .[dev]

4. Create a new branch for your changes:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

Development Guidelines
----------------------

Code Style
^^^^^^^^^^

* Follow PEP 8 style guidelines
* Use type hints for function parameters and return values
* Write comprehensive docstrings (Google style)
* Keep functions focused and single-purpose

.. code-block:: python

   def example_function(param1: str, param2: int) -> bool:
       """Brief description of function.

       More detailed description if needed.

       Args:
           param1: Description of param1
           param2: Description of param2

       Returns:
           Description of return value

       Examples:
           >>> example_function("test", 5)
           True
       """
       # Implementation here
       return True

Testing
^^^^^^^

* Write tests for new functionality
* Ensure all tests pass before submitting:

  .. code-block:: bash

     pytest

* Aim for high test coverage:

  .. code-block:: bash

     pytest --cov=msuthemes

Documentation
^^^^^^^^^^^^^

* Update docstrings for any changed functions
* Add examples to demonstrate new features
* Update relevant documentation files in ``docs/``
* Build and review documentation locally:

  .. code-block:: bash

     cd docs
     make html
     # Open _build/html/index.html in browser

Submitting Changes
------------------

1. Commit your changes with clear, descriptive messages:

   .. code-block:: bash

      git add .
      git commit -m "Add feature: brief description

      More detailed explanation of changes if needed."

2. Push to your fork:

   .. code-block:: bash

      git push origin feature/your-feature-name

3. Create a pull request on GitHub

4. Describe your changes in the PR description:

   * What problem does this solve?
   * What changes were made?
   * Any breaking changes?
   * Related issues?

Pull Request Checklist
----------------------

Before submitting, ensure:

- [ ] Code follows PEP 8 style guidelines
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Docstrings are complete
- [ ] Examples are included
- [ ] Commit messages are clear

Reporting Issues
----------------

When reporting issues, please include:

1. Python version (``python --version``)
2. MSUthemes version (``pip show msuthemes``)
3. Operating system
4. Complete error message or traceback
5. Minimal code example to reproduce the issue

Example issue template:

.. code-block:: markdown

   **Python version:** 3.11.0
   **MSUthemes version:** 0.1.0
   **OS:** macOS 14.0

   **Description:**
   Brief description of the issue

   **Steps to reproduce:**
   ```python
   from msuthemes import theme_msu
   theme_msu()
   # Code that reproduces the issue
   ```

   **Expected behavior:**
   What you expected to happen

   **Actual behavior:**
   What actually happened

   **Error message:**
   ```
   Complete error traceback
   ```

Suggesting Features
-------------------

Feature suggestions are welcome! Please:

1. Check existing issues to avoid duplicates
2. Clearly describe the feature and its use case
3. Provide examples of how it would be used
4. Consider implementation complexity

Code of Conduct
---------------

* Be respectful and inclusive
* Provide constructive feedback
* Focus on the issue, not the person
* Help create a welcoming environment for all contributors

Development Setup
-----------------

Recommended development environment:

1. Python 3.8 or higher
2. Virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. Install in editable mode:

   .. code-block:: bash

      pip install -e .[dev]

4. Run tests:

   .. code-block:: bash

      pytest

5. Check code style:

   .. code-block:: bash

      black msuthemes/
      flake8 msuthemes/

Building Documentation
----------------------

To build documentation locally:

.. code-block:: bash

   cd docs
   pip install -r ../requirements-dev.txt
   make html

View the built documentation at ``docs/_build/html/index.html``.

Questions?
----------

If you have questions about contributing:

* Open a discussion on GitHub
* Email the maintainer: emilio@msu.edu
* Check existing issues and pull requests

Thank you for contributing to MSUthemes!
