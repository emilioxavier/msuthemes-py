#!/bin/bash
# Script to build msuthemes package for PyPI distribution

set -e

echo "=================================="
echo "msuthemes-py Package Builder"
echo "=================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Clean previous builds
echo -e "${YELLOW}Step 1: Cleaning previous builds...${NC}"
rm -rf build/
rm -rf dist/
rm -rf *.egg-info
rm -rf msuthemes.egg-info
echo -e "${GREEN}✓ Clean complete${NC}"
echo ""

# Step 2: Check required tools
echo -e "${YELLOW}Step 2: Checking required tools...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python not found${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python found: $(python3 --version)${NC}"

if ! python3 -c "import build" &> /dev/null; then
    echo -e "${YELLOW}  Installing build tool...${NC}"
    python3 -m pip install build
fi
echo -e "${GREEN}✓ Build tool available${NC}"
echo ""

# Step 3: Run tests
echo -e "${YELLOW}Step 3: Running tests...${NC}"
if [ "$1" != "--skip-tests" ]; then
    python3 -m pytest tests/ -v --tb=short || {
        echo -e "${RED}✗ Tests failed. Fix errors before building.${NC}"
        exit 1
    }
    echo -e "${GREEN}✓ All tests passed${NC}"
else
    echo -e "${YELLOW}  Tests skipped (--skip-tests flag)${NC}"
fi
echo ""

# Step 4: Build source and wheel distributions
echo -e "${YELLOW}Step 4: Building distributions...${NC}"
python3 -m build
echo -e "${GREEN}✓ Build complete${NC}"
echo ""

# Step 5: List created files
echo -e "${YELLOW}Step 5: Distribution files created:${NC}"
ls -lh dist/
echo ""

# Step 6: Check package with twine
echo -e "${YELLOW}Step 6: Checking package...${NC}"
if command -v twine &> /dev/null; then
    twine check dist/*
    echo -e "${GREEN}✓ Package check passed${NC}"
else
    echo -e "${YELLOW}  Twine not found. Install with: pip install twine${NC}"
fi
echo ""

# Step 7: Display summary
echo "=================================="
echo -e "${GREEN}✓ Package build successful!${NC}"
echo "=================================="
echo ""
echo "Distribution files are in dist/:"
echo "  - Source distribution (.tar.gz)"
echo "  - Wheel distribution (.whl)"
echo ""
echo "Next steps:"
echo "  1. Test installation: pip install dist/msuthemes-0.2.0-py3-none-any.whl"
echo "  2. Upload to Test PyPI: twine upload --repository testpypi dist/*"
echo "  3. Test from Test PyPI: pip install --index-url https://test.pypi.org/simple/ msuthemes"
echo "  4. Upload to PyPI: twine upload dist/*"
echo ""
echo "See RELEASE_CHECKLIST.md for complete release process."
