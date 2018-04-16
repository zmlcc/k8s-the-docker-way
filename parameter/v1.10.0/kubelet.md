A detailed description of the command-line flag of kubelet




### container
- container-runtime string

    The container runtime to use. Possible values: 'docker', 'remote', 'rkt (deprecated)'. (default "docker")

- runtime-cgroups string

    Optional absolute name of cgroups to create and run the runtime in.

- pod-infra-container-image string

    The image whose network/ipc namespaces containers in each pod will use. (default "k8s.gcr.io/pause-amd64:3.1")


- docker-endpoint string

    Use this for the docker endpoint to communicate with (default "unix:///var/run/docker.sock")

- image-pull-progress-deadline duration

    If no pulling progress is made before this deadline, the image pulling will be cancelled. (default 1m0s)



### experimental
- experimental-mounter-path string

    [Experimental] Path of mounter binary. Leave empty to use the default mount.




- container-runtime-endpoint string

    [Experimental] The endpoint of remote runtime service. Currently unix socket is supported on Linux, and tcp is supported on windows.  Examples:'unix:///var/run/dockershim.sock', 'tcp://localhost:3735' (default "unix:///var/run/dockershim.sock")


- image-service-endpoint string

    [Experimental] The endpoint of remote image service. If not specified, it will be the same with container-runtime-endpoint by default. Currently unix socket is supported on Linux, and tcp is supported on windows.  Examples:'unix:///var/run/dockershim.sock', 'tcp://localhost:3735'

- experimental-check-node-capabilities-before-mount

    [Experimental] if set true, the kubelet will check the underlying node for required components (binaries, etc.) before performing the mount

- experimental-allocatable-ignore-eviction

    When set to 'true', Hard Eviction Thresholds will be ignored while calculating Node Allocatable. See https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/ for more details. [default=false]

- experimental-qos-reserved mapStringString

    A set of ResourceName=Percentage (e.g. memory=50%) pairs that describe how pod resource requests are reserved at the QoS level. Currently only memory is supported. [default=none]



### serving

- enable-server

    Enable the Kubelet's server (default true)

- runonce

    If true, exit after spawning pods from static pod files or remote urls. Exclusive with --enable-server


### node

- hostname-override string

    If non-empty, will use this string as identification instead of the actual hostname.

- node-ip string

    IP address of the node. If set, kubelet will use this IP address for the node

- node-labels mapStringString

    <Warning: Alpha feature> Labels to add when registering the node in the cluster.  Labels must be key=value pairs separated by ','.

- register-node

    Register the node with the apiserver. If --kubeconfig is not provided, this flag is irrelevant, as the Kubelet won't have an apiserver to register with. Default=true. (default true)

- register-with-taints []api.Taint

    Register the node with the given list of taints (comma separated "<key>=<value>:<effect>"). No-op if register-node is false.



### cloud

- azure-container-registry-config string

    Path to the file containing Azure container registry configuration information.

- cloud-config string

    The path to the cloud provider configuration file.  Empty string for no configuration file.

- cloud-provider string

    The provider for cloud services. Specify empty string for running with no cloud provider.

- provider-id string

    Unique identifier for identifying the node in a machine database, i.e cloudprovider



### config

- bootstrap-checkpoint-path string

    <Warning: Alpha feature> Path to to the directory where the checkpoints are stored

- bootstrap-kubeconfig string

    Path to a kubeconfig file that will be used to get client certificate for kubelet. If the file specified by --kubeconfig does not exist, the bootstrap kubeconfig is used to request a client certificate from the API server. On success, a kubeconfig file referencing the generated client certificate and key is written to the path specified by --kubeconfig. The client certificate and key file will be stored in the directory pointed by --cert-dir.

- config string

    The Kubelet will load its initial configuration from this file. The path may be absolute or relative; relative paths start at the Kubelet's current working directory. Omit this flag to use the built-in default configuration values. Command-line flags override configuration from this file.

- dynamic-config-dir string

    The Kubelet will use this directory for checkpointing downloaded configurations and tracking configuration health. The Kubelet will create this directory if it does not already exist. The path may be absolute or relative; relative paths start at the Kubelet's current working directory. Providing this flag enables dynamic Kubelet configuration. Presently, you must also enable the DynamicKubeletConfig feature gate to pass this flag.

- experimental-bootstrap-kubeconfig string

    deprecated: use --bootstrap-kubeconfig

- kubeconfig string

    Path to a kubeconfig file, specifying how to connect to the API server. Providing --kubeconfig enables API server mode, omitting --kubeconfig enables standalone mode.


- rotate-certificates

    <Warning: Beta feature> Auto rotate the kubelet client certificates by requesting new certificates from the kube-apiserver when the certificate expiration approaches.


### test
- really-crash-for-testing

    If true, when panics occur crash. Intended for testing.

- chaos-chance float

    If > 0.0, introduce random client errors and latency. Intended for testing.



### misc

- containerized

    Running kubelet in a container.





### lock
- exit-on-lock-contention

    Whether kubelet should exit upon lock-file contention.

- lock-file string

    <Warning: Alpha feature> The path to file for kubelet to use as a lock file.


### dir


- root-dir string

    Directory path for managing kubelet files (volume mounts,etc). (default "/var/lib/kubelet")


- volume-plugin-dir string

    The full path of the directory in which to search for additional third party volume plugins (default "/usr/libexec/kubernetes/kubelet-plugins/volume/exec/")

- cert-dir string

    The directory where the TLS certs are located. If --tls-cert-file and --tls-private-key-file are provided, this flag will be ignored. (default "/var/lib/kubelet/pki")



### default

- help

    help for kubelet

- version version[=true]

    Print version information and quit




### kernel



- seccomp-profile-root string

    <Warning: Alpha feature> Directory path for seccomp profiles. (default "/var/lib/kubelet/seccomp")

- experimental-kernel-memcg-notification

    If enabled, the kubelet will integrate with the kernel memcg notification to determine if memory eviction thresholds are crossed rather than polling.

- experimental-allowed-unsafe-sysctls strings

    Comma-separated whitelist of unsafe sysctls or unsafe sysctl patterns (ending in *). Use these at your own risk.


### log
- log-flush-frequency duration

    Maximum number of seconds between log flushes (default 5s)

### glog

- alsologtostderr

    log to standard error as well as files

- log-backtrace-at traceLocation

    when logging hits line file:N, emit a stack trace (default :0)

- log-dir string

    If non-empty, write log files in this directory



- logtostderr

    log to standard error instead of files (default true)

- stderrthreshold severity

    logs at or above this threshold go to stderr (default 2)

- v Level

    log level for V logs

- vmodule moduleSpec

    comma-separated list of pattern=N settings for file-filtered logging


### cadvisor
- housekeeping-interval duration

    Interval between container housekeepings (default 10s)

- docker-root string

    DEPRECATED: docker root is read from docker info (this is a fallback, default: /var/lib/docker) (default "/var/lib/docker")



### network

- cni-bin-dir string

    <Warning: Alpha feature> The full path of the directory in which to search for CNI plugin binaries. Default: /opt/cni/bin

- cni-conf-dir string

    <Warning: Alpha feature> The full path of the directory in which to search for CNI config files. Default: /etc/cni/net.d

- network-plugin string

    <Warning: Alpha feature> The name of the network plugin to be invoked for various events in kubelet/pod lifecycle

- network-plugin-mtu int32

    <Warning: Alpha feature> The MTU to be passed to the network plugin, to override the default. Set to 0 to use the default 1460 MTU.


