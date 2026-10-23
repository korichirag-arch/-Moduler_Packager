# 🛠️ Multi-Utility Toolkit

A modular, menu-driven Python CLI application that consolidates essential system utilities, mathematical calculations, time management tools, random data generation, file handling, and dynamic module introspection into a single console interface.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Module Architecture](#-module-architecture)
- [Prerequisites & Dependencies](#-prerequisites--dependencies)
- [Installation & Setup](#-installation--setup)
- [Usage & Menu Walkthrough](#-usage--menu-walkthrough)
- [Error Handling & Edge Cases](#-error-handling--edge-cases)
- [Project Structure](#-project-structure)

---

## 📖 Overview

The **Multi-Utility Toolkit** serves as a complete console-based tool covering practical standard library operations in Python. Designed with a structured loop and modular functions, it enables users to perform everyday computational and file tasks without switching tools or writing one-off scripts.

---

## ✨ Key Features

### 1. 🕒 Datetime and Time Operations
- **System Clock:** Displays the current system timestamp (`YYYY-MM-DD HH:MM:SS`).
- **Date Difference Calculator:** Computes absolute days between any two dates in `YYYY-MM-DD` format.
- **Custom Date Formatter:** Formats timestamps using user-specified `strftime` directives (e.g., `%d-%m-%Y`, `%B %d, %Y`).
- **Stopwatch:** Tracks elapsed execution time using high-resolution epoch time (`time.time()`).
- **Countdown Timer:** Terminal-based countdown updating the same line in real-time using carriage return (`\r`).

### 2. 🧮 Mathematical Operations
- **Factorial:** Non-negative integer factorial calculation using `math.factorial()`.
- **Compound Interest Solver:** Computes accrued compound amount based on principal, annual rate, and duration ($A = P(1 + r/100)^t$).
- **Trigonometric Functions:** Calculates sine, cosine, and tangent values from degree inputs via radian conversion (`math.radians()`).
- **2D Geometry Calculator:** Computes area for Circles ($\pi r^2$), Rectangles ($l \times w$), and Triangles ($0.5 \times b \times h$).

### 3. 🎲 Random Data Generation
- **Bounded Numbers:** Generates random integers within an inclusive range $[min, max]$.
- **Random Lists:** Creates dynamic integer lists of custom size and range via list comprehension.
- **Strong Password Generator:** Compiles cryptographically diverse passwords using ASCII letters, digits, and special characters.
- **Secure OTPs:** Emits 6-digit verification codes (`100000` to `999999`).

### 4. 🔑 Unique Identifiers (UUID)
- Generates standard **UUIDv4** tokens using pseudorandom generation (`uuid.uuid4()`).

### 5. 📁 File Operations
- **File Creator:** Creates fresh files cleanly in the local working directory.
- **File Writer:** Overwrites or creates files with user input.
- **File Reader:** Inspects file contents with preliminary `os.path.exists()` verification.
- **Data Appender:** Appends new lines to existing text files without truncating prior content.

### 6. 🔍 Dynamic Module Introspection (`dir()`)
- Inspects built-in and external Python modules (e.g., `math`, `os`, `sys`, `pandas`, or custom modules) at runtime using `__import__()` and displays the available attributes and function signatures.

---

## 🏗️ Module Architecture

| Module | Built-in / Third-Party | Purpose in Project |
| :--- | :--- | :--- |
| `datetime` | Built-in | Parsing strings to dates (`strptime`) and formatting outputs (`strftime`) |
| `time` | Built-in | Timing stopwatch durations and throttling countdown loops (`sleep`) |
| `math` | Built-in | Factorials, power formulas, geometric constants ($\pi$), and trig functions |
| `random` | Built-in | Uniform integer generation and string character sampling |
| `string` | Built-in | Pre-built character sets (`ascii_letters`, `digits`, `punctuation`) |
| `uuid` | Built-in | Generating universally unique 128-bit identifiers |
| `os` | Built-in | Filesystem operations and file path existence verification |
| `sys` | Built-in | System-level attribute discovery |
| `pandas` | Third-Party | Prepared for tabular data workflows and dataset extensions |

---

## ⚙️ Prerequisites & Dependencies

- **Python:** Version `3.8` or newer installed.
- **External Packages:** `pandas` (required for script imports).

Install the required library via pip:

```bash
pip install pandas
