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
        "scheduler.cfg": "/scheduler",
        "kube-proxy.cfg": "/proxy",
    }

    image = "gcr.io/google-containers/hyperkube:v1.12.3"
    fpath = "./tmp/origin"
    for fname, cmd_name in ND.items():
        print(fname)
        gen_config(image, cmd_name, fname, fpath)
