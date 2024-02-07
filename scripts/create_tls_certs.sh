SUBJECT="/C=US/ST=CO/L=Denver/O=Imaige/OU=MediaViz/CN=my-alias/emailAddress=caleb@imaige.com"
SAN="DNS:a9ffa50f4239140f1a19f8b8e811593a-1537691390.us-east-2.elb.amazonaws.com"

# Generate CA key and certificate
openssl genpkey -algorithm RSA -out ca-key.pem
openssl req -x509 -new -key ca-key.pem -out ca-cert.pem -subj "${SUBJECT}"

# Generate server key and certificate with SAN
openssl genpkey -algorithm RSA -out server-key.pem
openssl req -new -key server-key.pem -out server-csr.pem -subj "${SUBJECT}" -reqexts SAN -config <(cat /etc/ssl/openssl.cnf <(printf "[SAN]\nsubjectAltName=${SAN}"))
openssl x509 -req -in server-csr.pem -CA ca-cert.pem -CAkey ca-key.pem -out server-cert.pem -days 365 -extfile <(printf "subjectAltName=${SAN}")

# Generate client key and certificate
openssl genpkey -algorithm RSA -out client-key.pem
openssl req -new -key client-key.pem -out client-csr.pem -subj "${SUBJECT}"
openssl x509 -req -in client-csr.pem -CA ca-cert.pem -CAkey ca-key.pem -out client-cert.pem -days 365

# TODO future:
# 1) take user input for SUBJECT and SAN params
# 2) automatically move files to another directory
# 3) take user input for name (and location, although for now we can at least assume ../tls_certs/$name) of directory