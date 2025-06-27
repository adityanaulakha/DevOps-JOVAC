import boto3

def create_ec2_instance():
    ec2 = boto3.resource('ec2', region_name="eu-north-1")  

    # Launch EC2 instance
    instances = ec2.create_instances(
        ImageId="ami-042b4708b1d05f512",  
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.micro",  
        KeyName="test",  
        SecurityGroupIds=["sg-048cc533262f69b7f"],  
        SubnetId="subnet-05a7a2bfdaa829a13",  
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'TEST'}  
                ]
            }
        ]
    )
    print('Created Instance')

if __name__ == '__main__':
    create_ec2_instance()


    