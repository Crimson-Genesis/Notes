# SSH:- 
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
# Then all Public key to the your github account.

```

# GPG:- 
```bash
gpg --full-generate-key
gpg --default-new-key-algo rsa4096 --gen-key (if version bellow '2.1.17')
gpg --list-secret-keys --keyid-format=long
# Output will be something like this:-
"
$ gpg --list-secret-keys --keyid-format=long
/Users/hubot/.gnupg/secring.gpg
------------------------------------
sec   4096R/3AA5C34371567BD2 2016-03-10 [expires: 2017-03-10]
uid                          Hubot <hubot@example.com>
ssb   4096R/4BB6D45482678BE3 2016-03-10
"
# the GPG key ID is 3AA5C34371567BD2

gpg --armor --export 3AA5C34371567BD2
# Prints the GPG key ID, in ASCII armor format
# Then GPG begins with -----BEGIN PGP PUBLIC KEY BLOCK----- and ending with -----END PGP PUBLIC KEY BLOCK-----

# Then add the gpg key to your github account.


```
