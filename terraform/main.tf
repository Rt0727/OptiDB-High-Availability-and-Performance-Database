provider "aws" {
  region = "us-west-2"
}

resource "aws_rds_cluster" "postgresql_cluster" {
  cluster_identifier      = "pg-ha-cluster"
  engine                 = "aurora-postgresql"
  engine_version         = "13.4"
  master_username        = var.db_username
  master_password        = var.db_password
  database_name          = var.db_name
  backup_retention_period = 7
  skip_final_snapshot    = true
}

resource "aws_rds_cluster_instance" "postgresql_instance" {
  cluster_identifier = aws_rds_cluster.postgresql_cluster.id
  instance_class     = "db.r5.large"
  engine             = aws_rds_cluster.postgresql_cluster.engine
  engine_version     = aws_rds_cluster.postgresql_cluster.engine_version
  publicly_accessible = false
}

resource "aws_security_group" "db_sg" {
  name_prefix = "pg-ha-db-sg"
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_rds_cluster_parameter_group" "postgresql_params" {
  name        = "pg-ha-cluster-params"
  family      = "aurora-postgresql13"
  description = "Aurora PostgreSQL Cluster Parameters"
  parameter{
    name  = "max_connections"
    value = "200"
  }
}