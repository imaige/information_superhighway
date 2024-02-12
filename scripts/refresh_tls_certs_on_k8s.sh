# refresh_tls_certs_on_k8s.sh
# requirements: installed AWS CLI & successful authentication - includes:
# a) AWS user registration to ConfigMap in EKS, and
# b) registry auth, see 'Authenticate to your default registry' here:
# https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html

# Get user input for secret_name
read -p "Enter the name of the secret: " secret_name

# Get user input for the relative path to the folder containing k8s certificates
# While package is structured as-is, this will usually be '../tls_certs/k8s'
read -p "Enter the relative path to the folder containing certificates: " cert_folder

# Check if the secret exists
if kubectl get secret "$secret_name" &> /dev/null; then
    # If the secret exists, delete it
    echo "Deleting existing secret $secret_name..."
    kubectl delete secret "$secret_name"
fi

#kubectl delete secret tls-certs

# Create the new secret
echo "Creating new secret named $secret_name..."
kubectl create secret generic "$secret_name" --from-file="$cert_folder/server-key.pem" --from-file="$cert_folder/server-cert.pem" --from-file="$cert_folder/ca-cert.pem" --from-file="$cert_folder/client-key.pem" --from-file="$cert_folder/client-cert.pem"
