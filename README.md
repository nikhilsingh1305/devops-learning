# DevOps Learning Project

This repository documents my hands-on journey into DevOps by building and automating a real-world application delivery pipeline.

The project covers Git, CI/CD, Python, Docker, Docker Compose, PostgreSQL, GitHub Actions, GitHub Container Registry, and will later expand into AWS, Terraform, Kubernetes, and monitoring.

## Project Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Run Tests
    │
    ├── Build Docker Image
    │
    └── Push Image to GHCR
              │
              ▼
      GitHub Container Registry
              │
              ▼
        Deployment
```

## Current Technology Stack

- Git & GitHub
- GitHub Actions
- Python
- Flask
- Pytest
- Docker
- Docker Compose
- PostgreSQL
- Gunicorn
- GitHub Container Registry (GHCR)
- Linux / Bash

## Application

The project contains a small Flask application with a `/health` endpoint.

The health check verifies:

- Application availability
- Runtime environment
- PostgreSQL database connectivity

The application uses environment variables for runtime configuration instead of hardcoded infrastructure settings.

## Docker

The application is containerized using a Dockerfile and served using Gunicorn.

Docker Compose is used to run the application and PostgreSQL together.

```text
Docker Compose
│
├── Flask Application
│      │
│      └── Gunicorn
│
└── PostgreSQL
```

The application connects to PostgreSQL using the Docker Compose service name.

## CI/CD Pipeline

GitHub Actions automatically validates and packages the application.

### Pull Request

```text
Pull Request
     │
     ▼
Run Tests
     │
     ▼
Stop
```

Pull requests validate the application but do not publish Docker images.

### Push to main

```text
Push to main
     │
     ▼
Run Tests
     │
     ▼
Build Docker Image
     │
     ▼
Push Image to GHCR
```

The Docker image is tagged using the Git commit SHA.

Example:

```text
ghcr.io/nikhilsingh1305/devops-learning:<commit-sha>
```

This provides an immutable reference to the exact build.

### Release

Version tags are used for intentional releases.

Example:

```text
Git tag: v1.0.2
```

The pipeline converts this into:

```text
ghcr.io/nikhilsingh1305/devops-learning:1.0.2
```

The same image is also tagged as:

```text
ghcr.io/nikhilsingh1305/devops-learning:latest
```

This means `1.0.2` and `latest` point to the same released image.

## Docker Image Tagging Strategy

| Tag        | Purpose                         |
| ---------- | ------------------------------- |
| Commit SHA | Exact immutable build reference |
| `1.0.2`    | Specific application release    |
| `latest`   | Current release convenience tag |

This strategy provides both **traceability** and **human-friendly release versions**.

For example:

```text
main push
    │
    └── :<commit-sha>

v1.0.2
    │
    ├── :1.0.2
    │
    └── :latest
```

## Project Roadmap

### Completed

- Git fundamentals
- Git branching and pull requests
- GitHub Actions CI
- Python application setup
- Automated testing with Pytest
- Docker containerization
- Docker image management
- Docker networking
- Docker Compose
- PostgreSQL integration
- Environment-based configuration
- Gunicorn
- GitHub Container Registry
- Automated Docker image publishing
- Commit SHA image tagging
- Semantic version release tagging
- `latest` release tagging

### Upcoming

- Automated deployment
- Deployment verification
- AWS
- Infrastructure as Code with Terraform
- Kubernetes
- Monitoring and observability
- Production-style CI/CD improvements
