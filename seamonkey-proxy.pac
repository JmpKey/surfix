function FindProxyForURL(url, host) {
    // Specify SOCKS5 proxy
    var socksProxy = "SOCKS5 127.0.0.1:1111";

    // List of sites to proxy
    var proxySites = [
        "domain1.org",
        "domain2.net"
    ];

    for (var i = 0; i < proxySites.length; i++) {
        if (dnsDomainIs(host, proxySites[i])) {
            return socksProxy;
        }
    }

    // Use direct connection for all other sites
    return "DIRECT";
}
