# Git Easy Changelog

This project helps at managing yours REALEASE/CHANGELOG `.md` files, avoiding git conflicts as it use one file per
change reported in the final release file.

**Up to the moment**, this is **_not_** a python package.

## Usage
### Basic Usage

1. Download the repository content, and extract it at a new `CHANGELOG` folder.
1. Remove the `example` folder.
1. Create a folder for the next version.
1. Add a new `.md` single line file for each change that should be reported.
1. Run `summarise.py`
1. Go back to step 3.

### Advanced options

* You can change previous version files, up to error, reference of newest changes or anything you want.
* You can add a `date.md` file in any version file, which will be add as release date reference.

#### Example

You can test the project in `example` branch, by simple running `summarise.py`