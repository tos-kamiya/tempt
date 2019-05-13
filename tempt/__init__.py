#!/usr/bin/env python3

import os
import os.path as path
import shutil
import sys


def get_config_home():
    if 'APPDATA' in os.environ:
        confighome = os.environ['APPDATA']
    elif 'XDG_CONFIG_HOME' in os.environ:
        confighome = os.environ['XDG_CONFIG_HOME']
    else:
        confighome = path.join(os.environ['HOME'], '.config')
    
    return confighome


__doc__ = """Template touch: Create a copy of a template file having the specified extension.

Usage: %s <filename>
""" % path.basename(sys.argv[0])


def main():
    config_home = get_config_home()
    config_path = path.join(config_home, path.basename(sys.argv[0]))
    if not path.isdir(config_path):
        os.mkdir(config_path)
    
    template_dir = path.join(config_path, "templates")
    if not path.isdir(template_dir):
        os.mkdir(template_dir)
    
    template_files = os.listdir(template_dir)
    template_files.sort()

    args = sys.argv[1:]
    while args:
        a = args[0]
        if a == '-h':
            print(__doc__)
            sys.exit()
        else:
            break  # while args
        args.pop(0)

    for dest_file in args:
        p, ext = path.splitext(dest_file)
        for tf in template_files:
            p, t_ext = path.splitext(tf)
            if t_ext == ext:
                shutil.copyfile(path.join(template_dir, tf), dest_file)
                break  # for tf
        else:
            sys.exit("error: no such template file (*%s) in %s" % (ext, template_dir))


if __name__ == '__main__':
    main()
