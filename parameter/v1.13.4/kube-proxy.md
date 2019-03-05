A detailed description of the command-line flag of kube-proxy



### Deprecated

- bind-address 0.0.0.0

    The IP address for the proxy server to serve on (set to 0.0.0.0 for all IPv4 interfaces and `::` for all IPv6 interfaces) (default 0.0.0.0)

- cluster-cidr string

    The CIDR range of pods in the cluster. When configured, traffic sent to a Service cluster IP from outside this range will be masqueraded and traffic sent from pods to an external LoadBalancer IP will be directed to the respective cluster IP instead

- config-sync-period duration

    How often configuration from the apiserver is refreshed.  Must be greater than 0. (default 15m0s)

- conntrack-max-per-core int32

    Maximum number of NAT connections to track per CPU core (0 to leave the limit as-is and ignore conntrack-min). (default 32768)

- conntrack-min int32

    Minimum number of conntrack entries to allocate, regardless of conntrack-max-per-core (set conntrack-max-per-core=0 to leave the limit as-is). (default 131072)

- conntrack-tcp-timeout-close-wait duration

    NAT timeout for TCP connections in the CLOSE_WAIT state (default 1h0m0s)

- conntrack-tcp-timeout-established duration

    Idle timeout for established TCP connections (0 to leave as-is) (default 24h0m0s)

- feature-gates mapStringBool

    A set of key=value pairs that describe feature gates for alpha/experimental features. Options are:
```
APIListChunking=true|false (BETA - default=true)
APIResponseCompression=true|false (ALPHA - default=false)
AllAlpha=true|false (ALPHA - default=false)
AppArmor=true|false (BETA - default=true)
AttachVolumeLimit=true|false (BETA - default=true)
BalanceAttachedNodeVolumes=true|false (ALPHA - default=false)
BlockVolume=true|false (BETA - default=true)
BoundServiceAccountTokenVolume=true|false (ALPHA - default=false)
CPUManager=true|false (BETA - default=true)
CRIContainerLogRotation=true|false (BETA - default=true)
CSIBlockVolume=true|false (ALPHA - default=false)
CSIDriverRegistry=true|false (ALPHA - default=false)
CSINodeInfo=true|false (ALPHA - default=false)
CustomCPUCFSQuotaPeriod=true|false (ALPHA - default=false)
CustomPodDNS=true|false (BETA - default=true)
CustomResourceSubresources=true|false (BETA - default=true)
CustomResourceValidation=true|false (BETA - default=true)
CustomResourceWebhookConversion=true|false (ALPHA - default=false)
DebugContainers=true|false (ALPHA - default=false)
DevicePlugins=true|false (BETA - default=true)
DryRun=true|false (BETA - default=true)
DynamicAuditing=true|false (ALPHA - default=false)
DynamicKubeletConfig=true|false (BETA - default=true)
EnableEquivalenceClassCache=true|false (ALPHA - default=false)
ExpandInUsePersistentVolumes=true|false (ALPHA - default=false)
ExpandPersistentVolumes=true|false (BETA - default=true)
ExperimentalCriticalPodAnnotation=true|false (ALPHA - default=false)
ExperimentalHostUserNamespaceDefaulting=true|false (BETA - default=false)
HugePages=true|false (BETA - default=true)
HyperVContainer=true|false (ALPHA - default=false)
Initializers=true|false (ALPHA - default=false)
KubeletPodResources=true|false (ALPHA - default=false)
LocalStorageCapacityIsolation=true|false (BETA - default=true)
MountContainers=true|false (ALPHA - default=false)
NodeLease=true|false (ALPHA - default=false)
PersistentLocalVolumes=true|false (BETA - default=true)
PodPriority=true|false (BETA - default=true)
PodReadinessGates=true|false (BETA - default=true)
PodShareProcessNamespace=true|false (BETA - default=true)
ProcMountType=true|false (ALPHA - default=false)
QOSReserved=true|false (ALPHA - default=false)
ResourceLimitsPriorityFunction=true|false (ALPHA - default=false)
ResourceQuotaScopeSelectors=true|false (BETA - default=true)
RotateKubeletClientCertificate=true|false (BETA - default=true)
RotateKubeletServerCertificate=true|false (BETA - default=true)
RunAsGroup=true|false (ALPHA - default=false)
RuntimeClass=true|false (ALPHA - default=false)
SCTPSupport=true|false (ALPHA - default=false)
ScheduleDaemonSetPods=true|false (BETA - default=true)
ServiceNodeExclusion=true|false (ALPHA - default=false)
StreamingProxyRedirects=true|false (BETA - default=true)
SupportPodPidsLimit=true|false (ALPHA - default=false)
Sysctls=true|false (BETA - default=true)
TTLAfterFinished=true|false (ALPHA - default=false)
TaintBasedEvictions=true|false (BETA - default=true)
TaintNodesByCondition=true|false (BETA - default=true)
TokenRequest=true|false (BETA - default=true)
TokenRequestProjection=true|false (BETA - default=true)
ValidateProxyRedirects=true|false (ALPHA - default=false)
VolumeSnapshotDataSource=true|false (ALPHA - default=false)
VolumeSubpathEnvExpansion=true|false (ALPHA - default=false)
```

- healthz-bind-address 0.0.0.0

    The IP address for the health check server to serve on (set to 0.0.0.0 for all IPv4 interfaces and `::` for all IPv6 interfaces) (default 0.0.0.0:10256)

- healthz-port int32

    The port to bind the health check server. Use 0 to disable. (default 10256)

- hostname-override string

    If non-empty, will use this string as identification instead of the actual hostname.

- iptables-masquerade-bit int32

    If using the pure iptables proxy, the bit of the fwmark space to mark packets requiring SNAT with.  Must be within the range [0, 31]. (default 14)

- iptables-min-sync-period duration

    The minimum interval of how often the iptables rules can be refreshed as endpoints and services change (e.g. '5s', '1m', '2h22m').

- iptables-sync-period duration

    The maximum interval of how often iptables rules are refreshed (e.g. '5s', '1m', '2h22m').  Must be greater than 0. (default 30s)

- ipvs-exclude-cidrs strings

    A comma-separated list of CIDR's which the ipvs proxier should not touch when cleaning up IPVS rules.

- ipvs-min-sync-period duration

    The minimum interval of how often the ipvs rules can be refreshed as endpoints and services change (e.g. '5s', '1m', '2h22m').

- ipvs-scheduler string

    The ipvs scheduler type when proxy mode is ipvs

- ipvs-sync-period duration

    The maximum interval of how often ipvs rules are refreshed (e.g. '5s', '1m', '2h22m').  Must be greater than 0. (default 30s)

- kube-api-burst int32

    Burst to use while talking with kubernetes apiserver (default 10)

- kube-api-content-type string

    Content type of requests sent to apiserver. (default "application/vnd.kubernetes.protobuf")

- kube-api-qps float32

    QPS to use while talking with kubernetes apiserver (default 5)

- kubeconfig string

    Path to kubeconfig file with authorization information (the master location is set by the master flag).

- masquerade-all

    If using the pure iptables proxy, SNAT all traffic sent via Service cluster IPs (this not commonly needed)

- master string

    The address of the Kubernetes API server (overrides any value in kubeconfig)

- metrics-bind-address 0.0.0.0

    The IP address for the metrics server to serve on (set to 0.0.0.0 for all IPv4 interfaces and `::` for all IPv6 interfaces) (default 127.0.0.1:10249)

- metrics-port int32

    The port to bind the metrics server. Use 0 to disable. (default 10249)

- nodeport-addresses strings

    A string slice of values which specify the addresses to use for NodePorts. Values may be valid IP blocks (e.g. 1.2.3.0/24, 1.2.3.4/32). The default empty string slice ([]) means to use all local addresses.

- oom-score-adj int32

    The oom-score-adj value for kube-proxy process. Values must be within the range [-1000, 1000] (default -999)

- profiling

    If true enables profiling via web interface on /debug/pprof handler.

- proxy-mode ProxyMode

    Which proxy mode to use: 'userspace' (older) or 'iptables' (faster) or 'ipvs' (experimental). If blank, use the best-available proxy (currently iptables).  If the iptables proxy is selected, regardless of how, but the system's kernel or iptables versions are insufficient, this always falls back to the userspace proxy.

- proxy-port-range port-range

    Range of host ports (beginPort-endPort, single port or beginPort+offset, inclusive) that may be consumed in order to proxy service traffic. If (unspecified, 0, or 0-0) then ports will be randomly chosen.

- udp-timeout duration

    How long an idle UDP connection will be kept open (e.g. '250ms', '2s').  Must be greater than 0. Only applicable for proxy-mode=userspace (default 250ms)



### Main

- cleanup

    If true cleanup iptables and ipvs rules and exit.

- cleanup-ipvs

    If true make kube-proxy cleanup ipvs rules before running.  Default is true (default true)

- config string

    The path to the configuration file.

- write-config-to string

    If set, write the default configuration values to this file and exit.



### cloud

- azure-container-registry-config string

    Path to the file containing Azure container registry configuration information.

- cloud-provider-gce-lb-src-cidrs cidrs

    CIDRs opened in GCE firewall for LB traffic proxy & health checks (default 130.211.0.0/22,209.85.152.0/22,209.85.204.0/22,35.191.0.0/16)



### misc

- help

    help for kube-proxy

- log-flush-frequency duration

    Maximum number of seconds between log flushes (default 5s)

- version version[=true]

    Print version information and quit



### plugin.admission.defaulttolerationseconds

- default-not-ready-toleration-seconds int

    Indicates the tolerationSeconds of the toleration for notReady:NoExecute that is added by default to every pod that does not already have such a toleration. (default 300)

- default-unreachable-toleration-seconds int

    Indicates the tolerationSeconds of the toleration for unreachable:NoExecute that is added by default to every pod that does not already have such a toleration. (default 300)



### vendor.cadvisor

- application-metrics-count-limit int

    Max number of application metrics to store (per container) (default 100)

- boot-id-file string

    Comma-separated list of files to check for boot-id. Use the first one that exists. (default "/proc/sys/kernel/random/boot_id")

- container-hints string

    location of the container hints file (default "/etc/cadvisor/container_hints.json")

- containerd string

    containerd endpoint (default "unix:///var/run/containerd.sock")

- docker string

    docker endpoint (default "unix:///var/run/docker.sock")

- docker-env-metadata-whitelist string

    a comma-separated list of environment variable keys that needs to be collected for docker containers

- docker-only

    Only report docker containers in addition to root stats

- docker-root string

    DEPRECATED: docker root is read from docker info (this is a fallback, default: /var/lib/docker) (default "/var/lib/docker")

- docker-tls

    use TLS to connect to docker

- docker-tls-ca string

    path to trusted CA (default "ca.pem")

- docker-tls-cert string

    path to client certificate (default "cert.pem")

- docker-tls-key string

    path to private key (default "key.pem")

- enable-load-reader

    Whether to enable cpu load reader

- event-storage-age-limit string

    Max length of time for which to store events (per type). Value is a comma separated list of key values, where the keys are event types (e.g.: creation, oom) or "default" and the value is a duration. Default is applied to all non-specified event types (default "default=0")

- event-storage-event-limit string

    Max number of events to store (per type). Value is a comma separated list of key values, where the keys are event types (e.g.: creation, oom) or "default" and the value is an integer. Default is applied to all non-specified event types (default "default=0")

- global-housekeeping-interval duration

    Interval between global housekeepings (default 1m0s)

- housekeeping-interval duration

    Interval between container housekeepings (default 10s)

- log-cadvisor-usage

    Whether to log the usage of the cAdvisor container

- machine-id-file string

    Comma-separated list of files to check for machine-id. Use the first one that exists. (default "/etc/machine-id,/var/lib/dbus/machine-id")

- mesos-agent string

    Mesos agent address (default "127.0.0.1:5051")

- mesos-agent-timeout duration

    Mesos agent timeout (default 10s)

- storage-driver-buffer-duration duration

    Writes in the storage driver will be buffered for this duration, and committed to the non memory backends as a single transaction (default 1m0s)

- storage-driver-db string

    database name (default "cadvisor")

- storage-driver-host string

    database host:port (default "localhost:8086")

- storage-driver-password string

    database password (default "root")

- storage-driver-secure

    use secure connection with database

- storage-driver-table string

    table name (default "stats")

- storage-driver-user string

    database username (default "root")



### vendor.klog

- alsologtostderr

    log to standard error as well as files

- log-backtrace-at traceLocation

    when logging hits line file:N, emit a stack trace (default :0)

- log-dir string

    If non-empty, write log files in this directory

- log-file string

    If non-empty, use this log file

- logtostderr

    log to standard error instead of files (default true)

- skip-headers

    If true, avoid header prefixes in the log messages

- stderrthreshold severity

    logs at or above this threshold go to stderr (default 2)

- v Level

    log level for V logs

- vmodule moduleSpec

    comma-separated list of pattern=N settings for file-filtered logging

