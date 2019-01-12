xxtea-py

uses a header for the encryption/decryption data

```
>>> enc2 = xxtea.encrypt(text, "key1")
>>> enc2
b'\xadJ\xed=\xe8\x81\x0b\xb0\x99\x01\xce\x04iy\xe94'
>>> len(enc2)
16
>>> len(text)
8
>>> enc3 = xxtea.encrypt(enc2, "key1")
>>> enc3
b' \x97\x85\xaa\xa7\x13\x1b7\x15o\x97\xb9\xbf\xd5\xad\xb8\xa7S*^'
>>> len(enc3)
20
```

which is not nice for hidden;
