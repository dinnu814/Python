import boto3
session=boto3.session.Session(profile_name="default")
ec2_console_resource=session.resource(service_name="ec2",region_name="us-east-1")
#print(dir(ec2_console_resource))
instance_id=input("Enter your instance id for the status: ")
my_instance=ec2_console_resource.Instance(id=instance_id)
print(my_instance.state['Name'])
