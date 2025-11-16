#!/bin/bash
# Script to run MSUthemes test suite

set -e

echo "=================================="
echo "MSUthemes Test Suite"
echo "=================================="
echo ""

# Default options
COVERAGE=true
MARKERS=""
VERBOSE="-v"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --no-coverage)
            COVERAGE=false
            shift
            ;;
        --unit)
            MARKERS="-m unit"
            shift
            ;;
        --integration)
            MARKERS="-m integration"
            shift
            ;;
        --slow)
            MARKERS="-m slow"
            shift
            ;;
        --fast)
            MARKERS="-m 'not slow'"
            shift
            ;;
        --quiet)
            VERBOSE="-q"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--no-coverage] [--unit] [--integration] [--slow] [--fast] [--quiet]"
            exit 1
            ;;
    esac
done

# Build pytest command
PYTEST_CMD="pytest tests/"

if [ "$COVERAGE" = true ]; then
    PYTEST_CMD="$PYTEST_CMD --cov=msuthemes --cov-report=term-missing --cov-report=html"
fi

PYTEST_CMD="$PYTEST_CMD $VERBOSE $MARKERS"

echo "Running: $PYTEST_CMD"
echo ""

# Run tests
$PYTEST_CMD

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "=================================="
    echo "✓ All tests passed!"
    echo "=================================="

    if [ "$COVERAGE" = true ]; then
        echo ""
        echo "Coverage report generated in htmlcov/index.html"
    fi
else
    echo ""
    echo "=================================="
    echo "✗ Some tests failed"
    echo "=================================="
    exit 1
fi
