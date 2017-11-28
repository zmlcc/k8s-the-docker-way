
from collections import defaultdict


FIRST_GAP = 8
SECOND_GAP = 53
SPEC_NAME = ["feature-gates", "controllers"]
class Flag(object):
    def __init__(self, name, typ=None, explanation=None):
        self.name = name
        self.typ = typ
        self.explanation = explanation
        self.ext = ""
        self.tag = None

def parse(ss):
    flags = []
    with  open(ss) as ff:
        for line in ff:
            prefix = line[:FIRST_GAP]
            if prefix in ["      --",  "  -v, --", "  -h, --"]:
                explanation = line[SECOND_GAP:].strip()
                keyline = line[FIRST_GAP:SECOND_GAP].strip().split()
                if len(keyline) == 2:
                    flags.append(Flag(keyline[0],  keyline[1], explanation))
                elif len(keyline) == 1:
                    flags.append(Flag(keyline[0],  None, explanation))
                else:
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
                # flags.append(Flag(keyline[0], cur_tag))
                flag_map[keyline[0]] = cur_tag
            elif line[:3] == "###":
                cur_tag = line[3:].strip()

    return flag_map



def process(old_md, new_md, new_flagf, title=None):

    flags = parse(new_flagf)

    flag_map = get_flag_map(old_md)

    ## merge tag
    for flag in flags:
        flag.tag = flag_map.get(flag.name, "uncategorized")

    tag_map = defaultdict(list)
    for item in flags:
        tag_map[item.tag].append(item)


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

if __name__ == '__main__':
    FIRST_GAP = 8
    SECOND_GAP = 53
    old_md = "./tmp/origin/kube-proxy.md"
    new_md = "./tmp/v1.8.4/kube-proxy.md"
    flagf = "./tmp/origin/kube-proxy.flag"
    title = "A detailed description of the command-line flag of kube-proxy"
    process(old_md, new_md, flagf, title)