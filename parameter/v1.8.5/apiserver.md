A detailed description of the command-line flag of apiserver



### address

- bind-address ip

    The IP address on which to listen for the --secure-port port. The associated interface(s) must be reachable by the rest of the cluster, and by CLI/web clients. If blank, all interfaces will be used (0.0.0.0). (default 0.0.0.0)

- insecure-bind-address ip

    The IP address on which to serve the --insecure-port (set to 0.0.0.0 for all interfaces). (default 127.0.0.1)

- insecure-port int

    The port on which to serve unsecured, unauthenticated access. It is assumed that firewall rules are set up such that this port is not reachable from outside of the cluster and that port 443 on the cluster's public address is proxied to this port. This is performed by nginx in the default setup. (default 8080)

- kubernetes-service-node-port int

    If non-zero, the Kubernetes master service (which apiserver creates/maintains) will be of type NodePort, using this as the value of the port. If zero, the Kubernetes master service will be of type ClusterIP.

- secure-port int

    The port on which to serve HTTPS with authentication and authorization. If 0, don't serve HTTPS at all. (default 6443)



### admission

- admission-control stringSlice

    Ordered list of plug-ins to do admission control of resources into cluster. Comma-delimited list of: AlwaysAdmit, AlwaysDeny, AlwaysPullImages, DefaultStorageClass, DefaultTolerationSeconds, DenyEscalatingExec, DenyExecOnPrivileged, EventRateLimit, GenericAdmissionWebhook, ImagePolicyWebhook, InitialResources, Initializers, LimitPodHardAntiAffinityTopology, LimitRanger, NamespaceAutoProvision, NamespaceExists, NamespaceLifecycle, NodeRestriction, OwnerReferencesPermissionEnforcement, PersistentVolumeClaimResize, PersistentVolumeLabel, PodNodeSelector, PodPreset, PodSecurityPolicy, PodTolerationRestriction, Priority, ResourceQuota, SecurityContextDeny, ServiceAccount. (default [AlwaysAdmit])

- admission-control-config-file string

    File with admission control configuration.

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



### audit

- audit-log-format string

    Format of saved audits. "legacy" indicates 1-line text format for each event. "json" indicates structured json format. Requires the 'AdvancedAuditing' feature gate. Known formats are legacy,json. (default "json")

- audit-log-maxage int

    The maximum number of days to retain old audit log files based on the timestamp encoded in their filename.

- audit-log-maxbackup int

    The maximum number of old audit log files to retain.

- audit-log-maxsize int

    The maximum size in megabytes of the audit log file before it gets rotated.

- audit-log-path string

    If set, all requests coming to the apiserver will be logged to this file.  '-' means standard out.

- audit-policy-file string

    Path to the file that defines the audit policy configuration. Requires the 'AdvancedAuditing' feature gate. With AdvancedAuditing, a profile is required to enable auditing.

- audit-webhook-config-file string

    Path to a kubeconfig formatted file that defines the audit webhook configuration. Requires the 'AdvancedAuditing' feature gate.

- audit-webhook-mode string

    Strategy for sending audit events. Blocking indicates sending events should block server responses. Batch causes the webhook to buffer and send events asynchronously. Known modes are batch,blocking. (default "batch")



### authentication

- anonymous-auth

    Enables anonymous requests to the secure port of the API server. Requests that are not rejected by another authentication method are treated as anonymous requests. Anonymous requests have a username of system:anonymous, and a group name of system:unauthenticated. (default true)

- authentication-token-webhook-cache-ttl duration

    The duration to cache responses from the webhook token authenticator. (default 2m0s)

- authentication-token-webhook-config-file string

    File with webhook configuration for token authentication in kubeconfig format. The API server will query the remote service to determine authentication for bearer tokens.

- basic-auth-file string

    If set, the file that will be used to admit requests to the secure port of the API server via http basic authentication.

- enable-bootstrap-token-auth

    Enable to allow secrets of type 'bootstrap.kubernetes.io/token' in the 'kube-system' namespace to be used for TLS bootstrapping authentication.

- experimental-keystone-ca-file string

    If set, the Keystone server's certificate will be verified by one of the authorities in the experimental-keystone-ca-file, otherwise the host's root CA set will be used.

- experimental-keystone-url string

    If passed, activates the keystone authentication plugin.

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

- oidc-username-claim string

    The OpenID claim to use as the user name. Note that claims other than the default ('sub') is not guaranteed to be unique and immutable. This flag is experimental, please see the authentication documentation for further details. (default "sub")

- oidc-username-prefix string

    If provided, all usernames will be prefixed with this value. If not provided, username claims other than 'email' are prefixed by the issuer URL to avoid clashes. To skip any prefixing, provide the value '-'.

- service-account-key-file stringArray

    File containing PEM-encoded x509 RSA or ECDSA private or public keys, used to verify ServiceAccount tokens. If unspecified, --tls-private-key-file is used. The specified file can contain multiple keys, and the flag can be specified multiple times with different files.

- service-account-lookup

    If true, validate ServiceAccount tokens exist in etcd as part of authentication. (default true)

- token-auth-file string

    If set, the file that will be used to secure the secure port of the API server via token authentication.



### authorization

- authorization-mode string

    Ordered list of plug-ins to do authorization on secure port. Comma-delimited list of: AlwaysAllow,AlwaysDeny,ABAC,Webhook,RBAC,Node. (default "AlwaysAllow")

- authorization-policy-file string

    File with authorization policy in csv format, used with --authorization-mode=ABAC, on the secure port.

- authorization-webhook-cache-authorized-ttl duration

    The duration to cache 'authorized' responses from the webhook authorizer. (default 5m0s)

- authorization-webhook-cache-unauthorized-ttl duration

    The duration to cache 'unauthorized' responses from the webhook authorizer. (default 30s)

- authorization-webhook-config-file string

    File with webhook configuration in kubeconfig format, used with --authorization-mode=Webhook. The API server will query the remote service to determine access on the API server's secure port.



### cloud

- azure-container-registry-config string

    Path to the file container Azure container registry configuration information.

- cloud-config string

    The path to the cloud provider configuration file. Empty string for no configuration file.

- cloud-provider string

    The provider for cloud services. Empty string for no provider.

- cloud-provider-gce-lb-src-cidrs cidrs

    CIDRS opened in GCE firewall for LB traffic proxy & health checks (default 130.211.0.0/22,35.191.0.0/16,209.85.152.0/22,209.85.204.0/22)

- google-json-key string

    The Google Cloud Platform Service Account JSON Key to use for authentication.



### cluster

- advertise-address ip

    The IP address on which to advertise the apiserver to members of the cluster. This address must be reachable by the rest of the cluster. If blank, the --bind-address will be used. If --bind-address is unspecified, the host's default interface will be used.

- apiserver-count int

    The number of apiservers running in the cluster, must be a positive number. (default 1)

- enable-aggregator-routing

    Turns on aggregator routing requests to endoints IP rather than cluster IP.



### container

- allow-privileged

    If true, allow privileged containers. [default=false]

- container-hints string

    location of the container hints file (default "/etc/cadvisor/container_hints.json")

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



### etcd

- etcd-cafile string

    SSL Certificate Authority file used to secure etcd communication.

- etcd-certfile string

    SSL certification file used to secure etcd communication.

- etcd-keyfile string

    SSL key file used to secure etcd communication.

- etcd-prefix string

    The prefix to prepend to all resource paths in etcd. (default "/registry")

- etcd-quorum-read

    If true, enable quorum read.

- etcd-servers stringSlice

    List of etcd servers to connect with (scheme://ip:port), comma separated.

- etcd-servers-overrides stringSlice

    Per-resource etcd servers overrides, comma separated. The individual override format: group/resource#servers, where servers are http://ip:port, semicolon separated.



### event

- event-storage-age-limit string

    Max length of time for which to store events (per type). Value is a comma separated list of key values, where the keys are event types (e.g.: creation, oom) or "default" and the value is a duration. Default is applied to all non-specified event types (default "default=0")

- event-storage-event-limit string

    Max number of events to store (per type). Value is a comma separated list of key values, where the keys are event types (e.g.: creation, oom) or "default" and the value is an integer. Default is applied to all non-specified event types (default "default=0")

- event-ttl duration

    Amount of time to retain events. (default 1h0m0s)



### feature

- feature-gates mapStringBool

    A set of key=value pairs that describe feature gates for alpha/experimental features. Options are:
```
APIListChunking=true|false (ALPHA - default=false)
APIResponseCompression=true|false (ALPHA - default=false)
Accelerators=true|false (ALPHA - default=false)
AdvancedAuditing=true|false (BETA - default=true)
AllAlpha=true|false (ALPHA - default=false)
AllowExtTrafficLocalEndpoints=true|false (default=true)
AppArmor=true|false (BETA - default=true)
CPUManager=true|false (ALPHA - default=false)
CustomResourceValidation=true|false (ALPHA - default=false)
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
MountPropagation=true|false (ALPHA - default=false)
PersistentLocalVolumes=true|false (ALPHA - default=false)
PodPriority=true|false (ALPHA - default=false)
RotateKubeletClientCertificate=true|false (BETA - default=true)
RotateKubeletServerCertificate=true|false (ALPHA - default=false)
ServiceNodeExclusion=true|false (ALPHA - default=false)
StreamingProxyRedirects=true|false (BETA - default=true)
SupportIPVSProxyMode=true|false (ALPHA - default=false)
TaintBasedEvictions=true|false (ALPHA - default=false)
TaintNodesByCondition=true|false (ALPHA - default=false)
```

- runtime-config mapStringString

    A set of key=value pairs that describe runtime configuration that may be passed to apiserver. apis/<groupVersion> key can be used to turn on/off specific api versions. apis/<groupVersion>/<resource> can be used to turn on/off specific resources. api/all and api/legacy are special keys to control all and legacy api versions respectively.



### general

- boot-id-file string

    Comma-separated list of files to check for boot-id. Use the first one that exists. (default "/proc/sys/kernel/random/boot_id")

- cors-allowed-origins stringSlice

    List of allowed origins for CORS, comma separated.  An allowed origin can be a regular expression to support subdomain matching. If this list is empty CORS will not be enabled.

- enable-garbage-collector

    Enables the generic garbage collector. MUST be synced with the corresponding flag of the kube-controller-manager. (default true)

- enable-load-reader

    Whether to enable cpu load reader

- enable-swagger-ui

    Enables swagger ui on the apiserver at /swagger-ui

- external-hostname string

    The hostname to use when generating externalized URLs for this master (e.g. Swagger API Docs).

- help

    help for hyperkube

- machine-id-file string

    Comma-separated list of files to check for machine-id. Use the first one that exists. (default "/etc/machine-id,/var/lib/dbus/machine-id")

- master-service-namespace string

    DEPRECATED: the namespace from which the kubernetes master services should be injected into pods. (default "default")

- repair-malformed-updates

    If true, server will do its best to fix the update request to pass the validation, e.g., setting empty UID in update request to its existing value. This flag can be turned off after we fix all the clients that send malformed updates. (default true)

- target-ram-mb int

    Memory limit for apiserver in MB (used to configure sizes of caches, etc.)

- version version[=true]

    Print version information and quit



### kubelet

- kubelet-https

    Use https for kubelet connections. (default true)

- kubelet-preferred-address-types stringSlice

    List of the preferred NodeAddressTypes to use for kubelet connections. (default [Hostname,InternalDNS,InternalIP,ExternalDNS,ExternalIP])

- kubelet-read-only-port uint

    DEPRECATED: kubelet port. (default 10255)

- kubelet-timeout duration

    Timeout for kubelet operations. (default 5s)



### limiter

- default-not-ready-toleration-seconds int

    Indicates the tolerationSeconds of the toleration for notReady:NoExecute that is added by default to every pod that does not already have such a toleration. (default 300)

- default-unreachable-toleration-seconds int

    Indicates the tolerationSeconds of the toleration for unreachable:NoExecute that is added by default to every pod that does not already have such a toleration. (default 300)

- delete-collection-workers int

    Number of workers spawned for DeleteCollection call. These are used to speed up namespace cleanup. (default 1)

- deserialization-cache-size int

    Number of deserialized json objects to cache in memory.

- max-connection-bytes-per-sec int

    If non-zero, throttle each user connection to this number of bytes/sec. Currently only applies to long-running requests.

- max-mutating-requests-inflight int

    The maximum number of mutating requests in flight at a given time. When the server exceeds this, it rejects requests. Zero for no limit. (default 200)

- max-requests-inflight int

    The maximum number of non-mutating requests in flight at a given time. When the server exceeds this, it rejects requests. Zero for no limit. (default 400)

- min-request-timeout int

    An optional field indicating the minimum number of seconds a handler must keep a request open before timing it out. Currently only honored by the watch request handler, which picks a randomized value above this number as the connection timeout, to spread out load. (default 1800)

- request-timeout duration

    An optional field indicating the duration a handler must keep a request open before timing it out. This is the default request timeout for requests but may be overridden by flags such as --min-request-timeout for specific types of requests. (default 1m0s)



### log

- alsologtostderr

    log to standard error as well as files

- enable-logs-handler

    If true, install a /logs handler for the apiserver logs. (default true)

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



### node

- ssh-keyfile string

    If non-empty, use secure SSH proxy to the nodes, using this user keyfile

- ssh-user string

    If non-empty, use secure SSH proxy to the nodes, using this user name



### profiling

- contention-profiling

    Enable lock contention profiling, if profiling is enabled

- profiling

    Enable profiling via web interface host:port/debug/pprof/ (default true)



### secret

- experimental-encryption-provider-config string

    The file containing configuration for encryption providers to be used for storing secrets in etcd



### service

- service-cluster-ip-range ipNet

    A CIDR notation IP range from which to assign service cluster IPs. This must not overlap with any IP ranges assigned to nodes for pods.

- service-node-port-range portRange

    A port range to reserve for services with NodePort visibility. Example: '30000-32767'. Inclusive at both ends of the range. (default 30000-32767)



### storage

- storage-backend string

    The storage backend for persistence. Options: 'etcd3' (default), 'etcd2'.

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

- storage-media-type string

    The media type to use to store objects in storage. Some resources or storage backends may only support a specific media type and will ignore this setting. (default "application/vnd.kubernetes.protobuf")

- storage-versions string

    The per-group version to store resources in. Specified in the format "group1/version1,group2/version2,...". In the case where objects are moved from one group to the other, you may specify the format "group1=group2/v1beta1,group3/v1beta1,...". You only need to pass the groups you wish to change from the defaults. It defaults to a list of preferred versions of all registered groups, which is derived from the KUBE_API_VERSIONS environment variable. (default "admission.k8s.io/v1alpha1,admissionregistration.k8s.io/v1alpha1,apps/v1beta1,authentication.k8s.io/v1,authorization.k8s.io/v1,autoscaling/v1,batch/v1,certificates.k8s.io/v1beta1,componentconfig/v1alpha1,extensions/v1beta1,federation/v1beta1,imagepolicy.k8s.io/v1alpha1,networking.k8s.io/v1,policy/v1beta1,rbac.authorization.k8s.io/v1beta1,scheduling.k8s.io/v1alpha1,settings.k8s.io/v1alpha1,storage.k8s.io/v1,v1")



### tls

- allow-verification-with-non-compliant-keys

    Allow a SignatureVerifier to use keys which are technically non-compliant with RFC6962.

- cert-dir string

    The directory where the TLS certs are located. If --tls-cert-file and --tls-private-key-file are provided, this flag will be ignored. (default "/var/run/kubernetes")

- client-ca-file string

    If set, any request presenting a client certificate signed by one of the authorities in the client-ca-file is authenticated with an identity corresponding to the CommonName of the client certificate.

- kubelet-certificate-authority string

    Path to a cert file for the certificate authority.

- kubelet-client-certificate string

    Path to a client cert file for TLS.

- kubelet-client-key string

    Path to a client key file for TLS.

- proxy-client-cert-file string

    Client certificate used to prove the identity of the aggregator or kube-apiserver when it must call out during a request. This includes proxying requests to a user api-server and calling out to webhook admission plugins. It is expected that this cert includes a signature from the CA in the --requestheader-client-ca-file flag. That CA is published in the 'extension-apiserver-authentication' configmap in the kube-system namespace. Components recieving calls from kube-aggregator should use that CA to perform their half of the mutual TLS verification.

- proxy-client-key-file string

    Private key for the client certificate used to prove the identity of the aggregator or kube-apiserver when it must call out during a request. This includes proxying requests to a user api-server and calling out to webhook admission plugins.

- requestheader-allowed-names stringSlice

    List of client certificate common names to allow to provide usernames in headers specified by --requestheader-username-headers. If empty, any client certificate validated by the authorities in --requestheader-client-ca-file is allowed.

- requestheader-client-ca-file string

    Root certificate bundle to use to verify client certificates on incoming requests before trusting usernames in headers specified by --requestheader-username-headers

- requestheader-extra-headers-prefix stringSlice

    List of request header prefixes to inspect. X-Remote-Extra- is suggested.

- requestheader-group-headers stringSlice

    List of request headers to inspect for groups. X-Remote-Group is suggested.

- requestheader-username-headers stringSlice

    List of request headers to inspect for usernames. X-Remote-User is common.

- tls-ca-file string

    If set, this certificate authority will used for secure access from Admission Controllers. This must be a valid PEM-encoded CA bundle. Altneratively, the certificate authority can be appended to the certificate provided by --tls-cert-file.

- tls-cert-file string

    File containing the default x509 Certificate for HTTPS. (CA cert, if any, concatenated after server cert). If HTTPS serving is enabled, and --tls-cert-file and --tls-private-key-file are not provided, a self-signed certificate and key are generated for the public address and saved to /var/run/kubernetes.

- tls-private-key-file string

    File containing the default x509 private key matching --tls-cert-file.

- tls-sni-cert-key namedCertKey

    A pair of x509 certificate and private key file paths, optionally suffixed with a list of domain patterns which are fully qualified domain names, possibly with prefixed wildcard segments. If no domain patterns are provided, the names of the certificate are extracted. Non-wildcard matches trump over wildcard matches, explicit domain patterns trump over extracted names. For multiple key/certificate pairs, use the --tls-sni-cert-key multiple times. Examples: "example.crt,example.key" or "foo.crt,foo.key:*.foo.com,foo.com". (default [])



### watch

- default-watch-cache-size int

    Default watch cache size. If zero, watch cache will be disabled for resources that do not have a default watch size set. (default 100)

- watch-cache

    Enable watch caching in the apiserver (default true)

- watch-cache-sizes stringSlice

    List of watch cache sizes for every resource (pods, nodes, etc.), comma separated. The individual override format: resource#size, where size is a number. It takes effect when watch-cache is enabled.

