# MMM - Marketing Mix Model from Scratch

## What is This Project?

This is a **Marketing Mix Model (MMM) implementation from scratch** built with Python, NumPy, and Pandas. The goal is to understand how MMM works by building it from first principles, rather than using existing libraries.

### Why This is Different
Unlike other open-source MMMs, this project uses only **numpy and pandas** for data manipulation. While it may perform worse than production libraries, the goal is to **learn and truly understand how MMM works** from the ground up.

### Key Components:
- **Data Generation**: Synthetic marketing data with realistic patterns
- **Linear Regression**: Custom implementation with statistical inference
- **Adstock & Saturation**: Marketing effect transformations
- **Contribution Analysis**: ROI and attribution calculations
- **Docker Integration**: Reproducible environments
- **CI/CD Pipeline**: Automated testing and deployment

## Quick Start

### Option 1: Using Virtual Environment (Recommended for Development)
```bash
# Clone the repository
git clone <your-repo-url>
cd mmm

# Install dependencies
pip install -r requirements.txt

# Run the model
python main.py
```

### Option 2: Using Docker (Recommended for Testing/Deployment)
```bash
# Build the Docker image
docker build -t mmm-project .

# Run the model
docker run --rm mmm-project
```

## Project Structure

```
mmm/
├── main.py                 # Main execution script
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── README.md              # Project overview (this file)
├── DOCKER.md              # Detailed Docker guide
├── mmm.ipynb              # Jupyter notebook with analysis
├── build_docs.sh          # Quick documentation builder
├── src/                   # Source code
│   ├── data_generation.py # Synthetic data creation
│   ├── linear_regression.py # Custom regression implementation
│   ├── contributions.py   # ROI and attribution calculations
│   └── utils.py           # Helper functions (adstock, saturation)
├── docs/                  # Sphinx documentation
│   ├── source/            # Documentation source files
│   ├── build/             # Generated documentation
│   └── Makefile           # Sphinx build commands
├── .github/workflows/     # CI/CD pipeline
└── venv_mmm_310/          # Virtual environment
```

## Understanding the MMM Model

### Data Generation Process

The model generates synthetic marketing data with these components:

1. **Media Variables** (`x1`, `x2`): Marketing spend data
2. **Adstock Transformation**: Marketing effect persistence over time
3. **Saturation**: Diminishing returns on marketing spend
4. **Trend**: Long-term growth pattern
5. **Seasonality**: Cyclical patterns
6. **Events**: One-time marketing activities

### Key Functions

#### Adstock Transformation
```python
# Implements: Adstock_t = Media_t + α * Adstock_{t-1}
from src.utils import geometric_adstock
adstocked = geometric_adstock(media_data, alpha=0.4)
```

#### Saturation Function
```python
# Models diminishing returns
from src.utils import saturation
saturated = saturation(adstocked_data, lambda_param=2.0)
```

#### Linear Regression
```python
from src.linear_regression import LinearRegression
model = LinearRegression(df, 'y', ['x1_sat', 'x2_sat', 'trend'])
results = model.fit()
model.summary()
```

#### Contribution Analysis
```python
from src.contributions import Contributions
contrib = Contributions(df, coefficients)
decomposition = contrib.decomposition()
roi = contrib.roi(contributions, media_vars, media_costs)
```

## Development Workflow

### Using Virtual Environment (Recommended)
```bash
# Activate virtual environment
source venv_mmm_310/bin/activate

# Verify installation
python -c "import pandas, numpy, matplotlib; print('✅ All packages installed')"

# Run a quick test
python main.py
```

### Using Docker for Development
```bash
# Build development image
docker build -t mmm-dev .

# Run with interactive shell
docker run -it mmm-dev bash

# Inside container, you can:
python main.py
python -c "from src.utils import saturation; print('Test passed')"
exit
```


### Recommended Workflow
- **Local Testing**: Use virtual environment for quick iterations
- **Integration Testing**: Use Docker for complete testing
- **CI/CD Testing**: Automated testing on clean environment

## Documentation

This project includes comprehensive documentation built with Sphinx:

### View Documentation
```bash
# Build the documentation
./build_docs.sh

# Or manually
cd docs && make html
```

### Documentation Structure
- **Theory**: Mathematical foundations of MMM
- **API Reference**: Auto-generated from code docstrings
- **Tutorials**: Step-by-step guides
- **Examples**: Practical use cases

The documentation is available at `docs/build/html/index.html` after building.

**Remember**: This project is about learning and understanding MMM from first principles. Take time to experiment with parameters, understand the mathematics, and build intuition for how marketing mix modeling works!