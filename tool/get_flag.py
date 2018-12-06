
import subprocess
from io import StringIO
from os import path


def get_flag(image, cmd_name, fname, fpath, from_stdout=True):
    cmd = "docker run --rm %s %s --help" % (image, cmd_name)
    ffname = path.join(fpath, fname)
    cc = subprocess.run(
        cmd, shell=True,  stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
    if from_stdout:
        kkk = StringIO(cc.stdout.decode('utf-8'))
    else:
        kkk = StringIO(cc.stderr.decode('utf-8'))
    output = False
    with open(ffname, "w") as ff:
        for line in kkk:
            if output:
                ff.write(line)
            elif line.startswith("Available Flags") or line.startswith("Flags") or line.startswith("Generic flags"):
                output = True


if __name__ == '__main__':

    ND = {
        "apiserver.flag": "/apiserver",
        "controller-manager.flag": "/controller-manager",
        "scheduler.flag": "/scheduler",
        "kubelet.flag": "/kubelet",
        "kube-proxy.flag": "/proxy",
    }

    image = "gcr.io/google-containers/hyperkube:v1.12.3"
    fpath = "./tmp/origin"
    for fname, cmd_name in ND.items():
        print(fname)
        get_flag(image, cmd_name, fname, fpath)

