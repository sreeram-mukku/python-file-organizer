# 📂 File Organizer and Standardizer Script

A powerful, command-line Python utility designed to enforce naming consistency and automatically organize files within a specified directory.

The script performs two primary functions:
1.  **Standardizes File Names:** Converts complex file names into a clean, lowercased, and underscore-separated format.
2.  **Organizes Files:** Optionally moves files into subdirectories based on their file extension.

| Original File Name | Renamed File Name |
| :--- | :--- |
| `9.8 Iterators.pdf` | `9_8_iterators.pdf` |
| `My Awesome Project - V2.0.zip` | `my_awesome_project_v2_0.zip` |
| `Document (Final) [2024].docx` | `document_final_2024.docx` |

## ✨ Features

* **Clean Naming:** Replaces spaces, hyphens, and most punctuation with **underscores (`_`)**.
* **Case Conversion:** Converts all file names to **lowercase**.
* **Directory Traversal:** Processes all files in the target directory (non-recursive).
* **Optional Organization:** Can sort files into folders named after their file extension (e.g., all `.pdf` files go into a `pdf` folder).

---

## 🐍 Modules Used (Standard Library)

This project relies exclusively on the **Python Standard Library**, meaning no external installation is necessary. 

| Module | Purpose in this Script |
| :--- | :--- |
| **`os`** | Core module for interacting with the operating system, used for tasks like **getting file paths** (`os.path.join`), **checking if a path is a directory** (`os.path.isdir`), and **renaming files** (`os.rename`). |
| **`shutil`** | Provides high-level file operations, used specifically for **moving files** between directories (`shutil.move`) during the organization phase. |
| **`argparse`** | Used for **parsing command-line arguments**, allowing the user to specify the target directory and use flags like `--organize`. |
| **`re`** | The **regular expression** module, used within the standardization logic to efficiently **find and replace** various special characters and spaces with a single underscore. |

---

## 🚀 Installation

This script uses only Python's standard library modules.

1.  **Ensure Python is installed:** You must have **Python 3** installed on your system.
    ```bash
    python3 --version
    ```
2.  **Save the script:** Save the Python code as a file named `file_organizer.py` in a convenient location.

---

## 💻 Usage

Run the script from your command line, passing the directory you want to process as the first argument.

### 1. Standardize Naming Only

Use this command to **only rename** the files for consistency.

```bash
python3 file_organizer.py <target_directory>
```
### 2. Standardize and Organize (Moving)
Use the optional --organize flag to not only rename but also **move** the files into subdirectories created within the target directory, based on their extension.

```bash
python3 file_organizer.py <target_directory> --organize
```
