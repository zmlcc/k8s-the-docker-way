A detailed description of the command-line flag of controller-manager



### AttachDetachController

- attach-detach-reconcile-sync-period duration

    The reconciler sync wait time between volume attach detach. This duration must be larger than one second, and increasing this value from the default may allow for volumes to be mismatched with pods. (default 1m0s)

- disable-attach-detach-reconcile-sync

    Disable volume attach detach reconciler sync. Disabling this may cause volumes to be mismatched with pods. Use wisely.



### Authentication

- authentication-kubeconfig string

    kubeconfig file pointing at the 'core' kubernetes server with enough rights to create tokenaccessreviews.authentication.k8s.io. This is optional. If empty, all token requests are considered to be anonymous and no client CA is looked up in the cluster.

- authentication-skip-lookup

    If false, the authentication-kubeconfig will be used to lookup missing authentication configuration from the cluster.

- authentication-token-webhook-cache-ttl duration

    The duration to cache responses from the webhook token authenticator. (default 10s)

- authentication-tolerate-lookup-failure

    If true, failures to look up missing authentication configuration from the cluster are not considered fatal. Note that this can result in authentication that treats all requests as anonymous.



### Authentication.ClientCert

- client-ca-file string

    If set, any request presenting a client certificate signed by one of the authorities in the client-ca-file is authenticated with an identity corresponding to the CommonName of the client certificate.



### Authentication.RequestHeader

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



### CSRSigningController

- cluster-signing-cert-file string

    Filename containing a PEM-encoded X509 CA certificate used to issue cluster-scoped certificates (default "/etc/kubernetes/ca/ca.pem")

- cluster-signing-key-file string

    Filename containing a PEM-encoded RSA or ECDSA private key used to sign cluster-scoped certificates (default "/etc/kubernetes/ca/ca.key")

- experimental-cluster-signing-duration duration

    The length of duration signed certificates will be given. (default 8760h0m0s)



### CloudProvider

- cloud-config string

    The path to the cloud provider configuration file. Empty string for no configuration file.

- cloud-provider string

    The provider for cloud services. Empty string for no provider.



### Debugging

- contention-profiling

    Enable lock contention profiling, if profiling is enabled

- profiling

    Enable profiling via web interface host:port/debug/pprof/



### DeploymentController

- concurrent-deployment-syncs int32

    The number of deployment objects that are allowed to sync concurrently. Larger number = more responsive deployments, but more CPU (and network) load (default 5)

- deployment-controller-sync-period duration

    Period for syncing the deployments. (default 30s)



### EndPointController

- concurrent-endpoint-syncs int32

    The number of endpoint syncing operations that will be done concurrently. Larger number = faster endpoint updating, but more CPU (and network) load (default 5)



### FeatureGate

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



### GarbageCollectorController

- concurrent-gc-syncs int32

    The number of garbage collector workers that are allowed to sync concurrently. (default 20)

- enable-garbage-collector

    Enables the generic garbage collector. MUST be synced with the corresponding flag of the kube-apiserver. (default true)



### GenericComponent

- controller-start-interval duration

    Interval between starting controller managers.

- kube-api-burst int32

    Burst to use while talking with kubernetes apiserver. (default 30)

- kube-api-content-type string

    Content type of requests sent to apiserver. (default "application/vnd.kubernetes.protobuf")

- kube-api-qps float32

    QPS to use while talking with kubernetes apiserver. (default 20)

- min-resync-period duration

    The resync period in reflectors will be random between MinResyncPeriod and 2*MinResyncPeriod. (default 12h0m0s)



### HPAController

- horizontal-pod-autoscaler-cpu-initialization-period duration

    The period after pod start when CPU samples might be skipped. (default 5m0s)

- horizontal-pod-autoscaler-downscale-stabilization duration

    The period for which autoscaler will look backwards and not scale down below any recommendation it made during that period. (default 5m0s)

- horizontal-pod-autoscaler-initial-readiness-delay duration

    The period after pod start during which readiness changes will be treated as initial readiness. (default 30s)

- horizontal-pod-autoscaler-sync-period duration

    The period for syncing the number of pods in horizontal pod autoscaler. (default 15s)

- horizontal-pod-autoscaler-tolerance float

    The minimum change (from 1.0) in the desired-to-actual metrics ratio for the horizontal pod autoscaler to consider scaling. (default 0.1)



### InsecureServing

- address ip

    The IP address on which to serve the insecure --port (set to 0.0.0.0 for all IPv4 interfaces and :: for all IPv6 interfaces). (default 0.0.0.0) (DEPRECATED: see --bind-address instead.)

- port int

    The port on which to serve unsecured, unauthenticated access. Set to 0 to disable. (default 10252) (DEPRECATED: see --secure-port instead.)



### KubeCloudShared

- allocate-node-cidrs

    Should CIDRs for Pods be allocated and set on the cloud provider.

- cidr-allocator-type string

    Type of CIDR allocator to use (default "RangeAllocator")

- cluster-cidr string

    CIDR Range for Pods in cluster. Requires --allocate-node-cidrs to be true

- cluster-name string

    The instance prefix for the cluster. (default "kubernetes")

- configure-cloud-routes

    Should CIDRs allocated by allocate-node-cidrs be configured on the cloud provider. (default true)

- node-monitor-period duration

    The period for syncing NodeStatus in NodeController. (default 5s)

- route-reconciliation-period duration

    The period for reconciling routes created for Nodes by cloud provider. (default 10s)

- use-service-account-credentials

    If true, use individual service account credentials for each controller.



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

- controllers strings

    A list of controllers to enable. '*' enables all on-by-default controllers, 'foo' enables the controller named 'foo', '-foo' disables the controller named 'foo'.
```
All controllers: attachdetach, bootstrapsigner, cloud-node-lifecycle, clusterrole-aggregation, cronjob, csrapproving, csrcleaner, csrsigning, daemonset, deployment, disruption, endpoint, garbagecollector, horizontalpodautoscaling, job, namespace, nodeipam, nodelifecycle, persistentvolume-binder, persistentvolume-expander, podgc, pv-protection, pvc-protection, replicaset, replicationcontroller, resourcequota, root-ca-cert-publisher, route, service, serviceaccount, serviceaccount-token, statefulset, tokencleaner, ttl, ttl-after-finished
Disabled-by-default controllers: bootstrapsigner, tokencleaner (default [*])
```

- external-cloud-volume-plugin string

    The plugin to use when cloud provider is set to external. Can be empty, should only be set when cloud-provider is external. Currently used to allow node and volume controllers to work for in tree cloud providers.

- kubeconfig string

    Path to kubeconfig file with authorization and master location information.

- master string

    The address of the Kubernetes API server (overrides any value in kubeconfig).



### NamespaceController

- concurrent-namespace-syncs int32

    The number of namespace objects that are allowed to sync concurrently. Larger number = more responsive namespace termination, but more CPU (and network) load (default 10)

- namespace-sync-period duration

    The period for syncing namespace life-cycle updates (default 5m0s)



### NodeIpamController

- node-cidr-mask-size int32

    Mask size for node cidr in cluster. (default 24)

- service-cluster-ip-range string

    CIDR Range for Services in cluster. Requires --allocate-node-cidrs to be true



### NodeLifecycleController

- enable-taint-manager

    WARNING: Beta feature. If set to true enables NoExecute Taints and will evict all not-tolerating Pod running on Nodes tainted with this kind of Taints. (default true)

- large-cluster-size-threshold int32

    Number of nodes from which NodeController treats the cluster as large for the eviction logic purposes. --secondary-node-eviction-rate is implicitly overridden to 0 for clusters this size or smaller. (default 50)

- node-eviction-rate float32

    Number of nodes per second on which pods are deleted in case of node failure when a zone is healthy (see --unhealthy-zone-threshold for definition of healthy/unhealthy). Zone refers to entire cluster in non-multizone clusters. (default 0.1)

- node-monitor-grace-period duration

    Amount of time which we allow running Node to be unresponsive before marking it unhealthy. Must be N times more than kubelet's nodeStatusUpdateFrequency, where N means number of retries allowed for kubelet to post node status. (default 40s)

- node-startup-grace-period duration

    Amount of time which we allow starting Node to be unresponsive before marking it unhealthy. (default 1m0s)

- pod-eviction-timeout duration

    The grace period for deleting pods on failed nodes. (default 5m0s)

- secondary-node-eviction-rate float32

    Number of nodes per second on which pods are deleted in case of node failure when a zone is unhealthy (see --unhealthy-zone-threshold for definition of healthy/unhealthy). Zone refers to entire cluster in non-multizone clusters. This value is implicitly overridden to 0 if the cluster size is smaller than --large-cluster-size-threshold. (default 0.01)

- unhealthy-zone-threshold float32

    Fraction of Nodes in a zone which needs to be not Ready (minimum 3) for zone to be treated as unhealthy.  (default 0.55)



### PersistentVolumeBinderController

- enable-dynamic-provisioning

    Enable dynamic provisioning for environments that support it. (default true)

- enable-hostpath-provisioner

    Enable HostPath PV provisioning when running without a cloud provider. This allows testing and development of provisioning features.  HostPath provisioning is not supported in any way, won't work in a multi-node cluster, and should not be used for anything other than testing or development.

- flex-volume-plugin-dir string

    Full path of the directory in which the flex volume plugin should search for additional third party volume plugins. (default "/usr/libexec/kubernetes/kubelet-plugins/volume/exec/")

- pv-recycler-increment-timeout-nfs int32

    the increment of time added per Gi to ActiveDeadlineSeconds for an NFS scrubber pod (default 30)

- pv-recycler-minimum-timeout-hostpath int32

    The minimum ActiveDeadlineSeconds to use for a HostPath Recycler pod.  This is for development and testing only and will not work in a multi-node cluster. (default 60)

- pv-recycler-minimum-timeout-nfs int32

    The minimum ActiveDeadlineSeconds to use for an NFS Recycler pod (default 300)

- pv-recycler-pod-template-filepath-hostpath string

    The file path to a pod definition used as a template for HostPath persistent volume recycling. This is for development and testing only and will not work in a multi-node cluster.

- pv-recycler-pod-template-filepath-nfs string

    The file path to a pod definition used as a template for NFS persistent volume recycling

- pv-recycler-timeout-increment-hostpath int32

    the increment of time added per Gi to ActiveDeadlineSeconds for a HostPath scrubber pod.  This is for development and testing only and will not work in a multi-node cluster. (default 30)

- pvclaimbinder-sync-period duration

    The period for syncing persistent volumes and persistent volume claims (default 15s)



### PodGCController

- terminated-pod-gc-threshold int32

    Number of terminated pods that can exist before the terminated pod garbage collector starts deleting terminated pods. If <= 0, the terminated pod garbage collector is disabled. (default 12500)



### ReplicaSetController

- concurrent-replicaset-syncs int32

    The number of replica sets that are allowed to sync concurrently. Larger number = more responsive replica management, but more CPU (and network) load (default 5)



### ReplicationController

- concurrent_rc_syncs int32

    The number of replication controllers that are allowed to sync concurrently. Larger number = more responsive replica management, but more CPU (and network) load (default 5)



### ResourceQuotaController

- concurrent-resource-quota-syncs int32

    The number of resource quotas that are allowed to sync concurrently. Larger number = more responsive quota management, but more CPU (and network) load (default 5)

- resource-quota-sync-period duration

    The period for syncing quota usage status in the system (default 5m0s)



### SAController

- concurrent-serviceaccount-token-syncs int32

    The number of service account token objects that are allowed to sync concurrently. Larger number = more responsive token generation, but more CPU (and network) load (default 5)

- root-ca-file string

    If set, this root certificate authority will be included in service account's token secret. This must be a valid PEM-encoded CA bundle.

- service-account-private-key-file string

    Filename containing a PEM-encoded private RSA or ECDSA key used to sign service account tokens.



### SecureServing

- bind-address ip

    The IP address on which to listen for the --secure-port port. The associated interface(s) must be reachable by the rest of the cluster, and by CLI/web clients. If blank, all interfaces will be used (0.0.0.0 for all IPv4 interfaces and :: for all IPv6 interfaces). (default 0.0.0.0)

- cert-dir string

    The directory where the TLS certs are located. If --tls-cert-file and --tls-private-key-file are provided, this flag will be ignored.

- http2-max-streams-per-connection int

    The limit that the server gives to clients for the maximum number of streams in an HTTP/2 connection. Zero means to use golang's default.

- secure-port int

    The port on which to serve HTTPS with authentication and authorization.If 0, don't serve HTTPS at all. (default 10257)

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



### ServiceController

- concurrent-service-syncs int32

    The number of services that are allowed to sync concurrently. Larger number = more responsive service management, but more CPU (and network) load (default 1)



### TTLAfterFinishedController

- concurrent-ttl-after-finished-syncs int32

    The number of TTL-after-finished controller workers that are allowed to sync concurrently. (default 5)



### misc

- help

    help for kube-controller-manager

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

