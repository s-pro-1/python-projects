from pathlib import Path
import os
import shutil

# Get the current user's Downloads folder
downloads = Path.home() / "Downloads"

# Map file extensions to their destination folders
extension_map = {
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "pdf": "Documents",
    "txt": "Documents",
    "docx": "Documents",
    "mp3": "Musics",
    "wav": "Musics",
    "mp4": "Videos",
    "zip": "Archives"
}

# Get every item inside the Downloads folder
files = os.listdir(downloads)

# Process one item at a time
for file in files:

    # Create the full path to the current item
    source = downloads / file

    # Skip folders because we only want to organize files
    if not source.is_file():
        continue

    # Get the file extension (example: "photo.PNG" -> "png")
    extension = file.split(".")[-1].lower()

    # Find the destination folder using the extension
    folder = extension_map.get(extension)

    # Skip files with unsupported or unknown extensions
    if folder is None:
        print(f"Skipping: {file}")
        continue

    # Build the destination folder path
    destination = downloads / folder

    # Create the destination folder if it doesn't already exist
    if not destination.exists():
        destination.mkdir()

    # Move the file into its destination folder
    shutil.move(source, destination)