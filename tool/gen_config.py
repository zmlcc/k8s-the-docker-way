import subprocess
from os import path


def gen_config(image, cmd_name, fname, fpath, from_stdout=True):
    ffpath = path.abspath(fpath)
    cmd = "docker run --rm -v %s:/aaa  %s %s --write-config-to /aaa/%s" % (
        ffpath, image, cmd_name, fname)
    print(cmd)
    subprocess.run(cmd, shell=True)


if __name__ == '__main__':

    ND = {
        "scheduler.cfg": "/hyperkube kube-scheduler",
        "kube-proxy.cfg": "/hyperkube kube-proxy",
    }

    image = "gcr.io/google-containers/hyperkube-amd64:v1.15.5"
    fpath = "./tmp/origin"
    for fname, cmd_name in ND.items():
        print(fname)
        gen_config(image, cmd_name, fname, fpath)
