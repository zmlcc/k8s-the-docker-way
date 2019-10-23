A detailed description of the command-line flag of apiserver



### APIEnablement

- runtime-config mapStringString

    A set of key=value pairs that describe runtime configuration that may be passed to apiserver. <group>/<version> (or <version> for the core group) key can be used to turn on/off specific api versions. api/all is special key to control all api versions, be careful setting it false, unless you know what you do. api/legacy is deprecated, we will remove it in the future, so stop using it.



### Admission

- admission-control strings

    Admission is divided into two phases. In the first phase, only mutating admission plugins run. In the second phase, only validating admission plugins run. The names in the below list may represent a validating plugin, a mutating plugin, or both. The order of plugins in which they are passed to this flag does not matter. Comma-delimited list of: AlwaysAdmit, AlwaysDeny, AlwaysPullImages, DefaultStorageClass, DefaultTolerationSeconds, DenyEscalatingExec, DenyExecOnPrivileged, EventRateLimit, ExtendedResourceToleration, ImagePolicyWebhook, LimitPodHardAntiAffinityTopology, LimitRanger, MutatingAdmissionWebhook, NamespaceAutoProvision, NamespaceExists, NamespaceLifecycle, NodeRestriction, OwnerReferencesPermissionEnforcement, PersistentVolumeClaimResize, PersistentVolumeLabel, PodNodeSelector, PodPreset, PodSecurityPolicy, PodTolerationRestriction, Priority, ResourceQuota, SecurityContextDeny, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionWebhook. (DEPRECATED: Use --enable-admission-plugins or --disable-admission-plugins instead. Will be removed in a future version.)

- admission-control-config-file string

    File with admission control configuration.

- disable-admission-plugins strings

    admission plugins that should be disabled although they are in the default enabled plugins list (NamespaceLifecycle, LimitRanger, ServiceAccount, TaintNodesByCondition, Priority, DefaultTolerationSeconds, DefaultStorageClass, StorageObjectInUseProtection, PersistentVolumeClaimResize, MutatingAdmissionWebhook, ValidatingAdmissionWebhook, ResourceQuota). Comma-delimited list of admission plugins: AlwaysAdmit, AlwaysDeny, AlwaysPullImages, DefaultStorageClass, DefaultTolerationSeconds, DenyEscalatingExec, DenyExecOnPrivileged, EventRateLimit, ExtendedResourceToleration, ImagePolicyWebhook, LimitPodHardAntiAffinityTopology, LimitRanger, MutatingAdmissionWebhook, NamespaceAutoProvision, NamespaceExists, NamespaceLifecycle, NodeRestriction, OwnerReferencesPermissionEnforcement, PersistentVolumeClaimResize, PersistentVolumeLabel, PodNodeSelector, PodPreset, PodSecurityPolicy, PodTolerationRestriction, Priority, ResourceQuota, SecurityContextDeny, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionWebhook. The order of plugins in this flag does not matter.

- enable-admission-plugins strings

    admission plugins that should be enabled in addition to default enabled ones (NamespaceLifecycle, LimitRanger, ServiceAccount, TaintNodesByCondition, Priority, DefaultTolerationSeconds, DefaultStorageClass, StorageObjectInUseProtection, PersistentVolumeClaimResize, MutatingAdmissionWebhook, ValidatingAdmissionWebhook, ResourceQuota). Comma-delimited list of admission plugins: AlwaysAdmit, AlwaysDeny, AlwaysPullImages, DefaultStorageClass, DefaultTolerationSeconds, DenyEscalatingExec, DenyExecOnPrivileged, EventRateLimit, ExtendedResourceToleration, ImagePolicyWebhook, LimitPodHardAntiAffinityTopology, LimitRanger, MutatingAdmissionWebhook, NamespaceAutoProvision, NamespaceExists, NamespaceLifecycle, NodeRestriction, OwnerReferencesPermissionEnforcement, PersistentVolumeClaimResize, PersistentVolumeLabel, PodNodeSelector, PodPreset, PodSecurityPolicy, PodTolerationRestriction, Priority, ResourceQuota, SecurityContextDeny, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionWebhook. The order of plugins in this flag does not matter.



### Admission.DefaultTolerationSeconds

- default-not-ready-toleration-seconds int

    Indicates the tolerationSeconds of the toleration for notReady:NoExecute that is added by default to every pod that does not already have such a toleration. (default 300)

- default-unreachable-toleration-seconds int

    Indicates the tolerationSeconds of the toleration for unreachable:NoExecute that is added by default to every pod that does not already have such a toleration. (default 300)



### Audit

- audit-dynamic-configuration

    Enables dynamic audit configuration. This feature also requires the DynamicAuditing feature flag

- audit-log-batch-buffer-size int

    The size of the buffer to store events before batching and writing. Only used in batch mode. (default 10000)

- audit-log-batch-max-size int

    The maximum size of a batch. Only used in batch mode. (default 1)

- audit-log-batch-max-wait duration

    The amount of time to wait before force writing the batch that hadn't reached the max size. Only used in batch mode.

- audit-log-batch-throttle-burst int

    Maximum number of requests sent at the same moment if ThrottleQPS was not utilized before. Only used in batch mode.

- audit-log-batch-throttle-enable

    Whether batching throttling is enabled. Only used in batch mode.

- audit-log-batch-throttle-qps float32

    Maximum average number of batches per second. Only used in batch mode.

- audit-log-format string

    Format of saved audits. "legacy" indicates 1-line text format for each event. "json" indicates structured json format. Known formats are legacy,json. (default "json")

- audit-log-maxage int

    The maximum number of days to retain old audit log files based on the timestamp encoded in their filename.

- audit-log-maxbackup int

    The maximum number of old audit log files to retain.

- audit-log-maxsize int

    The maximum size in megabytes of the audit log file before it gets rotated.

- audit-log-mode string

    Strategy for sending audit events. Blocking indicates sending events should block server responses. Batch causes the backend to buffer and write events asynchronously. Known modes are batch,blocking,blocking-strict. (default "blocking")

- audit-log-path string

    If set, all requests coming to the apiserver will be logged to this file.  '-' means standard out.

- audit-log-truncate-enabled

    Whether event and batch truncating is enabled.

- audit-log-truncate-max-batch-size int

    Maximum size of the batch sent to the underlying backend. Actual serialized size can be several hundreds of bytes greater. If a batch exceeds this limit, it is split into several batches of smaller size. (default 10485760)

- audit-log-truncate-max-event-size int

    Maximum size of the audit event sent to the underlying backend. If the size of an event is greater than this number, first request and response are removed, and if this doesn't reduce the size enough, event is discarded. (default 102400)

- audit-log-version string

    API group and version used for serializing audit events written to log. (default "audit.k8s.io/v1")

- audit-policy-file string

    Path to the file that defines the audit policy configuration.

- audit-webhook-batch-buffer-size int

    The size of the buffer to store events before batching and writing. Only used in batch mode. (default 10000)

- audit-webhook-batch-max-size int

    The maximum size of a batch. Only used in batch mode. (default 400)

- audit-webhook-batch-max-wait duration

    The amount of time to wait before force writing the batch that hadn't reached the max size. Only used in batch mode. (default 30s)

- audit-webhook-batch-throttle-burst int

    Maximum number of requests sent at the same moment if ThrottleQPS was not utilized before. Only used in batch mode. (default 15)

- audit-webhook-batch-throttle-enable

    Whether batching throttling is enabled. Only used in batch mode. (default true)

- audit-webhook-batch-throttle-qps float32

    Maximum average number of batches per second. Only used in batch mode. (default 10)

- audit-webhook-config-file string

    Path to a kubeconfig formatted file that defines the audit webhook configuration.

- audit-webhook-initial-backoff duration

    The amount of time to wait before retrying the first failed request. (default 10s)

- audit-webhook-mode string

    Strategy for sending audit events. Blocking indicates sending events should block server responses. Batch causes the backend to buffer and write events asynchronously. Known modes are batch,blocking,blocking-strict. (default "batch")

- audit-webhook-truncate-enabled

    Whether event and batch truncating is enabled.

- audit-webhook-truncate-max-batch-size int

    Maximum size of the batch sent to the underlying backend. Actual serialized size can be several hundreds of bytes greater. If a batch exceeds this limit, it is split into several batches of smaller size. (default 10485760)

- audit-webhook-truncate-max-event-size int

    Maximum size of the audit event sent to the underlying backend. If the size of an event is greater than this number, first request and response are removed, and if this doesn't reduce the size enough, event is discarded. (default 102400)

- audit-webhook-version string

    API group and version used for serializing audit events written to webhook. (default "audit.k8s.io/v1")



### Authentication.Anonymous

- anonymous-auth

    Enables anonymous requests to the secure port of the API server. Requests that are not rejected by another authentication method are treated as anonymous requests. Anonymous requests have a username of system:anonymous, and a group name of system:unauthenticated. (default true)



### Authentication.BootstrapToken

- enable-bootstrap-token-auth

    Enable to allow secrets of type 'bootstrap.kubernetes.io/token' in the 'kube-system' namespace to be used for TLS bootstrapping authentication.



### Authentication.ClientCert

- client-ca-file string

    If set, any request presenting a client certificate signed by one of the authorities in the client-ca-file is authenticated with an identity corresponding to the CommonName of the client certificate.



### Authentication.OIDC

- oidc-ca-file string

    If set, the OpenID server's certificate will be verified by one of the authorities in the oidc-ca-file, otherwise the host's root CA set will be used.

- oidc-client-id string

    The client ID for the OpenID Connect client, must be set if oidc-issuer-url is set.

- oidc-groups-claim string

    If provided, the name of a custom OpenID Connect claim for specifying user groups. The claim value is expected to be a string or array of strings. This flag is experimental, please see the authentication documentation for further details.

- oidc-groups-prefix string

    If provided, all groups will be prefixed with this value to prevent conflicts with other authentication strategies.

- oidc-issuer-url string

    The URL of the OpenID issuer, only HTTPS scheme will be accepted. If set, it will be used to verify the OIDC JSON Web Token (JWT).

- oidc-required-claim mapStringString

    A key=value pair that describes a required claim in the ID Token. If set, the claim is verified to be present in the ID Token with a matching value. Repeat this flag to specify multiple claims.

- oidc-signing-algs strings

    Comma-separated list of allowed JOSE asymmetric signing algorithms. JWTs with a 'alg' header value not in this list will be rejected. Values are defined by RFC 7518 https://tools.ietf.org/html/rfc7518#section-3.1. (default [RS256])

- oidc-username-claim string

    The OpenID claim to use as the user name. Note that claims other than the default ('sub') is not guaranteed to be unique and immutable. This flag is experimental, please see the authentication documentation for further details. (default "sub")

- oidc-username-prefix string

    If provided, all usernames will be prefixed with this value. If not provided, username claims other than 'email' are prefixed by the issuer URL to avoid clashes. To skip any prefixing, provide the value '-'.



### Authentication.PasswordFile

- basic-auth-file string

    If set, the file that will be used to admit requests to the secure port of the API server via http basic authentication.



### Authentication.RequestHeader

- requestheader-allowed-names strings

    List of client certificate common names to allow to provide usernames in headers specified by --requestheader-username-headers. If empty, any client certificate validated by the authorities in --requestheader-client-ca-file is allowed.

- requestheader-client-ca-file string

    Root certificate bundle to use to verify client certificates on incoming requests before trusting usernames in headers specified by --requestheader-username-headers. WARNING: generally do not depend on authorization being already done for incoming requests.

- requestheader-extra-headers-prefix strings

    List of request header prefixes to inspect. X-Remote-Extra- is suggested.

- requestheader-group-headers strings

    List of request headers to inspect for groups. X-Remote-Group is suggested.

- requestheader-username-headers strings

    List of request headers to inspect for usernames. X-Remote-User is common.



### Authentication.ServiceAccounts

- api-audiences strings

    Identifiers of the API. The service account token authenticator will validate that tokens used against the API are bound to at least one of these audiences. If the --service-account-issuer flag is configured and this flag is not, this field defaults to a single element list containing the issuer URL .

- service-account-issuer string

    Identifier of the service account token issuer. The issuer will assert this identifier in "iss" claim of issued tokens. This value is a string or URI.

- service-account-key-file stringArray

    File containing PEM-encoded x509 RSA or ECDSA private or public keys, used to verify ServiceAccount tokens. The specified file can contain multiple keys, and the flag can be specified multiple times with different files. If unspecified, --tls-private-key-file is used. Must be specified when --service-account-signing-key is provided

- service-account-lookup

    If true, validate ServiceAccount tokens exist in etcd as part of authentication. (default true)

- service-account-max-token-expiration duration

    The maximum validity duration of a token created by the service account token issuer. If an otherwise valid TokenRequest with a validity duration larger than this value is requested, a token will be issued with a validity duration of this value.



### Authentication.TokenFile

- token-auth-file string

    If set, the file that will be used to secure the secure port of the API server via token authentication.



### Authentication.WebHook

- authentication-token-webhook-cache-ttl duration

    The duration to cache responses from the webhook token authenticator. (default 2m0s)

- authentication-token-webhook-config-file string

    File with webhook configuration for token authentication in kubeconfig format. The API server will query the remote service to determine authentication for bearer tokens.



### Authorization

- authorization-mode strings

    Ordered list of plug-ins to do authorization on secure port. Comma-delimited list of: AlwaysAllow,AlwaysDeny,ABAC,Webhook,RBAC,Node. (default [AlwaysAllow])

- authorization-policy-file string

    File with authorization policy in json line by line format, used with --authorization-mode=ABAC, on the secure port.

- authorization-webhook-cache-authorized-ttl duration

    The duration to cache 'authorized' responses from the webhook authorizer. (default 5m0s)

- authorization-webhook-cache-unauthorized-ttl duration

    The duration to cache 'unauthorized' responses from the webhook authorizer. (default 30s)

- authorization-webhook-config-file string

    File with webhook configuration in kubeconfig format, used with --authorization-mode=Webhook. The API server will query the remote service to determine access on the API server's secure port.



### CloudProvider

- cloud-provider-gce-lb-src-cidrs cidrs

    CIDRs opened in GCE firewall for LB traffic proxy & health checks (default 130.211.0.0/22,209.85.152.0/22,209.85.204.0/22,35.191.0.0/16)

- cloud-config string

    The path to the cloud provider configuration file. Empty string for no configuration file.

- cloud-provider string

    The provider for cloud services. Empty string for no provider.



### Etcd

- default-watch-cache-size int

    Default watch cache size. If zero, watch cache will be disabled for resources that do not have a default watch size set. (default 100)

- delete-collection-workers int

    Number of workers spawned for DeleteCollection call. These are used to speed up namespace cleanup. (default 1)

- enable-garbage-collector

    Enables the generic garbage collector. MUST be synced with the corresponding flag of the kube-controller-manager. (default true)

- encryption-provider-config string

    The file containing configuration for encryption providers to be used for storing secrets in etcd

- etcd-cafile string

    SSL Certificate Authority file used to secure etcd communication.

- etcd-certfile string

    SSL certification file used to secure etcd communication.

- etcd-compaction-interval duration

    The interval of compaction requests. If 0, the compaction request from apiserver is disabled. (default 5m0s)

- etcd-count-metric-poll-period duration

    Frequency of polling etcd for number of resources per type. 0 disables the metric collection. (default 1m0s)

- etcd-keyfile string

    SSL key file used to secure etcd communication.

- etcd-prefix string

    The prefix to prepend to all resource paths in etcd. (default "/registry")

- etcd-servers strings

    List of etcd servers to connect with (scheme://ip:port), comma separated.

- etcd-servers-overrides strings

    Per-resource etcd servers overrides, comma separated. The individual override format: group/resource#servers, where servers are URLs, semicolon separated.

- storage-backend string

    The storage backend for persistence. Options: 'etcd3' (default).

- storage-media-type string

    The media type to use to store objects in storage. Some resources or storage backends may only support a specific media type and will ignore this setting. (default "application/vnd.kubernetes.protobuf")

- watch-cache

    Enable watch caching in the apiserver (default true)

- watch-cache-sizes strings

    Watch cache size settings for some resources (pods, nodes, etc.), comma separated. The individual setting format: resource[.group]#size, where resource is lowercase plural (no version), group is omitted for resources of apiVersion v1 (the legacy core API) and included for others, and size is a number. It takes effect when watch-cache is enabled. Some resources (replicationcontrollers, endpoints, nodes, pods, services, apiservices.apiregistration.k8s.io) have system defaults set by heuristics, others default to default-watch-cache-size



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



### Features

- contention-profiling

    Enable lock contention profiling, if profiling is enabled

- profiling

    Enable profiling via web interface host:port/debug/pprof/ (default true)



### GenericServerRun

- advertise-address ip

    The IP address on which to advertise the apiserver to members of the cluster. This address must be reachable by the rest of the cluster. If blank, the --bind-address will be used. If --bind-address is unspecified, the host's default interface will be used.

- cors-allowed-origins strings

    List of allowed origins for CORS, comma separated.  An allowed origin can be a regular expression to support subdomain matching. If this list is empty CORS will not be enabled.

- enable-inflight-quota-handler

    If true, replace the max-in-flight handler with an enhanced one that queues and dispatches with priority and fairness

- external-hostname string

    The hostname to use when generating externalized URLs for this master (e.g. Swagger API Docs).

- master-service-namespace string

    DEPRECATED: the namespace from which the kubernetes master services should be injected into pods. (default "default")

- max-mutating-requests-inflight int

    The maximum number of mutating requests in flight at a given time. When the server exceeds this, it rejects requests. Zero for no limit. (default 200)

- max-requests-inflight int

    The maximum number of non-mutating requests in flight at a given time. When the server exceeds this, it rejects requests. Zero for no limit. (default 400)

- min-request-timeout int

    An optional field indicating the minimum number of seconds a handler must keep a request open before timing it out. Currently only honored by the watch request handler, which picks a randomized value above this number as the connection timeout, to spread out load. (default 1800)

- request-timeout duration

    An optional field indicating the duration a handler must keep a request open before timing it out. This is the default request timeout for requests but may be overridden by flags such as --min-request-timeout for specific types of requests. (default 1m0s)

- target-ram-mb int

    Memory limit for apiserver in MB (used to configure sizes of caches, etc.)



### InsecureServing

- address ip

    The IP address on which to serve the insecure --port (set to 0.0.0.0 for all IPv4 interfaces and :: for all IPv6 interfaces). (default 127.0.0.1) (DEPRECATED: see --bind-address instead.)

- insecure-bind-address ip

    The IP address on which to serve the --insecure-port (set to 0.0.0.0 for all IPv4 interfaces and :: for all IPv6 interfaces). (default 127.0.0.1) (DEPRECATED: This flag will be removed in a future version.)

- insecure-port int

    The port on which to serve unsecured, unauthenticated access. (default 8080) (DEPRECATED: This flag will be removed in a future version.)

- port int

    The port on which to serve unsecured, unauthenticated access. Set to 0 to disable. (default 8080) (DEPRECATED: see --secure-port instead.)



### SecureServing

- bind-address ip

    The IP address on which to listen for the --secure-port port. The associated interface(s) must be reachable by the rest of the cluster, and by CLI/web clients. If blank, all interfaces will be used (0.0.0.0 for all IPv4 interfaces and :: for all IPv6 interfaces). (default 0.0.0.0)

- cert-dir string

    The directory where the TLS certs are located. If --tls-cert-file and --tls-private-key-file are provided, this flag will be ignored. (default "/var/run/kubernetes")

- http2-max-streams-per-connection int

    The limit that the server gives to clients for the maximum number of streams in an HTTP/2 connection. Zero means to use golang's default.

- secure-port int

    The port on which to serve HTTPS with authentication and authorization.It cannot be switched off with 0. (default 6443)

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



### cluster

- apiserver-count int

    The number of apiservers running in the cluster, must be a positive number. (In use when --endpoint-reconciler-type=master-count is enabled.) (default 1)

- enable-aggregator-routing

    Turns on aggregator routing requests to endpoints IP rather than cluster IP.

- endpoint-reconciler-type string

    Use an endpoint reconciler (master-count, lease, none) (default "lease")



### kubelet

- kubelet-certificate-authority string

    Path to a cert file for the certificate authority.

- kubelet-client-certificate string

    Path to a client cert file for TLS.

- kubelet-client-key string

    Path to a client key file for TLS.

- kubelet-https

    Use https for kubelet connections. (default true)

- kubelet-preferred-address-types strings

    List of the preferred NodeAddressTypes to use for kubelet connections. (default [Hostname,InternalDNS,InternalIP,ExternalDNS,ExternalIP])

- kubelet-read-only-port uint

    DEPRECATED: kubelet port. (default 10255)

- kubelet-timeout duration

    Timeout for kubelet operations. (default 5s)



### misc

- allow-privileged

    If true, allow privileged containers. [default=false]

- event-ttl duration

    Amount of time to retain events. (default 1h0m0s)

- max-connection-bytes-per-sec int

    If non-zero, throttle each user connection to this number of bytes/sec. Currently only applies to long-running requests.

- proxy-client-cert-file string

    Client certificate used to prove the identity of the aggregator or kube-apiserver when it must call out during a request. This includes proxying requests to a user api-server and calling out to webhook admission plugins. It is expected that this cert includes a signature from the CA in the --requestheader-client-ca-file flag. That CA is published in the 'extension-apiserver-authentication' configmap in the kube-system namespace. Components receiving calls from kube-aggregator should use that CA to perform their half of the mutual TLS verification.

- proxy-client-key-file string

    Private key for the client certificate used to prove the identity of the aggregator or kube-apiserver when it must call out during a request. This includes proxying requests to a user api-server and calling out to webhook admission plugins.

- service-account-signing-key-file string

    Path to the file that contains the current private key of the service account token issuer. The issuer will sign issued ID tokens with this private key. (Requires the 'TokenRequest' feature gate.)

- help

    help for kube-apiserver

- log-flush-frequency duration

    Maximum number of seconds between log flushes (default 5s)

- version version[=true]

    Print version information and quit



### service

- kubernetes-service-node-port int

    If non-zero, the Kubernetes master service (which apiserver creates/maintains) will be of type NodePort, using this as the value of the port. If zero, the Kubernetes master service will be of type ClusterIP.

- service-cluster-ip-range ipNet

    A CIDR notation IP range from which to assign service cluster IPs. This must not overlap with any IP ranges assigned to nodes for pods. (default 10.0.0.0/24)

- service-node-port-range portRange

    A port range to reserve for services with NodePort visibility. Example: '30000-32767'. Inclusive at both ends of the range. (default 30000-32767)



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

