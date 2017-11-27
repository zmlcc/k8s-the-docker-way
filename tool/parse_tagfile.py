
class Flag(object):
    def __init__(self, name, typ=None, explanation=None):
        self.name = name
        self.typ = typ
        self.explanation = explanation
        self.ext = ""
        self.tag = None

def parse(ss):
    flags = []
    cur_tag = None
    cur_flag = None
    with open(ss) as ff:
        for line in ff:
            if line[0] = '-':
                keyline = line[1:].strip().split()
                cur_flag = Flag(keyline[0], None)
                cur_flag.tag = cur_tag
            elif line[:3] = "###":
                cur_tag = line[3:].strip()
            else:
                pass

    return flags