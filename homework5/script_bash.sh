#!/bin/bash
# variables
LOGFILE="access.log"
RESULT="result_bash.txt"

all_requests_cnt(){
echo "Общее количество запросов:" > $RESULT
cat $LOGFILE | wc -l >> $RESULT
echo '' >> $RESULT
}

top_requests_methods(){
echo "Общее количество запросов по типу:" >> $RESULT
cat $LOGFILE | awk '{print $6}' | cut -d'"' -f2 | sort | uniq -c | sort -rn | awk '{print $2, $1}' | head -5 >> $RESULT
echo '' >> $RESULT
}

top_requests_freq(){
echo "Топ 10 самых частых запросов:" >> $RESULT
cat $LOGFILE | awk '{print $7}' | sort | uniq -c | sort -rn | head -10 >> $RESULT
echo '' >> $RESULT
}

top_users_req_4XX(){
echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4XX) ошибкой:" >> $RESULT
cat $LOGFILE | awk '$9 ~ /^4/ {print $1, $7, $9, $10}' | sort -rnk4 | head -5 >> $RESULT
echo '' >> $RESULT
}

top_users_req_5XX(){
echo "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:" >> $RESULT
cat $LOGFILE | awk '$9 ~ /^5/ {print $1}' | sort | uniq -c | sort -rn | awk '{print $2, $1}' | head -5 >> $RESULT
}

# executing
all_requests_cnt
top_requests_methods
top_requests_freq
top_users_req_4XX
top_users_req_5XX
