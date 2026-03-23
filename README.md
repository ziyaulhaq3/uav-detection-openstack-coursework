# UAV Detection on OpenStack
YOLOv8 drone detection system deployed on OpenStack cloud.

## OpenStack Services
- Nova: VM compute instances
- Neutron: Network with floating IPs
- Glance: VM image storage
- Keystone: Identity and authentication

## CI/CD Pipeline
1. Push code to GitHub
2. GitHub Actions runs tests
3. Builds and validates API
4. Deploys to OpenStack VM

## Module: CSI_7_FIT - Future Internet Technologies - LSBU
