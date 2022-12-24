import subprocess
import csv

# Define the path to the gam executable
gam = "PATH TO GAM"

# Open the input CSV file
with open("./users.csv", 'r') as f:
    # Create a reader to read the input CSV file
    reader = csv.DictReader(f)

    # Open the output CSV file
    with open("./gmailprofiles.csv", 'w') as y:
        # Write the header row to the output CSV file
        y.write("emailAddress,historyId,messagesTotal,threadsTotal\n")

        # Iterate over the rows in the input CSV file
        for row in reader:
            # Retrieve the email address from the row
            email = row['email']

            # Construct the gam command
            command = [gam, "user", email, "print", "gmailprofile"]

            # Run the gam command and capture the output
            result = subprocess.run(command, stdout=subprocess.PIPE, check=True)

            # Split the output into a list of fields
            fields = result.stdout.decode("utf-8").strip().split(",")

            # Write the fields to the output CSV file without a newline character at the end
            y.write(",".join(fields))