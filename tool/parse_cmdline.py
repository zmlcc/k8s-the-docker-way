
FIRST_GAP = 8
SECOND_GAP = 64
SPEC_NAME = ["feature-gates", "controllers"]

class Flag(object):
    def __init__(self, name, typ, explanation):
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

if __name__ == '__main__':
    fname = "./tmp-cm"
    flags = parse(fname)
    for item in flags:
        print(item.name, item.typ)
