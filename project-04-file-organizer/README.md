# Project 04 - File Organizer

A Python program that automatically organizes files in the Downloads folder into categorized folders.

## Features

- Organizes files by extension
- Creates folders automatically
- Supports:
  - Images
  - Documents
  - Musics
  - Videos
  - Archives
- Skips unsupported file types
- Skips folders
- Skips files without extensions
- Prevents overwriting duplicate files by renaming them

## Technologies Used

- Python
- pathlib
- shutil

## Project Structure

```
project-04-file-organizer/
│
├── README.md
└── index.py
```

## Example

Before:

```
Downloads/
│
├── photo.png
├── song.mp3
├── report.pdf
├── movie.mp4
└── archive.zip
```

After:

```
Downloads/
│
├── Images/
│   └── photo.png
│
├── Musics/
│   └── song.mp3
│
├── Documents/
│   └── report.pdf
│
├── Videos/
│   └── movie.mp4
│
└── Archives/
    └── archive.zip
```

## What I Learned

- pathlib
- Working with file paths
- shutil.move()
- File extensions
- Dictionaries
- Creating folders automatically
- Handling duplicate filenames
- Writing reusable functions
- Basic file automation

## Author

Sofi Zeleke