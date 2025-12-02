# MSUthemes Release Checklist

Complete checklist for releasing MSUthemes to PyPI.

## Pre-Release Checklist

### Code Quality

- [x] All tests passing (`pytest`)
- [x] Code coverage > 90% (`pytest --cov=msuthemes`)
- [x] No linting errors (`flake8 msuthemes/`)
- [x] Code formatted (`black msuthemes/`)
- [x] Type hints added where appropriate
- [x] Docstrings complete and accurate

### Documentation

- [x] README.md up to date
- [x] CHANGELOG.md updated with version changes
- [x] API documentation complete
- [x] Examples working and tested
- [x] Installation instructions accurate
- [x] License file present and correct

### Package Configuration

- [x] Version number updated in `pyproject.toml`
- [x] Dependencies listed correctly
- [x] Package metadata complete (author, description, etc.)
- [x] Keywords and classifiers accurate
- [x] MANIFEST.in includes all necessary files
- [x] Font files included
- [x] Data files included

### Testing

- [x] Unit tests complete (170+ tests)
- [x] Integration tests working
- [x] Examples run without errors
- [x] Cross-platform compatibility verified
- [x] Python versions tested (3.8, 3.9, 3.10, 3.11, 3.12)

---

## Build Process

### 1. Clean Previous Builds

```bash
rm -rf build/ dist/ *.egg-info
```

### 2. Install Build Tools

```bash
pip install --upgrade build twine
```

### 3. Run Tests

```bash
pytest
pytest --cov=msuthemes
```

### 4. Build Distribution

```bash
# Using the build script
./build_package.sh

# Or manually
python -m build
```

This creates:
- Source distribution: `dist/msuthemes-0.1.0.tar.gz`
- Wheel distribution: `dist/msuthemes-0.1.0-py3-none-any.whl`

### 5. Check Distribution

```bash
twine check dist/*
```

---

## Testing the Package

### Test Local Installation

```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from wheel
pip install dist/msuthemes-0.1.0-py3-none-any.whl

# Test imports
python -c "import msuthemes; print(msuthemes.__version__)"

# Run an example
python examples/basic_usage.py

# Clean up
deactivate
rm -rf test_env
```

### Test from Test PyPI (Optional)

```bash
# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ msuthemes

# Test the installation
python -c "from msuthemes import theme_msu; print('✓ Import successful')"
```

---

## PyPI Upload

### Prerequisites

1. **PyPI Account**: Create account at https://pypi.org/account/register/
2. **API Token**: Generate at https://pypi.org/manage/account/token/
3. **Configure `.pypirc`** (in home directory):

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YourActualAPITokenHere

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YourTestPyPITokenHere
```

### Upload to PyPI

```bash
# Upload to PyPI (PRODUCTION)
twine upload dist/*

# You will be prompted to enter your credentials if not in .pypirc
```

### Verify Upload

1. Visit https://pypi.org/project/msuthemes/
2. Check that:
   - Version is correct
   - README displays properly
   - All links work
   - Classifiers are correct

---

## Post-Release

### Tag the Release

```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

### Create GitHub Release

1. Go to https://github.com/emilioxavier/msuthemes-py/releases
2. Click "Create a new release"
3. Select tag `v0.1.0`
4. Release title: "MSUthemes v0.1.0 - Initial Release"
5. Description: Copy from CHANGELOG.md
6. Attach distribution files (optional)
7. Publish release

### Update Documentation

1. Build and deploy Sphinx documentation:
   ```bash
   cd docs
   make html
   # Deploy to GitHub Pages or Read the Docs
   ```

2. Update README badges if any

### Announce Release

- [ ] Announce on department mailing list
- [ ] Share on relevant social media
- [ ] Update MSU related forums/groups
- [ ] Notify R package users of Python version

### Monitor

- [ ] Check PyPI download statistics
- [ ] Monitor GitHub issues
- [ ] Respond to user questions
- [ ] Track feature requests

---

## Version Numbering

MSUthemes follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version (1.x.x): Incompatible API changes
- **MINOR** version (x.1.x): New functionality, backwards compatible
- **PATCH** version (x.x.1): Bug fixes, backwards compatible

Current version: **0.1.0** (Alpha)

---

## Rollback Procedure

If a critical issue is discovered after release:

1. **Identify the issue**: Document the problem
2. **Fix the issue**: Create fix in a new branch
3. **Test thoroughly**: Run full test suite
4. **Create patch release**: Increment patch version (e.g., 0.1.1)
5. **Build and upload**: Follow build process above
6. **Announce**: Notify users of the patch

---

## Troubleshooting

### Build Fails

- Check Python version compatibility
- Ensure all dependencies installed
- Verify MANIFEST.in includes all files
- Check for syntax errors in pyproject.toml

### Upload Fails

- Verify API token is correct
- Check internet connection
- Ensure version doesn't already exist on PyPI
- Verify package name isn't already taken

### Installation Issues

- Check Python version requirements
- Verify all dependencies available
- Test in clean virtual environment
- Check for platform-specific issues

---

## Checklist Summary

**Pre-Release:**
- [x] Tests passing
- [x] Documentation complete
- [x] Version updated
- [x] CHANGELOG.md updated

**Build:**
- [ ] Clean build directory
- [ ] Build distributions
- [ ] Check with twine
- [ ] Test local installation

**Release:**
- [ ] Upload to PyPI
- [ ] Verify on PyPI website
- [ ] Create git tag
- [ ] Create GitHub release

**Post-Release:**
- [ ] Deploy documentation
- [ ] Announce release
- [ ] Monitor feedback

---

## Quick Reference Commands

```bash
# Complete build and test process
./build_package.sh

# Manual build
python -m build

# Check package
twine check dist/*

# Test upload
twine upload --repository testpypi dist/*

# Production upload
twine upload dist/*

# Create git tag
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

---

## Support

For questions about the release process:
- **Author**: Emilio Xavier Esposito
- **Email**: emilio@msu.edu
- **GitHub**: https://github.com/emilioxavier/msuthemes-py/issues

---

## Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Help](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
