#!/bin/bash

# Build and serve MMM documentation

echo "Building MMM documentation..."

# Navigate to docs directory
cd docs

# Build the documentation
make html

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Documentation built successfully!"
    echo "📁 HTML files are in: docs/build/html/"
    echo ""
    echo "To view the documentation:"
    echo "1. Open docs/build/html/index.html in your browser"
    echo "2. Or serve it locally with: python -m http.server --directory docs/build/html"
    echo ""
    echo "To serve locally on port 8000:"
    echo "python -m http.server 8000 --directory docs/build/html"
else
    echo "❌ Documentation build failed!"
    exit 1
fi 