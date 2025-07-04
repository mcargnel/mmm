# Docker Learning Guide - Using MMM Project

## What We Just Created

### 1. **requirements.txt**
- Lists all Python packages your project needs
- Docker will install these automatically
- Version pinning ensures consistency

### 2. **Dockerfile**
- **FROM**: Uses Python 3.10 slim image (smaller, faster)
- **WORKDIR**: Sets the working directory inside container
- **COPY**: Copies files from your computer to container
- **RUN**: Executes commands during build (installing packages)
- **ENV**: Sets environment variables
- **CMD**: Default command when container starts

### 3. **.dockerignore**
- Tells Docker which files to ignore
- Speeds up builds and reduces image size
- Excludes virtual environments, cache files, etc.

## Docker Commands You'll Use

### Building Your Image
```bash
# Build the Docker image
docker build -t mmm-project .

# What this does:
# - docker build: Build a new image
# - -t mmm-project: Tag the image with name "mmm-project"
# - .: Use current directory as build context
```

### Running Your Container
```bash
# Run the container
docker run mmm-project

# Run with interactive mode (if you want to explore)
docker run -it mmm-project bash

# Run and see the output
docker run --rm mmm-project
```

### Managing Images and Containers
```bash
# List all images
docker images

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Remove a container
docker rm <container_id>

# Remove an image
docker rmi mmm-project
```

## Step-by-Step Tutorial

### Step 1: Build Your First Image
```bash
# Navigate to your project directory
cd /path/to/your/mmm/project

# Build the image
docker build -t mmm-project .
```

**What happens during build:**
1. Docker downloads Python 3.10 slim image
2. Sets `/app` as working directory
3. Copies requirements.txt and installs packages
4. Copies your project files
5. Sets up environment variables

### Step 2: Run Your Container
```bash
# Run your MMM model
docker run --rm mmm-project
```

**Expected output:**
```
Generating Data
[Your model output here]
```

### Step 3: Interactive Exploration
```bash
# Run container with bash shell
docker run -it mmm-project bash

# Inside the container, you can:
ls -la                    # See your files
python main.py           # Run your model
python -c "import pandas; print(pandas.__version__)"  # Check versions
exit                     # Leave the container
```

## Understanding Docker Layers

Docker builds images in layers. Each instruction in your Dockerfile creates a layer:

```
Layer 1: FROM python:3.10-slim
Layer 2: WORKDIR /app
Layer 3: COPY requirements.txt
Layer 4: RUN pip install -r requirements.txt
Layer 5: COPY . .
Layer 6: ENV PYTHONPATH=/app
Layer 7: CMD ["python", "main.py"]
```

**Why this matters:**
- If you change your code but not requirements.txt, Docker reuses layers 1-4
- This makes builds much faster
- That's why we copy requirements.txt first!

## Images vs Containers: The Fundamental Difference

### The Blueprint Analogy

**Image = Blueprint**
- Contains all the instructions and files needed to run your application
- Immutable (can't be changed once created)
- Stored on disk
- Can be shared, versioned, and reused
- Like a template or recipe

**Container = Running Instance**
- A running instance created from the image
- Mutable (can be modified while running)
- Lives in memory
- Has a specific lifecycle (start, stop, delete)
- Like a house built from the blueprint
- Can create multiple containers from the same image (each container is an instance of the image)
- Multiple containers from the same image can be run in parallel

### Key Differences Summary

| Aspect | Image | Container |
|--------|-------|-----------|
| **Nature** | Static template | Dynamic running instance |
| **Storage** | On disk | In memory |
| **Mutability** | Immutable | Mutable |
| **Lifecycle** | Created once, reused many times | Created, started, stopped, deleted |
| **Sharing** | Can be pushed/pulled from registries | Cannot be shared (but can be committed to new images) |
| **Size** | Base size + layers | Minimal overhead |
| **Purpose** | Definition | Execution |

### Practical Example with Your MMM Project

```bash
# 1. IMAGE: The blueprint (what we built)
docker build -t mmm-project .          # Creates image
docker images                          # Lists images
# REPOSITORY    TAG       IMAGE ID       SIZE
# mmm-project   latest    9bb9fe5c4baf   514MB

# 2. CONTAINER: Running instances from that image
docker run --rm mmm-project            # Creates and runs container
docker run --rm mmm-project            # Creates another container (same image!)
docker run --rm mmm-project            # Creates yet another container

# 3. Multiple containers from same image
docker run -d --name mmm-1 mmm-project  # Container 1
docker run -d --name mmm-2 mmm-project  # Container 2 (same image!)
docker run -d --name mmm-3 mmm-project  # Container 3 (same image!)

# 4. See the difference
docker images                          # Shows 1 image
docker ps -a                          # Shows 3 containers
```

### Why This Matters

1. **Efficiency**: One image can spawn many containers
2. **Consistency**: All containers from the same image start identical
3. **Isolation**: Each container runs independently
4. **Scalability**: Easy to run multiple instances of your MMM model
5. **Resource Management**: Images are shared, containers are separate

### Real-World Analogy

Think of it like a restaurant:

- **Image** = Recipe book with all ingredients and instructions
- **Container** = Each time you cook the dish (same recipe, different instance)
- You can cook the same dish multiple times (multiple containers)
- Each cooking session is independent (containers don't affect each other)
- The recipe stays the same (image is immutable)

## Docker Registries: Sharing and Distribution

### What is a Docker Registry?

A **Docker Registry** is a storage and distribution system for Docker images. Think of it like a library or app store for Docker images.

### The Library Analogy

- **Registry** = Library building
- **Images** = Books in the library
- **Pulling** = Borrowing a book (downloading an image)
- **Pushing** = Donating a book (uploading your image)
- **Tags** = Different editions of the same book

### Types of Registries

#### 1. **Docker Hub** (Public Registry)
- The default, public registry at `hub.docker.com`
- Like GitHub for Docker images
- Free for public images, paid for private ones
- Examples: `python:3.10-slim`, `nginx:latest`, `postgres:13`

#### 2. **Private Registries**
- Your company's internal registry
- Cloud providers: AWS ECR, Google Container Registry, Azure Container Registry
- Self-hosted: Harbor, GitLab Container Registry, JFrog Artifactory

#### 3. **Local Registry**
- Images stored on your machine
- What you see with `docker images`

### Registry Commands

#### Pulling Images (Downloading)
```bash
# Pull from Docker Hub
docker pull python:3.10-slim
docker pull nginx:latest

# Pull from private registry
docker pull your-registry.com/myapp:v1.0

# Pull with specific tag
docker pull mmm-project:latest
```

#### Pushing Images (Uploading)
```bash
# Tag your image for a registry
docker tag mmm-project:latest yourusername/mmm-project:v1.0

# Push to Docker Hub
docker push yourusername/mmm-project:v1.0

# Push to private registry
docker push your-registry.com/mmm-project:v1.0
```

#### Working with Tags
```bash
# List all tags for an image
docker images mmm-project

# Tag your image
docker tag mmm-project:latest mmm-project:v1.0
docker tag mmm-project:latest mmm-project:stable

# Remove a tag
docker rmi mmm-project:v1.0
```

### Registry URLs and Naming

```bash
# Format: [registry-url/]username/image-name:tag

# Docker Hub (default)
docker pull python:3.10-slim                    # python:3.10-slim
docker pull yourusername/mmm-project:latest     # yourusername/mmm-project:latest

# Private registry
docker pull mycompany.com/mmm-project:v1.0      # mycompany.com/mmm-project:v1.0
docker pull 123456789.dkr.ecr.us-east-1.amazonaws.com/mmm-project:latest

# Local (no registry specified)
docker pull mmm-project:latest                  # local image
```

### Practical Example: Sharing Your MMM Project

```bash
# 1. Tag your image for sharing
docker tag mmm-project:latest yourusername/mmm-project:v1.0

# 2. Push to Docker Hub
docker push yourusername/mmm-project:v1.0

# 3. Someone else can now pull and run it
docker pull yourusername/mmm-project:v1.0
docker run yourusername/mmm-project:v1.0
```

### Why Registries Matter for Your MMM Project

1. **Collaboration**: Share your model with teammates
2. **Deployment**: Deploy the same image across environments
3. **Versioning**: Track different versions of your model
4. **Reproducibility**: Anyone can run your exact model
5. **CI/CD**: Automate building and deploying your model

### Best Practices

#### 1. **Meaningful Tags**
```bash
# Good tags
docker tag mmm-project:latest mmm-project:v1.2.3
docker tag mmm-project:latest mmm-project:stable
docker tag mmm-project:latest mmm-project:2024-01-15

# Avoid
docker tag mmm-project:latest mmm-project:latest  # Redundant
```

#### 2. **Registry Security**
```bash
# Login to private registry
docker login your-registry.com

# Login to Docker Hub
docker login

# Logout
docker logout
```

#### 3. **Image Naming**
```bash
# Good naming
yourusername/mmm-project:v1.0
company/marketing-mix-model:latest

# Avoid generic names
project:latest
app:v1.0
```

## Git + Docker: The Perfect Partnership

### Why Git and Docker Work Together

**Git** manages your source code, **Docker** manages your runtime environment. Together, they create a complete development and deployment pipeline.

### The Relationship Analogy

- **Git** = Recipe book (source code)
- **Docker** = Kitchen setup (runtime environment)
- **Git + Docker** = Complete restaurant (code + environment)

### Git-Docker Workflow

#### 1. **Development Workflow**
```bash
# 1. Make changes to your code
git add .
git commit -m "Add new MMM features"

# 2. Build new Docker image
docker build -t mmm-project:latest .

# 3. Test your changes
docker run mmm-project:latest

# 4. Push to Git
git push origin main
```

#### 2. **Version Tagging Strategy**
```bash
# Tag your Git commit
git tag v1.0.0
git push origin v1.0.0

# Tag your Docker image with same version
docker tag mmm-project:latest mmm-project:v1.0.0
docker push yourusername/mmm-project:v1.0.0
```

#### 3. **Branch-Based Development**
```bash
# Create feature branch
git checkout -b feature/new-model
# Make changes...

# Build Docker image for this branch
docker build -t mmm-project:feature-new-model .

# Test feature
docker run mmm-project:feature-new-model

# Merge and clean up
git checkout main
git merge feature/new-model
docker rmi mmm-project:feature-new-model
```

### Git Hooks for Docker

#### Pre-commit Hook (`.git/hooks/pre-commit`)
```bash
#!/bin/bash
# Build and test Docker image before commit
echo "Building Docker image..."
docker build -t mmm-project:test .
if [ $? -eq 0 ]; then
    echo "Docker build successful"
    exit 0
else
    echo "Docker build failed"
    exit 1
fi
```

#### Post-commit Hook (`.git/hooks/post-commit`)
```bash
#!/bin/bash
# Tag Docker image with commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)
docker tag mmm-project:latest mmm-project:$COMMIT_HASH
echo "Tagged Docker image with commit: $COMMIT_HASH"
```

### Dockerfile in Git Workflow

#### 1. **Dockerfile as Code**
```dockerfile
# Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
CMD ["python", "main.py"]
```

#### 2. **Git Ignore for Docker**
```gitignore
# .gitignore
# Docker artifacts
.dockerignore
docker-compose.override.yml

# But include Dockerfile and docker-compose.yml
!Dockerfile
!docker-compose.yml
```

#### 3. **Multi-stage Dockerfile for Git**
```dockerfile
# Build stage (for CI/CD)
FROM python:3.10-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "main.py"]
```

### CI/CD Integration

#### GitHub Actions Example (`.github/workflows/docker.yml`)
```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [ main ]
    tags: [ 'v*' ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Build Docker image
      run: docker build -t mmm-project:${{ github.sha }} .
    
    - name: Push to registry
      run: |
        docker tag mmm-project:${{ github.sha }} yourusername/mmm-project:latest
        docker push yourusername/mmm-project:latest
```

### What is CI/CD?

**CI/CD** stands for **Continuous Integration** and **Continuous Deployment/Delivery**. It's a set of practices and tools that automate the process of building, testing, and deploying your code every time you make a change.

- **Continuous Integration (CI):** Automatically builds and tests your code whenever you push changes to your repository (e.g., GitHub, GitLab).
- **Continuous Deployment/Delivery (CD):** Automatically deploys your application (or Docker image) to a server, cloud, or registry after passing tests.

### Why is CI/CD Important?

- **Automation:** Reduces manual work and human error
- **Consistency:** Ensures every build and deployment is done the same way
- **Speed:** Faster feedback and delivery of new features or fixes
- **Collaboration:** Teams can work together without breaking each other's work
- **Reproducibility:** Every build is versioned and traceable

### How Does CI/CD Work with Docker?

1. **Code Change:** You push code to your Git repository (e.g., GitHub)
2. **CI/CD Pipeline Triggers:** A CI/CD tool (like GitHub Actions, GitLab CI, Jenkins) detects the change
3. **Build:** The pipeline builds a new Docker image using your Dockerfile
4. **Test:** The pipeline runs tests inside the Docker container
5. **Tag & Push:** If tests pass, the image is tagged (e.g., with the commit hash or version) and pushed to a Docker registry
6. **Deploy:** Optionally, the image is deployed to a server or cloud platform

### Example: GitHub Actions for Docker

The YAML example above shows a simple GitHub Actions workflow:
- **on:** Triggers on pushes to `main` or tags starting with `v`
- **jobs:** Defines a build job that:
  - Checks out your code
  - Builds the Docker image (using the commit SHA as the tag)
  - Tags and pushes the image to Docker Hub (or another registry)

#### Step-by-Step:
1. **Push code to GitHub**
2. **GitHub Actions runs the workflow**
3. **Docker image is built and tested automatically**
4. **Image is pushed to your registry**
5. **Teammates or servers can pull and run the new image**

### Best Practices for CI/CD with Docker
- Use meaningful tags (e.g., version, commit hash)
- Run tests inside the container to ensure environment consistency
- Store secrets (like registry passwords) securely in CI/CD settings
- Keep your Dockerfile and requirements.txt up to date
- Use multi-stage builds for smaller, more secure images

### Real-World Benefits
- **No more "works on my machine"**: Every environment is identical
- **Faster releases**: New features and fixes are delivered quickly
- **Traceability**: Every image is linked to a specific code version
- **Easy rollbacks**: Deploy any previous image version instantly

## Common Patterns and Best Practices

### 1. **Multi-stage Builds** (Advanced)
For production, you might want to separate build and runtime:

```dockerfile
# Build stage
FROM python:3.10-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "main.py"]
```

### 2. **Environment Variables**
```bash
# Pass environment variables
docker run -e DATABASE_URL=postgresql://... mmm-project

# Or use a .env file
docker run --env-file .env mmm-project
```

### 3. **Volume Mounting** (for development)
```bash
# Mount your local directory to container
docker run -v $(pwd):/app mmm-project

# This allows you to edit code locally and see changes in container
```

## Troubleshooting Common Issues

### 1. **Permission Errors**
```bash
# If you get permission errors, run with user flag
docker run --user $(id -u):$(id -g) mmm-project
```

### 2. **Port Conflicts**
```bash
# If your app needs to expose a port
docker run -p 8080:8080 mmm-project
```

### 3. **Memory Issues**
```bash
# Limit memory usage
docker run --memory=2g mmm-project
```

## Next Steps for Your MMM Project

### 1. **Add Data Persistence**
```bash
# Mount a volume for data
docker run -v $(pwd)/data:/app/data mmm-project
```

### 2. **Create a Development Environment**
```dockerfile
# Dockerfile.dev
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "-m", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

### 3. **Docker Compose** (for complex setups)
```yaml
# docker-compose.yml
version: '3.8'
services:
  mmm:
    build: .
    volumes:
      - ./data:/app/data
    environment:
      - PYTHONPATH=/app
```

## Why This Matters for Your MMM Project

1. **Reproducibility**: Anyone can run your model with identical results
2. **Deployment**: Easy to deploy to cloud platforms (AWS, GCP, Azure)
3. **Collaboration**: Team members can run your model without setup issues
4. **Versioning**: Different versions of your model can coexist
5. **Scalability**: Easy to run multiple instances for A/B testing

## Practice Exercises

1. **Build and run your image**
2. **Modify main.py and rebuild** - see how Docker caches layers
3. **Add a new Python package** to requirements.txt and rebuild
4. **Create a development version** that runs Jupyter notebook
5. **Try running with different Python versions** (3.9, 3.11)

## Resources for Further Learning

- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/) - Find base images
- [Docker Compose](https://docs.docker.com/compose/) - Multi-container applications
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

Remember: Docker is a tool that becomes more valuable as your projects grow. Start simple and add complexity as needed! 