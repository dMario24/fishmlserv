[project]
name = "fishmlserv"
version = "0.7.11"
description = "Serving Machine Learning Model - using sklearn(KNeighborsClassifier) using FastApi, Fly.io"
authors = [
    {name = "dMario24", email = "data.mario24@gmail.com"},
]
dependencies = [
    "fastapi>=0.112.2",
    "uvicorn[standard]>=0.30.6",
    "scikit-learn>=1.5.1",
]
requires-python = ">=3.8"
readme = "README.md"
license = {text = "MIT"}


[tool.pdm]
distribution = true

[tool.pdm.dev-dependencies]
note = [
    "notebook>=7.2.2",
    "matplotlib>=3.9.2",
]
test = [
    "pytest>=8.3.2",
    "pytest-cov>=5.0.0",
]