FROM postgres:13

# Copy custom configuration files
COPY ./postgresql.conf /etc/postgresql/postgresql.conf

# Set the default command to run PostgreSQL
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]