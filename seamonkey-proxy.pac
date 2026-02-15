function FindProxyForURL(url, host) {
    // Specify SOCKS5 proxy
    var socksProxy = "SOCKS5 127.0.0.1:1111";
    var socksProxy1 = "SOCKS5 127.0.0.1:2222";

    // List of sites => proxy
    var proxyConfig = {
        "domain1.org": socksProxy,
        "domain2.net": socksProxy1
    };

    for (var domain in proxyConfig) {
        if (dnsDomainIs(host, domain)) {
            return proxyConfig[domain];
        }
    }

    // Use direct connection for all other sites
    return "DIRECT";
}
