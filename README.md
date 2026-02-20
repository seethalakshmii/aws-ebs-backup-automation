<u>PROJECT: AUTOMATED EBS BACKUP</u>

<u>GOAL</u>
Automate EBS snapshots using AWS Lambda and Python (Boto3) to ensure data recovery via resource tagging.

<u>TECH STACK</u>

Cloud: AWS (EC2, Lambda, CloudWatch)

Runtime: Python 3.12

Security: IAM Roles (Keyless)

<u>KEY CAPABILITIES</u>

Tag-Driven: Backs up only instances tagged Backup: True.

Automated: Eliminates manual snapshots with event-driven logic.

Secure: Operates via least-privilege IAM permissions.

<u>WORKFLOW</u>

Provision: Launched Instance i-00850dc6016df70cf with required tags.

Authorize: Created IAM Policy for EC2 Snapshot and CloudWatch access.

Execute: Deployed Python script to Lambda to trigger backups.

Verify: Confirmed success via CloudWatch logs and EC2 Console.

<u>PROJECT STATUS</u>

Instance ID: i-00850dc6016df70cf

Result: SUCCESS (Verified)
