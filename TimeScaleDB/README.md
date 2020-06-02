#  TimeScaleDB工作记录
## TimeScaleDB 安装流程(参考文档https://docs.timescale.com/v1.2/getting-started/installation/rhel-centos/installation-yum )：
            
            yum install -y https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
            tee /etc/yum.repos.d/timescale_timescaledb.repo <<EOL
            [timescale_timescaledb]
            name=timescale_timescaledb
            baseurl=https://packagecloud.io/timescale/timescaledb/el/7/\$basearch
            repo_gpgcheck=1
            gpgcheck=0
            enabled=1
            gpgkey=https://packagecloud.io/timescale/timescaledb/gpgkey
            sslverify=1
            sslcacert=/etc/pki/tls/certs/ca-bundle.crt
            metadata_expire=300
            EOL
            yum update -y
            
## 安装timescaledb-postgresql-11并添加环境变量

            # Now install appropriate package for PG version
            yum install -y timescaledb-postgresql-11
            
            # Add the env path 
            export PATH=/usr/pgsql-11/bin:$PATH
            
## 初始化数据库

            # Initialize the database
            # From https://wiki.postgresql.org/wiki/YUM_Installation
            /usr/pgsql-11/bin/postgresql-11-setup initdb
            
            # Configure your database
            # Saving changes to: /var/lib/pgsql/11/data/postgresql.conf
            timescaledb-tune
            
            #To get started you'll need to restart PostgreSQL and add a postgres superuser
            systemctl restart postgresql-11.service
            
## 连接数据库并创建新得数据库            

            # connect to database
            sudo -u postgres psql -d <databasename>
            # Create the database, let's call it 'tutorial'
            CREATE database tutorial;
            # Connect to the database
            \c tutorial
            # Extend the database with TimescaleDB
            CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;
            # Connecting to the new database is as simple as:
            psql -U postgres -h localhost -d tutorial
            
