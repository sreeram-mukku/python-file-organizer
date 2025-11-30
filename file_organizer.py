import os
import shutil
import argparse
import re

def setup_cli_parser():
    """Sets up the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="A Python script to rename and organize files recursively in a directory.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Required argument: the target directory
    parser.add_argument(
        'target_directory',
        type=str,
        help='The root directory to traverse and organize.'
    )

    # Optional flag: to enable the organization (moving into folders) feature
    parser.add_argument(
        '-o', '--organize',
        action='store_true',
        help='If set, files will be moved into subdirectories based on their extension (e.g., .jpg into Images).'
    )

    return parser.parse_args()

def standardize_filename(filename):
    """
    Standardizes a filename by converting it to lowercase,
    replacing spaces/dots/dashes with a single underscore, and stripping extra chars.
    """
    # 1. Convert to lowercase
    name = filename.lower()
    
    # 2. Replace common separators (spaces, dots, hyphens) with a single underscore
    # This regex is powerful: it matches one or more occurrences of space, dot, or hyphen.
    name = re.sub(r'[\s.-]+', '_', name)
    
    # 3. Strip any leading or trailing underscores
    name = name.strip('_')
    
    # Optional: You might want to remove non-alphanumeric characters, but for a general renamer, 
    # leaving some special characters (like parentheses) that people use in file names is often best.

    return name

def process_directory(root_dir, should_organize):
    """
    Recursively traverses the directory, renames files, and optionally organizes them.
    """
    print(f"Starting process in: **{os.path.abspath(root_dir)}**")
    
    # os.walk yields a 3-tuple: (current_dir_path, dir_names_in_current, file_names_in_current)
    for folderpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            original_path = os.path.join(folderpath, filename)
            
            # Skip directories and special files like .DS_Store (mostly for Mac, but good practice)
            if os.path.isdir(original_path) or filename.startswith('.'):
                continue
            
            # --- RENAME LOGIC ---
            
            # 1. Separate the file name and extension
            name_part, extension = os.path.splitext(filename)
            
            # 2. Get the new standardized name part
            standardized_name = standardize_filename(name_part)
            new_filename = standardized_name + extension
            new_path = os.path.join(folderpath, new_filename)
            
            # Only rename if a change was actually made
            if filename != new_filename:
                try:
                    os.rename(original_path, new_path)
                    print(f"   RENAMED: '{filename}' -> '{new_filename}'")
                    # Update original_path and filename for the organization step
                    original_path = new_path
                    filename = new_filename
                except OSError as e:
                    print(f"   ERROR renaming {filename}: {e}")
            
            # --- ORGANIZATION LOGIC ---
            
            if should_organize:
                # Get the extension without the dot, and capitalize it for the folder name
                extension_clean = extension.lstrip('.').upper()
                
                # Simple mapping for common file types (optional, but nice)
                if extension_clean in ['JPG', 'JPEG', 'PNG', 'GIF']:
                    folder_name = 'Images'
                elif extension_clean in ['MP4', 'MOV', 'AVI']:
                    folder_name = 'Videos'
                elif extension_clean in ['DOCX', 'PDF', 'TXT']:
                    folder_name = 'Documents'
                elif extension_clean:
                    # Fallback: use the capitalized extension as the folder name
                    folder_name = extension_clean + ' Files' 
                else:
                    # File has no extension (e.g., a script or config file)
                    folder_name = 'Uncategorized'

                # Define the target directory for the organized file
                target_dir = os.path.join(root_dir, folder_name)
                
                # Create the target directory if it doesn't exist
                os.makedirs(target_dir, exist_ok=True)
                
                # Define the final destination path
                destination_path = os.path.join(target_dir, filename)

                # Move the file
                # Use shutil.move for robustness (it handles cross-device moves if necessary)
                if folderpath != target_dir: # Only move if it's not already in the target folder
                    try:
                        shutil.move(original_path, destination_path)
                        print(f"   MOVED: '{filename}' to folder '{folder_name}'")
                    except shutil.Error as e:
                         print(f"   ERROR moving {filename}: {e}")

def main():
    """Main function to parse arguments and run the file processing."""
    args = setup_cli_parser()
    
    # Get the absolute path and ensure it's a valid directory
    target_dir = os.path.abspath(args.target_directory)
    
    if not os.path.isdir(target_dir):
        print(f"Error: The provided path '{target_dir}' is not a valid directory.")
        exit(1)
        
    process_directory(target_dir, args.organize)
    print("\nProcessing complete!")

if __name__ == "__main__":
    main()