### AWS credentials: ####
# Change entries here to match your own #
# Get values for the first two entries from the "Security crediential" Tab
# Under in the menu under your name.
aws_access_key_id='AKIAJ7TG5BXBG255MTYA'
aws_secret_access_key='JUNazh2k1KkApRvCxoV1EfujlUZk8eexc9odcGsF'
# Get the Keypair in the EC2 Dashboard page.
keyPairFile="/Users/apple/UCSD_BigData/LocalScripts/tryandtry.pem" # name of file keeping local key
key_name="tryandtry" # name of keypair (not name of file where key is stored)
# Set the security group On the EC2 page (You will need to add IP addresses if
# you want to connect from a place previously unauthorized.
security_groups=['launch-wizard-1']
### End of AWS credentials ####
