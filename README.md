Here is the updated **README.md** reflecting the changes to include Python scripts for managing PostgreSQL high availability, backups, and failover, alongside the Terraform and Docker setup:

---

# OptiDB: High Availability and Performance Database

## Overview  
This repository provides an automated setup for a highly available and optimized PostgreSQL database system. The setup features failover mechanisms, connection pooling, load balancing, automated backups, and health monitoring to ensure seamless performance and high uptime. Docker is used for containerization, and Terraform is employed for Infrastructure as Code (IaC). Python is used to automate database management, backups, and failover operations.

## Features  
- **High Availability**: Implements failover support to maintain continuous database uptime.  
- **Optimized Performance**: Includes connection pooling and load balancing using `pgpool`.  
- **Automated Backups**: Ensures database backups are taken regularly and securely stored.  
- **Disaster Recovery**: Features automated failover and recovery scripts for quick restoration.  
- **Health Monitoring**: Python-based health checks to monitor the status of PostgreSQL nodes (primary and replicas).  
- **Containerized Environment**: Uses Docker for a consistent and portable setup.  

## Technologies Used  
- **Database**: PostgreSQL with `pgpool` for load balancing.  
- **Containerization**: Docker, Docker Compose.  
- **IaC**: Terraform for cloud-based or local resource management.  
- **Automation**: Python for database management, backups, failover handling, and health checks.  
- **Bash Scripts**: For routine tasks like backups and failover simulations.

| Technology                       | Purpose                              |
|-----------------------------------|--------------------------------------|
| **PostgreSQL with `pgpool`**      | Database for high availability and performance |
| **Docker**                        | Containerization                     |
| **Terraform**                     | Infrastructure provisioning          |
| **Python**                        | Automation for database management, backups, failover, health checks |
| **Bash Scripts**                  | Automation of routine tasks          |

## Prerequisites  
- Install [Docker](https://www.docker.com/)  
- Install [Terraform](https://www.terraform.io/)  
- Install [Git](https://git-scm.com/)  
- Install [Python](https://www.python.org/) and [psycopg2](https://pypi.org/project/psycopg2/)  
- Basic knowledge of Bash, PostgreSQL, and Python.  

## Setup Instructions  

### 1. Clone the Repository  
Clone this repository to your local machine and navigate into the directory:  
```bash  
git clone https://github.com/Rt0727/OptiDB-High-Availability-and-Performance-Database.git  
cd OptiDB-High-Availability-and-Performance-Database  
```  

### 2. Configure Terraform Variables  
Create a `.tfvars` file in the `terraform/` directory with the following contents:  
```hcl  
db_cluster_name     = "optidb_cluster"  
db_port             = 5432  
db_username         = "optidb_user"  
db_password         = "secure_password"  
backup_bucket       = "your_backup_bucket_name"  
pgpool_max_pool     = 100  
pgpool_health_check = 10  
```  

### 3. Initialize and Deploy Infrastructure  
Use Terraform to initialize and deploy the PostgreSQL cluster:  
```bash  
cd terraform  
terraform init  
terraform apply -var-file="variables.tfvars"  
```  
This will provision the PostgreSQL cluster resources and output database connection details.  

### 4. Build and Start Docker Containers  
Navigate back to the root directory and build the Docker containers:  
```bash  
docker-compose up --build  
```  
This will:  
- Start the PostgreSQL cluster and `pgpool` container for load balancing.  
- Configure the database with the desired high-availability setup.  

### 5. Test Failover and Recovery  
Simulate a failover scenario using the provided `failover.sh` script:  
```bash  
./scripts/failover.sh  
```  
This script tests the failover mechanism and ensures automatic recovery.  

### 6. Automate Backups  
Automate database backups with the `backup.sh` script:  
```bash  
./scripts/backup.sh  
```  
This script creates and securely stores backups of the PostgreSQL database.  

### 7. Manage Database with Python Scripts  
In addition to the Bash scripts, you can use Python scripts to automate tasks such as failover, backups, and health monitoring. You can find the Python scripts in the `python/` directory. Some key Python operations are:

- **Backup Management**: Run `python/python/backup_manager.py` to automate backups.
- **Failover Management**: Use `python/python/failover_manager.py` to manage failover.
- **Health Monitoring**: Use `python/python/health_check.py` for continuous health checks of the PostgreSQL nodes.

## Project Structure  
```plaintext  
high-availability-db-setup/  
│  
├── terraform/  
│   ├── main.tf                    # Defines PostgreSQL cluster resources  
│   ├── variables.tf               # Contains variable definitions  
│   └── outputs.tf                 # Outputs database connection details  
│  
├── docker/  
│   ├── Dockerfile                 # Dockerfile for PostgreSQL and pgpool setup  
│   └── docker-compose.yml         # Docker Compose file for HA setup  
│  
├── python/  
│   ├── db_manager.py              # Manages PostgreSQL cluster (primary & replica)  
│   ├── backup_manager.py          # Automates backups for PostgreSQL  
│   ├── failover_manager.py        # Automates failover and recovery  
│   ├── health_check.py            # Monitors PostgreSQL node health  
│   └── tests/  
│       ├── test_db_manager.py     # Unit tests for database management  
│       ├── test_backup_manager.py # Unit tests for backup management  
│       └── test_failover_manager.py # Unit tests for failover management  
│  
├── scripts/  
│   ├── backup.sh                  # Backup script for PostgreSQL  
│   └── failover.sh                # Failover and recovery simulation script  
│  
├── README.md                      # Documentation  
└── .gitignore                     # Git ignore file  
```  

## Troubleshooting  

### Common Issues  
1. **Terraform Errors**: Ensure Terraform is installed and the `variables.tfvars` file is correctly configured.  
2. **Docker Issues**: Verify Docker is running and containers are properly configured.  
3. **Connection Issues**: Check `pgpool` and PostgreSQL container logs for errors.  

### Logs  
Access logs for debugging:  
- PostgreSQL logs: Run `docker-compose logs db`  
- `pgpool` logs: Run `docker-compose logs pgpool`  

## Future Enhancements  
- Implement query optimization for complex analytics workloads.  
- Integrate monitoring tools such as Prometheus and Grafana for real-time metrics.  
- Add role-based access control to enhance security.  
- Expand failover mechanisms for multi-region deployment.  

```  

For any questions or issues, feel free to reach out at `rt07mahifan@gmail.com`.

```