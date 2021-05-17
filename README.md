# zabbix-aws
update from :	https://github.com/wawastein/zabbix-cloudwatch

Cloudwatch integration for Zabbix 5.2, Python 3.6.x  (tested on Centos 8)

1) clone repository
2) copy contents of direcotry 'scripts' to /usr/share/zabbix/
3) chmod +x /usr/share/zabbix/scripts -R
4) install 'boto3' (dnf install python3-pip -y && pip install boto3)
5) Import tempalte 'cloudwatch_template.xml' (from web GUI Zabbix)
6) Set credentials account (user, key and secrete) on : '/usr/share/zabbix/scripts/conf/aws.conf' 
7) Create host with interface 0.0.0.0; 
      link to template
      set Macros:   '{$ACCOUNT} <account-aws-name>' and '{$REGION} <region>'
