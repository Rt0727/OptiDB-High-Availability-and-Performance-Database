output "db_cluster_endpoint" {
  value = aws_rds_cluster.postgresql_cluster.endpoint
}

output "db_instance_endpoint" {
  value = aws_rds_cluster_instance.postgresql_instance.endpoint
}