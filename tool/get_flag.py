import subprocess
from io import StringIO
from os import path


def get_flag(image, cmd_name, fname, fpath, from_stdout=True):
    cmd = "docker run --rm %s %s --help" % (image, cmd_name)
    ffname = path.join(fpath, fname)
    cc = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if from_stdout:
        kkk = StringIO(cc.stdout.decode('utf-8'))
    else:
        kkk = StringIO(cc.stderr.decode('utf-8'))
    output = False
    with open(ffname, "w") as ff:
        for line in kkk:
            if output:
                ff.write(line)
            elif line.startswith("Available Flags") or line.startswith(
                    "Flags") or line.startswith(
                        "Generic flags") or line.strip().endswith("flags:"):
                output = True
                ff.write(line)


if __name__ == '__main__':

    ND = {
        "apiserver.flag": "/hyperkube kube-apiserver",
        "controller-manager.flag": "/hyperkube kube-controller-manager",
        "scheduler.flag": "/hyperkube kube-scheduler",
        "kubelet.flag": "/hyperkube kubelet",
        "kube-proxy.flag": "/hyperkube kube-proxy",
    }

    image = "gcr.io/google-containers/hyperkube-amd64:v1.15.5"
    fpath = "./tmp/origin"
    for fname, cmd_name in ND.items():
        print(fname)
        get_flag(image, cmd_name, fname, fpath)
