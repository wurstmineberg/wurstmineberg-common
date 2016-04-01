
import argparse
import os
import pathlib
import json


DEFAULT_CONFIG_DIR = "/opt/wurstmineberg/config/"

CONFIG_DIR = pathlib.Path(os.getenv("WURSTMINEBERG_CONFIG_DIR",
                                    default = DEFAULT_CONFIG_DIR))


_COPY_PROMPT = """The file

{file}

does not exist, create it? [yN]"""


def _from_file(configfile):
    with configfile:
        return json.load(configfile)


def _get_base_config(name, base):
    if base is None:
        return {}

    # from_assets uses "{name}" as a placeholder
    base = base.with_name(base.name.format(name = name))
    return _from_file(base.open("r"))


def _get_passed_configfile():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type = argparse.FileType("r"))
    (args, _) = parser.parse_known_args()
    return args.config


def _prompt_copy_config(name, e):
    import sys
    if not sys.__stdin__.isatty():
        return False
    response = input(_COPY_PROMPT.format(file = e.filename))
    if response.lower() == "y":
        with _get_configfile(name, mode = "w") as configfile:
            json.dump({}, configfile)
        return True
    return False


def _get_configfile(name, mode = "r"):
    try:
        return (CONFIG_DIR / "{}.json".format(name)).open(mode)
    except FileNotFoundError as e:
        print(e)
        if _prompt_copy_config(name, e):
            return _get_configfile(name)
        else:
            raise


def get_config(name, base = None, argparse_configfile = True):
    config = _get_base_config(name, base)

    passed_configfile = None
    if argparse_configfile:
        passed_configfile = _get_passed_configfile()

    if passed_configfile is None:
        configfile = _get_configfile(name)
    else:
        configfile = passed_configfile

    config.update(_from_file(configfile))
    return config


def from_assets(script_file):
    script_dir = pathlib.Path(script_file).resolve().parent
    return script_dir / "assets" / "{name}.default.json"


if __name__ == "__main__":
    print(get_config("example"))
    print(get_config("example", base = from_assets(__file__), argparse_configfile = False))
    

