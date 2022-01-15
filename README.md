# avogadr-py

Simple avogadr.io batch downloader python script

## Installation

avogadr-py is avalaible through Python Package Index ([PyPI](https://pypi.python.org/pypi)) using [pip](https://pip.pypa.io):

```console
foo@bar:~$ python3 -m pip install --upgrade avogadr_py
```

To uninstall using [pip](https://pip.pypa.io):

```console
foo@bar:~$ python3 -m pip uninstall avogadr_py
```

## Command reference

```console
foo@bar:~$ avogadr-py -h
usage: avogadr-py [-h] [-i INPUT] [-o OUTPUT_FOLDER] [-b BACKGROUND] [-f FOREGROUND] [-W WIDTH] [-H HEIGHT] [-n]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        JSON formatted compound list. Defaults to 'compounds.json'.
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        Folder to output files to. Defaults to 'output/'.
  -b BACKGROUND, --background BACKGROUND
                        Background colour in HEX format. Defaults to '24283b'.
  -f FOREGROUND, --foreground FOREGROUND
                        Foreground colour in HEX format. Defaults to '7aa2f7'.
  -W WIDTH, --width WIDTH
                        Image width in pixels. Defaults to '1920'.
  -H HEIGHT, --height HEIGHT
                        Image height in pixels. Defaults to '1080'.
  -n, --no-include-name
                        Don't include compound names. Defaults to 'False'.
```

## Example

```console
foo@bar:~$ avogadr-py -i compounds.json -W 3840 -H 2160 -o output/2160p/blue -f 7aa2f7
```

## Development

Source code repository is available on [GitHub](https://github.com/Czechbol/avogadr-py). Feel free to contribute. [Bug reports](https://github.com/Czechbol/avogadr-py/issues) and suggestions are welcome.

## License

avogadr-py is licensed under the [MIT License](https://github.com/Czechbol/avogadr-py/blob/main/LICENSE).

## Acknowledgement

- I would like to thank [Saul Johnson](https://github.com/lambdacasserole)
  for the amazing [avogadr.io](https://avogadr.io) website that is used as basis for this script.
