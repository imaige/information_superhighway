kubectl delete secret tls-certs
kubectl create secret generic tls-certs --from-file=./server-key.pem --from-file=./server-cert.pem --from-file=ca-cert.pem --from-file=client-key.pem --from-file=client-cert.pem

# TODO future:
# 1) update file pathing to be smarter - either take input, or know whether to run either on current dir or on ../tls_certs/k8s