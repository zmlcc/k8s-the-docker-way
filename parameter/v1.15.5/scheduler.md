A detailed description of the command-line flag of scheduler



### Authentication

- authentication-kubeconfig string

    kubeconfig file pointing at the 'core' kubernetes server with enough rights to create tokenaccessreviews.authentication.k8s.io. This is optional. If empty, all token requests are considered to be anonymous and no client CA is looked up in the cluster.

- authentication-skip-lookup

    If false, the authentication-kubeconfig will be used to lookup missing authentication configuration from the cluster.

- authentication-token-webhook-cache-ttl duration

    The duration to cache responses from the webhook token authenticator. (default 10s)

- authentication-tolerate-lookup-failure

    If true, failures to look up missing authentication configuration from the cluster are not considered fatal. Note that this can result in authentication that treats all requests as anonymous. (default true)

- client-ca-file string

    If set, any request presenting a client certificate signed by one of the authorities in the client-ca-file is authenticated with an identity corresponding to the CommonName of the client certificate.

- requestheader-allowed-names strings

    List of client certificate common names to allow to provide usernames in headers specified by --requestheader-username-headers. If empty, any client certificate validated by the authorities in --requestheader-client-ca-file is allowed.

- requestheader-client-ca-file string

    Root certificate bundle to use to verify client certificates on incoming requests before trusting usernames in headers specified by --requestheader-username-headers. WARNING: generally do not depend on authorization being already done for incoming requests.

- requestheader-extra-headers-prefix strings

    List of request header prefixes to inspect. X-Remote-Extra- is suggested. (default [x-remote-extra-])

- requestheader-group-headers strings

    List of request headers to inspect for groups. X-Remote-Group is suggested. (default [x-remote-group])

- requestheader-username-headers strings

    List of request headers to inspect for usernames. X-Remote-User is common. (default [x-remote-user])



### Authorization

- authorization-always-allow-paths strings

    A list of HTTP paths to skip during authorization, i.e. these are authorized without contacting the 'core' kubernetes server. (default [/healthz])

- authorization-kubeconfig string

    kubeconfig file pointing at the 'core' kubernetes server with enough rights to create subjectaccessreviews.authorization.k8s.io. This is optional. If empty, all requests not skipped by authorization are forbidden.

- authorization-webhook-cache-authorized-ttl duration

    The duration to cache 'authorized' responses from the webhook authorizer. (default 10s)

- authorization-webhook-cache-unauthorized-ttl duration

    The duration to cache 'unauthorized' responses from the webhook authorizer. (default 10s)



### CombinedInsecureServing

- address string

    DEPRECATED: the IP address on which to listen for the --port port (set to 0.0.0.0 for all IPv4 interfaces and :: for all IPv6 interfaces). See --bind-address instead. (default "0.0.0.0")

- port int

    DEPRECATED: the port on which to serve HTTP insecurely without authentication and authorization. If 0, don't serve HTTPS at all. See --secure-port instead. (default 10251)



### Deprecated

- algorithm-provider string

    DEPRECATED: the scheduling algorithm provider to use, one of: ClusterAutoscalerProvider | DefaultProvider

- contention-profiling

    DEPRECATED: enable lock contention profiling, if profiling is enabled

- kube-api-burst int32

    DEPRECATED: burst to use while talking with kubernetes apiserver (default 100)

- kube-api-content-type string

    DEPRECATED: content type of requests sent to apiserver. (default "application/vnd.kubernetes.protobuf")

- kube-api-qps float32

    DEPRECATED: QPS to use while talking with kubernetes apiserver (default 50)

- kubeconfig string

    DEPRECATED: path to kubeconfig file with authorization and master location information.

- lock-object-name string

    DEPRECATED: define the name of the lock object. (default "kube-scheduler")

- lock-object-namespace string

    DEPRECATED: define the namespace of the lock object. (default "kube-system")

- policy-config-file string

    DEPRECATED: file with scheduler policy configuration. This file is used if policy ConfigMap is not provided or --use-legacy-policy-config=true

- policy-configmap string

    DEPRECATED: name of the ConfigMap object that contains scheduler's policy configuration. It must exist in the system namespace before scheduler initialization if --use-legacy-policy-config=false. The config must be provided as the value of an element in 'Data' map with the key='policy.cfg'

- policy-configmap-namespace string

    DEPRECATED: the namespace where policy ConfigMap is located. The kube-system namespace will be used if this is not provided or is empty. (default "kube-system")

- profiling

    DEPRECATED: enable profiling via web interface host:port/debug/pprof/

- scheduler-name string

    DEPRECATED: name of the scheduler, used to select which pods will be processed by this scheduler, based on pod's "spec.schedulerName". (default "default-scheduler")

- use-legacy-policy-config

    DEPRECATED: when set to true, scheduler will ignore policy ConfigMap and uses policy config file



### LeaderElection

- leader-elect

    Start a leader election client and gain leadership before executing the main loop. Enable this when running replicated components for high availability. (default true)

- leader-elect-lease-duration duration

    The duration that non-leader candidates will wait after observing a leadership renewal until attempting to acquire leadership of a led but unrenewed leader slot. This is effectively the maximum duration that a leader can be stopped before it is replaced by another candidate. This is only applicable if leader election is enabled. (default 15s)

- leader-elect-renew-deadline duration

    The interval between attempts by the acting master to renew a leadership slot before it stops leading. This must be less than or equal to the lease duration. This is only applicable if leader election is enabled. (default 10s)

- leader-elect-resource-lock endpoints

    The type of resource object that is used for locking during leader election. Supported options are endpoints (default) and `configmaps`. (default "endpoints")

- leader-elect-retry-period duration

    The duration the clients should wait between attempting acquisition and renewal of a leadership. This is only applicable if leader election is enabled. (default 2s)



### Main

- config string

    The path to the configuration file. Flags override values in this file.

- master string

    The address of the Kubernetes API server (overrides any value in kubeconfig)

- write-config-to string

    If set, write the configuration values to this file and exit.



### SecureServing

- bind-address ip

    The IP address on which to listen for the --secure-port port. The associated interface(s) must be reachable by the rest of the cluster, and by CLI/web clients. If blank, all interfaces will be used (0.0.0.0 for all IPv4 interfaces and :: for all IPv6 interfaces). (default 0.0.0.0)

- cert-dir string

    The directory where the TLS certs are located. If --tls-cert-file and --tls-private-key-file are provided, this flag will be ignored.

- http2-max-streams-per-connection int

    The limit that the server gives to clients for the maximum number of streams in an HTTP/2 connection. Zero means to use golang's default.

- secure-port int

    The port on which to serve HTTPS with authentication and authorization.If 0, don't serve HTTPS at all. (default 10259)

- tls-cert-file string

    File containing the default x509 Certificate for HTTPS. (CA cert, if any, concatenated after server cert). If HTTPS serving is enabled, and --tls-cert-file and --tls-private-key-file are not provided, a self-signed certificate and key are generated for the public address and saved to the directory specified by --cert-dir.

- tls-cipher-suites strings

    Comma-separated list of cipher suites for the server. If omitted, the default Go cipher suites will be use.  Possible values: TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305,TLS_ECDHE_ECDSA_WITH_RC4_128_SHA,TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305,TLS_ECDHE_RSA_WITH_RC4_128_SHA,TLS_RSA_WITH_3DES_EDE_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA256,TLS_RSA_WITH_AES_128_GCM_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AES_256_GCM_SHA384,TLS_RSA_WITH_RC4_128_SHA

- tls-min-version string

    Minimum TLS version supported. Possible values: VersionTLS10, VersionTLS11, VersionTLS12, VersionTLS13

- tls-private-key-file string

    File containing the default x509 private key matching --tls-cert-file.

- tls-sni-cert-key namedCertKey

    A pair of x509 certificate and private key file paths, optionally suffixed with a list of domain patterns which are fully qualified domain names, possibly with prefixed wildcard segments. If no domain patterns are provided, the names of the certificate are extracted. Non-wildcard matches trump over wildcard matches, explicit domain patterns trump over extracted names. For multiple key/certificate pairs, use the --tls-sni-cert-key multiple times. Examples: "example.crt,example.key" or "foo.crt,foo.key:*.foo.com,foo.com". (default [])



### feature

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
CSIBlockVolume=true|false (BETA - default=true)
CSIDriverRegistry=true|false (BETA - default=true)
CSIInlineVolume=true|false (ALPHA - default=false)
CSIMigration=true|false (ALPHA - default=false)
CSIMigrationAWS=true|false (ALPHA - default=false)
CSIMigrationAzureDisk=true|false (ALPHA - default=false)
CSIMigrationAzureFile=true|false (ALPHA - default=false)
CSIMigrationGCE=true|false (ALPHA - default=false)
CSIMigrationOpenStack=true|false (ALPHA - default=false)
CSINodeInfo=true|false (BETA - default=true)
CustomCPUCFSQuotaPeriod=true|false (ALPHA - default=false)
CustomResourceDefaulting=true|false (ALPHA - default=false)
CustomResourcePublishOpenAPI=true|false (BETA - default=true)
CustomResourceSubresources=true|false (BETA - default=true)
CustomResourceValidation=true|false (BETA - default=true)
CustomResourceWebhookConversion=true|false (BETA - default=true)
DebugContainers=true|false (ALPHA - default=false)
DevicePlugins=true|false (BETA - default=true)
DryRun=true|false (BETA - default=true)
DynamicAuditing=true|false (ALPHA - default=false)
DynamicKubeletConfig=true|false (BETA - default=true)
ExpandCSIVolumes=true|false (ALPHA - default=false)
ExpandInUsePersistentVolumes=true|false (BETA - default=true)
ExpandPersistentVolumes=true|false (BETA - default=true)
ExperimentalCriticalPodAnnotation=true|false (ALPHA - default=false)
ExperimentalHostUserNamespaceDefaulting=true|false (BETA - default=false)
HyperVContainer=true|false (ALPHA - default=false)
KubeletPodResources=true|false (BETA - default=true)
LocalStorageCapacityIsolation=true|false (BETA - default=true)
LocalStorageCapacityIsolationFSQuotaMonitoring=true|false (ALPHA - default=false)
MountContainers=true|false (ALPHA - default=false)
NodeLease=true|false (BETA - default=true)
NonPreemptingPriority=true|false (ALPHA - default=false)
PodShareProcessNamespace=true|false (BETA - default=true)
ProcMountType=true|false (ALPHA - default=false)
QOSReserved=true|false (ALPHA - default=false)
RemainingItemCount=true|false (ALPHA - default=false)
RequestManagement=true|false (ALPHA - default=false)
ResourceLimitsPriorityFunction=true|false (ALPHA - default=false)
ResourceQuotaScopeSelectors=true|false (BETA - default=true)
RotateKubeletClientCertificate=true|false (BETA - default=true)
RotateKubeletServerCertificate=true|false (BETA - default=true)
RunAsGroup=true|false (BETA - default=true)
RuntimeClass=true|false (BETA - default=true)
SCTPSupport=true|false (ALPHA - default=false)
ScheduleDaemonSetPods=true|false (BETA - default=true)
ServerSideApply=true|false (ALPHA - default=false)
ServiceLoadBalancerFinalizer=true|false (ALPHA - default=false)
ServiceNodeExclusion=true|false (ALPHA - default=false)
StorageVersionHash=true|false (BETA - default=true)
StreamingProxyRedirects=true|false (BETA - default=true)
SupportNodePidsLimit=true|false (BETA - default=true)
SupportPodPidsLimit=true|false (BETA - default=true)
Sysctls=true|false (BETA - default=true)
TTLAfterFinished=true|false (ALPHA - default=false)
TaintBasedEvictions=true|false (BETA - default=true)
TaintNodesByCondition=true|false (BETA - default=true)
TokenRequest=true|false (BETA - default=true)
TokenRequestProjection=true|false (BETA - default=true)
ValidateProxyRedirects=true|false (BETA - default=true)
VolumePVCDataSource=true|false (ALPHA - default=false)
VolumeSnapshotDataSource=true|false (ALPHA - default=false)
VolumeSubpathEnvExpansion=true|false (BETA - default=true)
WatchBookmark=true|false (ALPHA - default=false)
WinDSR=true|false (ALPHA - default=false)
WinOverlay=true|false (ALPHA - default=false)
WindowsGMSA=true|false (ALPHA - default=false)
```



### misc

- help

    help for kube-scheduler

- log-flush-frequency duration

    Maximum number of seconds between log flushes (default 5s)

- version version[=true]

    Print version information and quit



### vendor.klog

- alsologtostderr

    log to standard error as well as files

- log-backtrace-at traceLocation

    when logging hits line file:N, emit a stack trace (default :0)

- log-dir string

    If non-empty, write log files in this directory

- log-file string

    If non-empty, use this log file

- log-file-max-size uint

    Defines the maximum size a log file can grow to. Unit is megabytes. If the value is 0, the maximum file size is unlimited. (default 1800)

- logtostderr

    log to standard error instead of files (default true)

- skip-headers

    If true, avoid header prefixes in the log messages

- skip-log-headers

    If true, avoid headers when opening log files

- stderrthreshold severity

    logs at or above this threshold go to stderr (default 2)

- v Level

    number for the log level verbosity

- vmodule moduleSpec

    comma-separated list of pattern=N settings for file-filtered logging

