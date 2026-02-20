PROJECT: AUTOMATED EBS SNAPSHOT SCHEDULING

# OVERVIEW
This project uses AWS Lambda and Python (Boto3) to automate EBS backups. It identifies specific EC2 instances via tags and creates point-in-time snapshots for disaster recovery.

# TECH STACK
Cloud: Amazon Web Services (AWS)
Compute: Lambda (Serverless)
Language: Python 3.12 (Boto3)
Security: IAM Roles (Keyless)

# CORE FEATURES

Tag-Based: Only targets instances with the "Backup: True" tag.
Secure: Uses IAM Roles instead of manual access keys.
Automated: Creates timestamped snapshots without manual intervention.

# IMPLEMENTATION STEPS

Resource Setup: Launched EC2 instance i-00850dc6016df70cf with backup tags.
IAM Security: Configured a policy for EC2 snapshot and CloudWatch permissions.
Automation: Deployed Python logic to Lambda to scan and backup volumes.
Verification: Confirmed snapshot creation via CloudWatch and EC2 Console.

# FINAL RESULTS
Target Instance: i-00850dc6016df70cf
Status: Verified Success
Documentation: Full step-by-step proof included in the attached report.
