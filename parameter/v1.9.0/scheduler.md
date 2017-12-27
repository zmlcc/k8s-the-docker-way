A detailed description of the command-line flag of scheduler



### address

- address string

    The IP address to serve on (set to 0.0.0.0 for all interfaces)

- port int32

    The port that the scheduler's http service runs on (default 10251)



### admission

- ir-data-source string

    Data source used by InitialResources. Supported options: influxdb, gcm. (default "influxdb")

- ir-dbname string

    InfluxDB database name which contains metrics required by InitialResources (default "k8s")

- ir-hawkular string

    Hawkular configuration URL

- ir-influxdb-host string

    Address of InfluxDB which contains metrics required by InitialResources (default "localhost:8080/api/v1/namespaces/kube-system/services/monitoring-influxdb:api/proxy")

- ir-namespace-only

    Whether the estimation should be made only based on data from the same namespace.

- ir-password string

    Password used for connecting to InfluxDB (default "root")

- ir-percentile int

    Which percentile of samples should InitialResources use when estimating resources. For experiment purposes. (default 90)

- ir-user string

    User used for connecting to InfluxDB (default "root")



### api

- kube-api-burst int32

    Burst to use while talking with kubernetes apiserver (default 100)

- kube-api-content-type string

    Content type of requests sent to apiserver. (default "application/vnd.kubernetes.protobuf")

- kube-api-qps float32

    QPS to use while talking with kubernetes apiserver (default 50)

- master string

    The address of the Kubernetes API server (overrides any value in kubeconfig)



### cloud

- azure-container-registry-config string

    Path to the file container Azure container registry configuration information.

- cloud-provider-gce-lb-src-cidrs cidrs

    CIDRs opened in GCE firewall for LB traffic proxy & health checks (default 130.211.0.0/22,35.191.0.0/16,209.85.152.0/22,209.85.204.0/22)

- google-json-key string

    The Google Cloud Platform Service Account JSON Key to use for authentication.



### container

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



### event

- event-storage-age-limit string

    Max length of time for which to store events (per type). Value is a comma separated list of key values, where the keys are event types (e.g.: creation, oom) or "default" and the value is a duration. Default is applied to all non-specified event types (default "default=0")

- event-storage-event-limit string

    Max number of events to store (per type). Value is a comma separated list of key values, where the keys are event types (e.g.: creation, oom) or "default" and the value is an integer. Default is applied to all non-specified event types (default "default=0")



### feature

- feature-gates mapStringBool

    A set of key=value pairs that describe feature gates for alpha/experimental features. Options are:
```
APIListChunking=true|false (BETA - default=true)
APIResponseCompression=true|false (ALPHA - default=false)
Accelerators=true|false (ALPHA - default=false)
AdvancedAuditing=true|false (BETA - default=true)
AllAlpha=true|false (ALPHA - default=false)
AllowExtTrafficLocalEndpoints=true|false (default=true)
AppArmor=true|false (BETA - default=true)
BlockVolume=true|false (ALPHA - default=false)
CPUManager=true|false (ALPHA - default=false)
CSIPersistentVolume=true|false (ALPHA - default=false)
CustomPodDNS=true|false (ALPHA - default=false)
CustomResourceValidation=true|false (BETA - default=true)
DebugContainers=true|false (ALPHA - default=false)
DevicePlugins=true|false (ALPHA - default=false)
DynamicKubeletConfig=true|false (ALPHA - default=false)
EnableEquivalenceClassCache=true|false (ALPHA - default=false)
ExpandPersistentVolumes=true|false (ALPHA - default=false)
ExperimentalCriticalPodAnnotation=true|false (ALPHA - default=false)
ExperimentalHostUserNamespaceDefaulting=true|false (BETA - default=false)
HugePages=true|false (ALPHA - default=false)
Initializers=true|false (ALPHA - default=false)
KubeletConfigFile=true|false (ALPHA - default=false)
LocalStorageCapacityIsolation=true|false (ALPHA - default=false)
MountContainers=true|false (ALPHA - default=false)
MountPropagation=true|false (ALPHA - default=false)
PVCProtection=true|false (ALPHA - default=false)
PersistentLocalVolumes=true|false (ALPHA - default=false)
PodPriority=true|false (ALPHA - default=false)
ResourceLimitsPriorityFunction=true|false (ALPHA - default=false)
RotateKubeletClientCertificate=true|false (BETA - default=true)
RotateKubeletServerCertificate=true|false (ALPHA - default=false)
ServiceNodeExclusion=true|false (ALPHA - default=false)
StreamingProxyRedirects=true|false (BETA - default=true)
SupportIPVSProxyMode=true|false (BETA - default=false)
TaintBasedEvictions=true|false (ALPHA - default=false)
TaintNodesByCondition=true|false (ALPHA - default=false)
VolumeScheduling=true|false (ALPHA - default=false)
```



### general

- boot-id-file string

    Comma-separated list of files to check for boot-id. Use the first one that exists. (default "/proc/sys/kernel/random/boot_id")

- config string

    The path to the configuration file.

- enable-load-reader

    Whether to enable cpu load reader

- help

    help for hyperkube

- kubeconfig string

    Path to kubeconfig file with authorization and master location information.

- lock-object-name string

    Define the name of the lock object. (default "kube-scheduler")

- lock-object-namespace string

    Define the namespace of the lock object. (default "kube-system")

- machine-id-file string

    Comma-separated list of files to check for machine-id. Use the first one that exists. (default "/etc/machine-id,/var/lib/dbus/machine-id")

- scheduler-name string

    Name of the scheduler, used to select which pods will be processed by this scheduler, based on pod's "spec.SchedulerName". (default "default-scheduler")

- version version[=true]

    Print version information and quit



### ha

- leader-elect

    Start a leader election client and gain leadership before executing the main loop. Enable this when running replicated components for high availability.

- leader-elect-lease-duration duration

    The duration that non-leader candidates will wait after observing a leadership renewal until attempting to acquire leadership of a led but unrenewed leader slot. This is effectively the maximum duration that a leader can be stopped before it is replaced by another candidate. This is only applicable if leader election is enabled. (default 15s)

- leader-elect-renew-deadline duration

    The interval between attempts by the acting master to renew a leadership slot before it stops leading. This must be less than or equal to the lease duration. This is only applicable if leader election is enabled. (default 10s)

- leader-elect-resource-lock endpoints

    The type of resource object that is used for locking during leader election. Supported options are endpoints (default) and `configmaps`. (default "endpoints")

- leader-elect-retry-period duration

    The duration the clients should wait between attempting acquisition and renewal of a leadership. This is only applicable if leader election is enabled. (default 2s)



### limiter

- default-not-ready-toleration-seconds int

    Indicates the tolerationSeconds of the toleration for notReady:NoExecute that is added by default to every pod that does not already have such a toleration. (default 300)

- default-unreachable-toleration-seconds int

    Indicates the tolerationSeconds of the toleration for unreachable:NoExecute that is added by default to every pod that does not already have such a toleration. (default 300)



### log

- alsologtostderr

    log to standard error as well as files

- log-backtrace-at traceLocation

    when logging hits line file:N, emit a stack trace (default :0)

- log-cadvisor-usage

    Whether to log the usage of the cAdvisor container

- log-dir string

    If non-empty, write log files in this directory

- log-flush-frequency duration

    Maximum number of seconds between log flushes (default 5s)

- loglevel int

    Log level (0 = DEBUG, 5 = FATAL) (default 1)

- logtostderr

    log to standard error instead of files (default true)

- stderrthreshold severity

    logs at or above this threshold go to stderr (default 2)

- v Level

    log level for V logs

- vmodule moduleSpec

    comma-separated list of pattern=N settings for file-filtered logging



### monitor

- application-metrics-count-limit int

    Max number of application metrics to store (per container) (default 100)

- global-housekeeping-interval duration

    Interval between global housekeepings (default 1m0s)

- housekeeping-interval duration

    Interval between container housekeepings (default 10s)



### policy

- algorithm-provider string

    The scheduling algorithm provider to use, one of: ClusterAutoscalerProvider | DefaultProvider

- policy-config-file string

    File with scheduler policy configuration. This file is used if policy ConfigMap is not provided or --use-legacy-policy-config==true

- policy-configmap string

    Name of the ConfigMap object that contains scheduler's policy configuration. It must exist in the system namespace before scheduler initialization if --use-legacy-policy-config==false. The config must be provided as the value of an element in 'Data' map with the key='policy.cfg'

- policy-configmap-namespace string

    The namespace where policy ConfigMap is located. The system namespace will be used if this is not provided or is empty.

- use-legacy-policy-config

    When set to true, scheduler will ignore policy ConfigMap and uses policy config file



### profiling

- contention-profiling

    Enable lock contention profiling, if profiling is enabled

- profiling

    Enable profiling via web interface host:port/debug/pprof/



### storage

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



### tls

- allow-verification-with-non-compliant-keys

    Allow a SignatureVerifier to use keys which are technically non-compliant with RFC6962.

