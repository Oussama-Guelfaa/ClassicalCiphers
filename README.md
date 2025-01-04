# Classical Ciphers Project

This project is a Python implementation of classical encryption ciphers, including Caesar, Playfair, and Vigenère ciphers. The repository also includes unit tests to ensure correctness, static code analysis setup with Flake8, and pre-commit hooks to maintain code quality.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Static Code Analysis with Flake8](#static-code-analysis-with-flake8)
- [Pre-Commit Hooks](#pre-commit-hooks)
- [Unit Testing](#unit-testing)
- [How to Contribute](#how-to-contribute)
- [License](#license)

---

## Project Overview
The Classical Ciphers project showcases implementations of three widely known classical encryption methods:
- **Caesar Cipher**
- **Playfair Cipher**
- **Vigenère Cipher**

These implementations are located in the `ciphers` directory and are designed to encrypt and decrypt textual data.

---

## Features
- **Encryption and Decryption**:
  - Each cipher class includes methods for both encrypting and decrypting text.
- **Unit Tests**:
  - Comprehensive tests for all ciphers using `pytest`.
- **Static Code Analysis**:
  - Ensures PEP 8 compliance and high code quality with Flake8.
- **Pre-Commit Hooks**:
  - Automatically checks code for formatting and quality issues before commits.

---

## Setup Instructions

### Prerequisites
Ensure that you have Python 3.7 or above installed on your system. Install `pip` if not already available.

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ClassicalCiphers.git
   cd ClassicalCiphers
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

---

## Static Code Analysis with Flake8

We use **Flake8** to ensure that the codebase adheres to PEP 8 standards.

### Why Flake8?
Flake8 catches stylistic errors, unused imports, and code smells before the code is executed, making the project more maintainable and professional.

### Installation
To install Flake8:
```bash
pip install flake8
```

### Configuration
A `.flake8` configuration file is included in the root directory with the following settings:
```ini
[flake8]
max-line-length = 88
ignore = E501,W503
exclude =
    .git,
    __pycache__,
    env/
```
- **max-line-length**: Limits lines to 88 characters.
- **ignore**: Ignores specific style violations.
- **exclude**: Skips checking for specified directories.

### Running Flake8
To check the codebase:
```bash
flake8 .
```
This will analyze all Python files in the project directory and subdirectories.

### Fixing Issues
You can manually fix reported issues or use a tool like `black` for automatic formatting:
```bash
pip install black
black .
```
Re-run `flake8` to ensure all issues are resolved.

---

## Pre-Commit Hooks

Pre-commit hooks are configured to automatically run Flake8 checks before each commit.

### Setting Up Pre-Commit
1. Install the pre-commit tool:
   ```bash
   pip install pre-commit
   ```

2. Install the hooks defined in `.pre-commit-config.yaml`:
   ```bash
   pre-commit install
   ```

3. Test the setup by making a commit:
   ```bash
   git add .
   git commit -m "Test pre-commit"
   ```
   Flake8 will run automatically and block the commit if any issues are detected.

---

## Unit Testing

We use `pytest` for unit testing to ensure the correctness of cipher implementations.

### Running Tests
1. Install `pytest` if not already installed:
   ```bash
   pip install pytest
   ```

2. Run the test suite:
   ```bash
   python3 -m unittest discover tests
   ```

The test files are located in the `tests` directory, with individual test files for each cipher implementation.



---
## How to Contribute

We welcome contributions to improve this project! Here’s how you can help:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and run Flake8 and tests to ensure quality.
4. Commit and push your changes.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

