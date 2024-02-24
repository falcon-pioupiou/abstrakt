region = "eu-west-2"
cluster_name = "eks-lon-managed-node"
vpc_name = "managed-containers"
vpc_cidr = "10.0.0.0/16"
subnet_count = "3"
private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
public_subnets = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
cluster_version = "1.28"
ami_type = "AL2_x86_64"
common_tags = {"cstag-owner": "njoshi02", "cstag-product": "Falcon", "cstag-accounting": "dev", "cstag-department": "Sales - 310000", "cstag-business": "Sales"}
eks_managed_node_groups = {"group1": {"name": "node-group-1", "instance_types": ["t3.small"], "min_size": "1", "max_size": "3", "desired_size": "2"}, "group2": {"name": "node-group-2", "instance_types": ["t3.small"], "min_size": "1", "max_size": "3", "desired_size": "2"}}
