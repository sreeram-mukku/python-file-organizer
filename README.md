# 📂 File Organizer and Standardizer Script

A powerful, command-line Python utility designed to enforce naming consistency and automatically organize files within a specified directory.

The script performs two primary functions:
1.  **Standardizes File Names:** Converts complex file names into a clean, lowercased, and underscore-separated format.
2.  **Organizes Files:** Optionally moves files into subdirectories based on their file extension.

## ✨ Features

* **Clean Naming:** Replaces spaces, hyphens, and most punctuation with **underscores (`_`)**.
* **Case Conversion:** Converts all file names to **lowercase**.
* **Directory Traversal:** Processes all files in the target directory (non-recursive).
* **Optional Organization:** Can sort files into folders named after their file extension (e.g., all `.pdf` files go into a `pdf` folder).

***

## 🚀 Installation

This script uses only Python's standard library modules, such as `os` and `sys`. No external packages are required.

1.  **Ensure Python is installed:** You must have **Python 3** installed on your system.
    ```bash
    python3 --version
    ```
2.  **Save the script:** Save the Python code as a file named `file_organizer.py` in a convenient location.

***

## 💻 Usage

Run the script from your command line, passing the directory you want to process as the first argument.

### 1. Standardize Naming Only

Use this command to **only rename** the files for consistency.

```bash
python3 file_organizer.py <target_directory>

<img width="1417" height="1079" alt="Screenshot from 2025-12-01 01-09-57" src="https://github.com/user-attachments/assets/be35f124-4b42-4580-aed2-22bb6c05f8cd" />

<img width="1437" height="1334" alt="Screenshot from 2025-12-01 01-10-32" src="https://github.com/user-attachments/assets/6949b268-bd3d-438d-87a4-5fcdf5ef370f" />



