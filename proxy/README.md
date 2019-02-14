a proxy impl over python/go/cpp for proxy tunnel with traffic obfs
repo: ss,ss-go,ss-qt5

e.g. for `go`:
```
func (d *Dialer) Dial(network, addr string) (c net.Conn, err error) {
	if strings.HasPrefix(network, "tcp") {
		conn, err := Dial(addr, d.server, d.cipher.Copy())
		if err != nil {
			return nil, err
		}
		return &ProxyConn {
			Conn: conn,
			raddr: &ProxyAddr {
				network: network,
				address: addr,
			},
		}, nil
	}
	return nil, fmt.Errorf("unsupported connection type: %s", network)
}
```

