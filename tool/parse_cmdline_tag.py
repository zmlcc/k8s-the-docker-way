
from collections import defaultdict

import re

SPEC_NAME = ["feature-gates", "controllers"]
class Flag(object):
    def __init__(self, name, typ=None, explanation=None):
        self.name = name
        self.typ = typ
        self.explanation = explanation
        self.ext = ""
        self.tag = None

def parse(ss, first_gap, second_gap):
    flags = []
    with  open(ss) as ff:
        for line in ff:
            prefix = line[:first_gap]
            if prefix in ["      --",  "  -v, --", "  -h, --"]:
                explanation = line[second_gap:].strip()
                keyline = line[first_gap:second_gap].strip().split()
                if len(keyline) == 1:
                    flags.append(Flag(keyline[0],  None, explanation))
                elif len(keyline) >= 2:
                    flags.append(Flag(keyline[0],  ' '.join(keyline[1:]), explanation))
                else:
                    print(line)
                    print(keyline)
                    raise SyntaxError
            elif len(flags) > 0 and flags[-1].name in SPEC_NAME:
                flags[-1].ext += line
            else:
                print(line)
                raise SyntaxError

    return flags

def get_flag_map(ss):
    # flags = []
    cur_tag = None
    flag_map = dict()
    with open(ss) as ff:
        for line in ff:
            if line[0] == '-':
                keyline = line[1:].strip().split()
                flag_map[keyline[0]] = cur_tag
            elif line[:3] == "###":
                cur_tag = line[3:].strip()

    return flag_map



def process(old_md, new_md, new_flagf, flag_gap, title=None):

    flags = parse(new_flagf, flag_gap[0], flag_gap[1])

    flag_map = get_flag_map(old_md)

    ## merge tag
    for flag in flags:
        flag.tag = flag_map.get(flag.name, "uncategorized")

    tag_map = defaultdict(list)
    for item in flags:
        tag_map[item.tag].append(item)

    if "uncategorized" in tag_map:
        print("--->>>  Has Uncategorized Tag: ", ' '.join(item.name for item in tag_map["uncategorized"]))
        

    ## write new_md file
    with open(new_md, "w") as ff:
        if title is None:
            ff.write("A detailed description of the command-line flag\n\n")
        else:
            ff.write(title)
            ff.write("\n\n")

        for tag in sorted(tag_map):
            ff.write("\n\n### %s\n\n"%tag)
            for flag in tag_map[tag]:
                if flag.typ is None:
                    ff.write("- %s\n\n"%(flag.name))
                else:                    
                    ff.write("- %s %s\n\n"%(flag.name, flag.typ))
                ff.write("    %s\n"%flag.explanation)
                if flag.ext != "":
                    ff.write("```\n")
                    ff.write(flag.ext)
                    ff.write("```\n")
                ff.write("\n")
                

def find_gap(fname):
    p1 = re.compile("--")
    p2 = re.compile("  \S")
    with open(fname) as ff:
        line = ff.read()
        return p1.search(line).end(), p2.search(line, 10).end()-1


if __name__ == '__main__':

    NL = ["apiserver", "controller-manager", "scheduler", "kubelet", "kube-proxy"]

    for name in NL:
        old_md = "./tmp/v1.10.0.a/%s.md"%(name)
        new_md = "./tmp/v1.10.0/%s.md"%(name)
        flagf = "./tmp/origin/%s.flag"%(name)
        title = "A detailed description of the command-line flag of %s"%(name)
        gap = find_gap(flagf)
        print(name, gap)
        process(old_md, new_md, flagf, gap, title)