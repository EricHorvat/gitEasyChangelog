# -*- coding: utf-8 -*-

"""Main module."""
import os
import packaging.version

LEVEL = "black"


def match(elem):
    try:
        ans = packaging.version.Version(elem)
    except packaging.version.InvalidVersion as e:
        # TODO print folder/file ommited
        return False
    return ans


IGNORED_FILES = ["date.md"]


def addFile(filename, changelog_file):
    with open(filename, "r") as file:
        lines = file.readlines()
        changelog_file.writelines(lines[:-1])
        changelog_file.write(lines[-1].rstrip("\n"))


def main(args=None):

    ls_ans = os.listdir(".")
    folders = list(sorted(filter(lambda el: el, map(lambda elem: match(elem),ls_ans)),reverse=True))
    with open("RELEASE.md","w") as changelog_file:
        if "header.md" in ls_ans:
            with open("header.md", "r") as header_file:
                changelog_file.writelines(header_file.readlines())
                changelog_file.writelines("\n")
        for folder in folders:
            changelog_file.write(str(folder))
            inner_files = list(sorted(filter(lambda elem: elem.endswith(".md") ,os.listdir("./" + str(folder)))))
            if "date.md" in inner_files:
                changelog_file.write(" [")
                addFile("./" + str(folder) + "/date.md",changelog_file)
                changelog_file.write("]")
            changelog_file.writelines(":\n---\n")

            previous = [""]

            for inner_file_name in inner_files:
                if inner_file_name not in IGNORED_FILES:
                    changelog_file.write(" * ")
                    addFile("./" + str(folder) + "/" + inner_file_name, changelog_file)
                    changelog_file.write("\n")
            changelog_file.writelines("\n")

        if "footer.md" in ls_ans:
            with open("footer.md", "r") as footer_file:
                changelog_file.writelines(footer_file.readlines())
