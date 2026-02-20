import boto3 
import datetime 
 
# Initialize the EC2 client 
ec2 = boto3.client('ec2') 
 
def lambda_handler(event, context): 
    # Your specific Instance ID 
    target_instance_id = 'i-00850dc6016df70cf' 
     
    print(f"Starting automated backup for instance: {target_instance_id}") 
     
    try: 
        # 1. Get details about the instance and its volumes 
        instance_data = ec2.describe_instances(InstanceIds=[target_instance_id]) 
         
        for reservation in instance_data['Reservations']: 
            for instance in reservation['Instances']: 
                # 2. Loop through all volumes (EBS) attached to this instance 
                for device in instance['BlockDeviceMappings']: 
                    volume_id = device['Ebs']['VolumeId'] 
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d 
%H:%M:%S") 
                     
                    # 3. Create the actual Snapshot 
                    description = f"Automated Backup of {target_instance_id} - 
{timestamp}" 
                    snapshot = ec2.create_snapshot( 
                        VolumeId=volume_id,  
                        Description=description 
                    ) 
                     
                    # 4. Add a Name tag to the snapshot for your report 
                    ec2.create_tags( 
                        Resources=[snapshot['SnapshotId']], 
                        Tags=[{'Key': 'Name', 'Value': f"Backup
{target_instance_id}"}] 
                    ) 
                     
                    print(f"Success! Created Snapshot ID: 
{snapshot['SnapshotId']} for Volume: {volume_id}") 
                     
    except Exception as e: 
        print(f"Error occurred: {str(e)}") 
        raise e 
