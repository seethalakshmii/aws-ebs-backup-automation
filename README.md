<u>PROJECT: AUTOMATED EBS SNAPSHOT SCHEDULING</u>

<u>OVERVIEW</u>
This project uses AWS Lambda and Python (Boto3) to automate EBS backups. It identifies specific EC2 instances via tags and creates point-in-time snapshots for disaster recovery.

<u>TECH STACK</u>
Cloud: Amazon Web Services (AWS)
Compute: Lambda (Serverless)
Language: Python 3.12 (Boto3)
Security: IAM Roles (Keyless)

<u>CORE FEATURES</u>

Tag-Based: Only targets instances with the "Backup: True" tag.

Secure: Uses IAM Roles instead of manual access keys.

Automated: Creates timestamped snapshots without manual intervention.

<u>IMPLEMENTATION STEPS</u>

Resource Setup: Launched EC2 instance i-00850dc6016df70cf with backup tags.

IAM Security: Configured a policy for EC2 snapshot and CloudWatch permissions.

Automation: Deployed Python logic to Lambda to scan and backup volumes.

Verification: Confirmed snapshot creation via CloudWatch and EC2 Console.

<u>FINAL RESULTS</u>
Target Instance: i-00850dc6016df70cf
Status: Verified Success
Documentation: Full step-by-step proof included in the attached report.
