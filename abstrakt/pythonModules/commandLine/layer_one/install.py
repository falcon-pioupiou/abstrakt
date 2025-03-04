import typer
import pytz

from datetime import datetime
from typing_extensions import Annotated

from abstrakt.pythonModules.opsManager.CrowdStrikeSensorOperationsManager import CrowdStrikeSensorOperationsManager
from abstrakt.pythonModules.customLogging.customLogging import CustomLogger

uk_timezone = pytz.timezone('Europe/London')
uk_time = datetime.now(uk_timezone)
uk_time_str = uk_time.strftime('%d%m%Y')

runtime_sensor_app = typer.Typer()


@runtime_sensor_app.command(rich_help_panel='CrowdStrike Sensors')
def crowdstrike(
  falcon_sensor: Annotated[bool, typer.Option('--falcon-sensor',
                                              help='Install Falcon Sensor',
                                              rich_help_panel='CrowdStrike EDR Sensor',
                                              show_default=False)] = False,
  kernel_mode: Annotated[bool, typer.Option('--kernel-mode', help='Install Falcon Sensor in Kernel mode',
                                            rich_help_panel='CrowdStrike EDR Sensor Options',
                                            show_default=False)] = False,
  ebpf_mode: Annotated[bool, typer.Option('--ebpf-mode', help='Install Falcon Sensor in ebpf mode',
                                          rich_help_panel='CrowdStrike EDR Sensor Options',
                                          show_default=False)] = False,
  monitor_namespaces: Annotated[str, typer.Option('--monitor-namespaces',
                                                  help='Namespaces to monitor to inject falcon sensor '
                                                       '| Example: All or ns1,ns2,ns3',
                                                  rich_help_panel='CrowdStrike EDR Sensor Options')] = 'All',
  exclude_namespaces: Annotated[str, typer.Option('--exclude-namespaces',
                                                  help='Namespaces to exclude from falcon sensor injection '
                                                       '| Example: ns1,ns2,ns3',
                                                  rich_help_panel='CrowdStrike EDR Sensor Options',
                                                  show_default=False)] = None,
  falcon_image_repo: Annotated[str, typer.Option('--falcon-image-repo', help='Falcon Sensor Image Repository | '
                                                 'Example: 123456789012.dkr.ecr.eu-west-2.amazonaws.com/ecr',
                                                 rich_help_panel="CrowdStrike EDR Sensor Options")] = None,
  falcon_image_tag: Annotated[str, typer.Option('--falcon-image-tag', help='Falcon Sensor Image Tag | '
                                                                           'Example: 7.10.0-16303-1.falcon-linux'
                                                                           '.x86_64.Release.US-1',
                                                rich_help_panel="CrowdStrike EDR Sensor Options",
                                                show_default=False)] = None,
  proxy_server: Annotated[str, typer.Option('--proxy-server', help='Proxy Server IP or FQDN | '
                                                                   'Example: 10.10.10.10 OR proxy.internal.com',
                                            rich_help_panel="CrowdStrike EDR Sensor Options",
                                            show_default=False)] = None,
  proxy_port: Annotated[str, typer.Option('--proxy-port', help='Proxy Server Port | Example: 8080',
                                          rich_help_panel="CrowdStrike EDR Sensor Options",
                                          show_default=False)] = None,
  falcon_sensor_tags: Annotated[str, typer.Option('--falcon-sensor-tags', help='Falcon Sensor Tags | '
                                                                               'Example: Tag1,Tag2',
                                                  rich_help_panel="CrowdStrike EDR Sensor Options",
                                                  show_default=False)] = None,
  # cloud_provider: Annotated[str, typer.Option('--cloud-provider',
  #                                             help='Cloud Service Provider [aws | azure | gcp]',
  #                                             rich_help_panel='Cloud Service Provider Options',
  #                                             show_default=False)] = None,
  # cluster_type: Annotated[str, typer.Option('--cluster-type',
  #                                           help='Cluster Type [eks-managed-node | eks-self-managed-node | '
  #                                                'eks-fargate | aks | gke-standard | gke-autopilot]',
  #                                           rich_help_panel='Cloud Service Provider Options',
  #                                           show_default=False)] = None,
  aws_cluster_name: Annotated[str, typer.Option('--aws-cluster-name',
                                                help='Cluster Name',
                                                rich_help_panel='AWS Options',
                                                show_default=False)] = None,
  aws_region: Annotated[str, typer.Option('--aws-region', help='Cluster Region or Zone',
                                          rich_help_panel='AWS Options',
                                          show_default=False)] = None,
  azure_cluster_name: Annotated[str, typer.Option('--azure-cluster-name',
                                                  help='Cluster Name',
                                                  rich_help_panel='Azure Options',
                                                  show_default=False)] = None,
  azure_resource_group_name: Annotated[str, typer.Option('--azure-resource-group-name',
                                                         help='Azure Resource Group Name',
                                                         rich_help_panel='Azure Options',
                                                         show_default=False)] = None,
  gcp_cluster_name: Annotated[str, typer.Option('--gcp-cluster-name',
                                                help='GCP Cluster Name',
                                                rich_help_panel='GCP Options',
                                                show_default=False)] = None,
  gcp_region: Annotated[str, typer.Option('--gcp-region', help='Cluster Region or Zone',
                                          rich_help_panel='GCP Options',
                                          show_default=False)] = None,
  gcp_project_id: Annotated[str, typer.Option('--gcp-project-name', help='GCP Project Name',
                                              rich_help_panel='GCP Options',
                                              show_default=False)] = None,
  kpa: Annotated[bool, typer.Option('--kpa',
                                    help='Install Kubernetes Protection Agent',
                                    rich_help_panel='CrowdStrike Kubernetes Agents',
                                    show_default=False)] = False,
  kac: Annotated[bool, typer.Option('--kac',
                                    help='Install Kubernetes Admission Controller',
                                    rich_help_panel='CrowdStrike Kubernetes Agents',
                                    show_default=False)] = False,
  iar: Annotated[bool, typer.Option('--iar',
                                    help='Install Image Assessment at Runtime',
                                    rich_help_panel='CrowdStrike Kubernetes Agents',
                                    show_default=False)] = False,
  detections_container: Annotated[bool, typer.Option('--detections-container',
                                                     help='Install CrowdStrike Detections Container',
                                                     rich_help_panel='CrowdStrike Artificial '
                                                                     'Detections Generator',
                                                     show_default=False)] = False,
  vulnerable_apps: Annotated[bool, typer.Option('--vulnerable-apps',
                                                help='Install Vulnerable Apps',
                                                rich_help_panel='CrowdStrike Artificial '
                                                                'Detections Generator',
                                                show_default=False)] = False,
  falcon_client_id: Annotated[str, typer.Option('--falcon-client-id',
                                                help='Client ID to Install Falcon Sensor | Example: QWERT',
                                                rich_help_panel='CrowdStrike API Keys',
                                                show_default=False)] = None,
  falcon_client_secret: Annotated[str, typer.Option('--falcon-client-secret',
                                                    help='Client Secret to Install Falcon Sensor | Example: QWERT',
                                                    rich_help_panel='CrowdStrike API Keys',
                                                    show_default=False)] = None,
  ecr_iam_policy_name: Annotated[str, typer.Option('--ecr-iam-policy-name', help='AWS IAM Policy Name [EKS Fargate '
                                                                                 'Only]',
                                                   rich_help_panel='AWS Options')] = 'CrowdStrikeFalconContainerEcrPull',
  ecr_iam_role_name: Annotated[str, typer.Option('--ecr-iam-role-name', help='AWS IAM Role Name [EKS Fargate Only]',
                                                 rich_help_panel='AWS Options')] = 'CrowdStrikeFalconContainerIAMRole'
):
  crwd_sensor_log_filename = f'/var/log/crowdstrike/sensors/sensor-{uk_time_str}.log'
  crwd_sensor_logger = CustomLogger(__name__, crwd_sensor_log_filename).logger

  manager = CrowdStrikeSensorOperationsManager(falcon_sensor=falcon_sensor,
                                               kernel_mode=kernel_mode,
                                               ebpf_mode=ebpf_mode,
                                               monitor_namespaces=monitor_namespaces,
                                               exclude_namespaces=exclude_namespaces,
                                               falcon_image_repo=falcon_image_repo,
                                               falcon_image_tag=falcon_image_tag,
                                               proxy_server=proxy_server,
                                               proxy_port=proxy_port,
                                               falcon_sensor_tags=falcon_sensor_tags,
                                               aws_region=aws_region,
                                               aws_cluster_name=aws_cluster_name,
                                               azure_resource_group_name=azure_resource_group_name,
                                               azure_cluster_name=azure_cluster_name,
                                               gcp_region=gcp_region,
                                               gcp_cluster_name=gcp_cluster_name,
                                               gcp_project_id=gcp_project_id,
                                               kpa=kpa,
                                               kac=kac,
                                               iar=iar,
                                               detections_container=detections_container,
                                               vulnerable_apps=vulnerable_apps,
                                               falcon_client_id=falcon_client_id,
                                               falcon_client_secret=falcon_client_secret,
                                               ecr_iam_policy_name=ecr_iam_policy_name,
                                               ecr_iam_role_name=ecr_iam_role_name,
                                               logger=crwd_sensor_logger)

  manager.start_crowdstrike_sensor_operations()
