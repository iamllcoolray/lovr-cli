# LOVR

lovr is a command line interface that manages LÖVE2D projects.

## Getting Started

Make sure you have the latest version of [LÖVE2D]("https://love2d.org/") installed.

### Installation

#### MACOSX

    brew install lovr (Not yet available)

### Initialize with Project Name

    lovr --new [new-löve2d-project-name]

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

#### Project Structure

    my-löve2d-project/
    ├── build/          # Build files and executables
    ├── assets/         # Asset files
    │   ├── audio/      # Audio files
    │   ├── maps/       # Map/Level files
    │   └── sprites/    # Sprite files
    ├── lib/            # Library files
    │   ├── love-lib/   # Third-Party LÖVE2D Library
    ├── src/            # Source files
    ├── conf.lua        # LÖVE2D configuration file
    └── main.lua        # Main file
