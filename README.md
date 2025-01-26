# Python Learning Challenge: Day 1

## Overview
Welcome to Day 1 of our **30-Day Python Learning Challenge**! This challenge is designed to help you master Python step by step by building projects and understanding core concepts.

Today's goal is to:
- Learn Python basics (variables, data types, input/output).
- Get started with Docker by containerizing a simple Python project.

This README provides an overview of what we've accomplished on Day 1, including the project we built and key takeaways.

---

## Day 1: Python Basics and Docker Setup

### Objectives
1. **Understand Python Basics:**
   - Variables and data types.
   - Input/output operations.
   - Writing and executing a Python script.

2. **Introduction to Docker:**
   - What is Docker and why it's useful.
   - How to create and use a Dockerfile to containerize a Python project.

---

## Project: Python Calculator
### Description
We created a simple Python calculator that:
- Prompts the user to enter two numbers.
- Asks the user to choose a mathematical operation (addition, subtraction, multiplication, or division).
- Performs the operation and prints the result.

The project was then containerized using Docker to ensure it runs consistently across environments.



### Docker Setup
To containerize the calculator, we created a `Dockerfile`:
```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY calculator.py .

# Command to run the Python script
CMD ["python", "calculator.py"]
```

### Docker Commands
1. **Build the Docker Image:**
   ```bash
   docker build -t python-calculator .
   ```
2. **Run the Docker Container:**
   ```bash
   docker run -it python-calculator
   ```

---

## Key Learnings
- **Python Basics:**
  - Variables, data types, and basic input/output operations.
  - Writing and running Python scripts.

- **Docker Basics:**
  - How to use Docker to containerize a project.
  - Key Docker commands (`docker build`, `docker run`, etc.).

---
