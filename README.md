# LOVR

lovr is a command line interface that initializes, manages, runs, builds LÖVE2D projects.

## Getting Started

Make sure you have the latest version of [LÖVE2D]("https://love2d.org/") installed.

### Installation

#### MACOSX

    brew install lovr

### Initialize with Project Name

    lovr --new [new-löve2d-project-name]

### Run Project

    lovr --run

### Build Project

    lovr --build

## Commands

### version

Displays the current version of lovr.

### help

Displays all the commands and their descriptions.

### new

Initializes a new LÖVE2D project.

#### Project Structure

    my-löve2d-project/
    ├── assets/         # Asset files
    │   ├── audio/      # Audio files
    │   ├── maps/       # Map/Level files
    │   └── sprites/    # Sprite files
    ├── lib/            # Library files
    ├── src/            # Source files
    ├── conf.lua        # LÖVE2D configuration file
    └── main.lua        # Main file

### run

Runs the LÖVE2D project.

### build

Builds the LÖVE2D project.

#### Project Structure

    my-löve2d-project/
    ├── build/          # Build files and executables
    ├── assets/         # Asset files
    │   ├── audio/      # Audio files
    │   ├── maps/       # Map/Level files
    │   └── sprites/    # Sprite files
    ├── lib/            # Library files
    ├── src/            # Source files
    ├── conf.lua        # LÖVE2D configuration file
    └── main.lua        # Main file

### get

Gets and adds third-party libraries in lib.
