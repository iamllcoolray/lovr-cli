import argparse
from commands import new, run, build, get

__version__ = "0.1"

__description__ = "Lovr is a command line interface that manages LÖVE2D projects"

# Create the parser
parser = argparse.ArgumentParser(description=__description__)

# Add arguments
parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}', help="show the current version of lovr")
parser.add_argument('-n', '--new', type=str, help="initializes a new LÖVE2D project")
parser.add_argument('-r', '--run', action='store_true', help="runs the LÖVE2D project")
parser.add_argument('-b', '--build', action='store_true', help="builds the LÖVE2D project into the builds directory")
parser.add_argument('-g', '--get', type=str, help="gets and stores third-party libraries in the lib directory")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.new:
    new_project = new.New(args.new);
    new_project.new_project()
    
if args.run:
    pass

if args.build:
    pass

if args.get:
    pass