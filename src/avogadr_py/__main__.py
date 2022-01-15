import argparse
import asyncio
import json
import os

import aiofiles
import aiohttp


def load_input(input: str) -> dict:
    with open(input) as json_file:
        data = json.loads(json_file.read())
    return data


async def download(
    compounds: dict,
    output_folder: str,
    bg_colour: str,
    fg_colour: str,
    width: str,
    height: str,
    dont_include_name: bool,
):
    if not output_folder.endswith("/"):
        output_folder += "/"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if bg_colour.startswith("#"):
        bg_colour = bg_colour.lstrip("#")
    if fg_colour.startswith("#"):
        fg_colour = fg_colour.lstrip("#")

    for compound in compounds:
        avogadr_link = (
            f"https://avogadr.io/api/name/{width}/{height}/{bg_colour}/{fg_colour}/{compound['compound']}"
        )
        if not dont_include_name:
            avogadr_link += f"?label={compound['compound']}&"

        async with aiohttp.ClientSession() as session:
            async with session.get(avogadr_link) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"{output_folder}/{compound['filename']}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()


async def main():
    parser = argparse.ArgumentParser(
        prog="avogadr-py",
        allow_abbrev=False,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-i",
        "--input",
        default="compounds.json",
        type=str,
        help="JSON formatted compound list. Defaults to 'compounds.json'.",
    )
    parser.add_argument(
        "-o",
        "--output-folder",
        default="output/",
        type=str,
        help="Folder to output files to. Defaults to 'output/'.",
    )
    parser.add_argument(
        "-b",
        "--background",
        default="24283b",
        type=str,
        help="Background colour in HEX format. Defaults to '24283b'.",
    )
    parser.add_argument(
        "-f",
        "--foreground",
        default="7aa2f7",
        type=str,
        help="Foreground colour in HEX format. Defaults to '7aa2f7'.",
    )
    parser.add_argument(
        "-W",
        "--width",
        default="1920",
        type=int,
        help="Image width in pixels. Defaults to '1920'.",
    )
    parser.add_argument(
        "-H",
        "--height",
        default="1080",
        type=int,
        help="Image height in pixels. Defaults to '1080'.",
    )
    parser.add_argument(
        "-n",
        "--no-include-name",
        action="store_true",
        default=False,
        help="Don't include compound names. Defaults to 'False'.",
    )
    args = parser.parse_args()

    compounds = load_input(args.input)

    await download(
        compounds,
        args.output_folder,
        args.background,
        args.foreground,
        args.width,
        args.height,
        args.no_include_name,
    )


def cli():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
