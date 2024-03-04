# create_tls_certs.sh

# Take user input for new directory name
read -p "Enter the name for the new directory where certs will be stored: " dir_name

# Take user input for existing directory location and validate
# While package is structured as-is, this will usually be "../tls_certs"
dir_location="../tls_certs"
while true; do
    read -p "Enter the existing directory location (relative or absolute path; leave blank for default): " dir_location
    # Convert relative path to absolute path
    dir_location=$(realpath "$dir_location")
    if [ -d "$dir_location" ]; then
        break
    else
        echo "Directory does not exist. Please enter a valid directory location."
    fi
done

# Check if the directory with the same name already exists
target_dir="$dir_location/$dir_name"
if [ -d "$target_dir" ]; then
    echo "Directory with the name '$dir_name' already exists. Certificates will be moved to this directory, overwriting existing certificates if any."
else
    # Create the new directory
    mkdir -p "$target_dir"
fi

SUBJECT="/C=US/ST=CO/L=Denver/O=Imaige/OU=MediaViz/CN=my-alias/emailAddress=caleb@imaige.com"
SAN="DNS:DNS:localhost, IP:127.0.0.1"

# Create SAN config file
SAN_CONFIG_FILE="$target_dir/san_config.cnf"
echo "[SAN]" > "$SAN_CONFIG_FILE"
echo "subjectAltName=${SAN}" >> "$SAN_CONFIG_FILE"

# Generate CA key and certificate
openssl genpkey -algorithm RSA -out "$target_dir/ca-key.pem"
openssl req -x509 -new -key "$target_dir/ca-key.pem" -out "$target_dir/ca-cert.pem" -subj "${SUBJECT}"

# Generate server key and certificate with SAN
openssl genpkey -algorithm RSA -out "$target_dir/server-key.pem"
openssl req -new -key "$target_dir/server-key.pem" -out "$target_dir/server-csr.pem" -subj "${SUBJECT}" -reqexts SAN -config "$SAN_CONFIG_FILE"
openssl x509 -req -in "$target_dir/server-csr.pem" -CA "$target_dir/ca-cert.pem" -CAkey "$target_dir/ca-key.pem" -out "$target_dir/server-cert.pem" -days 365 -extfile "$target_dir/san_config.cnf"

# Generate client key and certificate
openssl genpkey -algorithm RSA -out "$target_dir/client-key.pem"
openssl req -new -key "$target_dir/client-key.pem" -out "$target_dir/client-csr.pem" -subj "${SUBJECT}"
openssl x509 -req -in "$target_dir/client-csr.pem" -CA "$target_dir/ca-cert.pem" -CAkey "$target_dir/ca-key.pem" -out "$target_dir/client-cert.pem" -days 365

echo "Certificates and keys generated and moved to $target_dir"

# Clean up temporary files
rm "$SAN_CONFIG_FILE"

# TODO future:
# 1) take user input for SUBJECT and SAN params
