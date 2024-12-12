#!/bin/bash

# Check if the primary database is available
MASTER_STATUS=$(pg_isready -h localhost -p 5432)

if [ "$MASTER_STATUS" != "accepting connections" ]; then
  echo "Master database is down, initiating failover..."

  # Promote the slave to master
  docker exec -it db-slave pg_ctl promote -D /var/lib/postgresql/data

  # Update any application settings to point to the new master
  echo "Failover complete. New master is db-slave."
else
  echo "Master database is up and running."
fi