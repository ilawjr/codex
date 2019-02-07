# 85,000 msgs a second is a storm
echo "Starting locust test"
locust \
-f locustfile.py \
--host=https://dev-relaxing-mink-svalinn-0.codex.comcast.net:8080 \
--no-web \
-c 100000 \
-r 10000 \
--run-time 5m
echo "Ending locust test"

#-c 125000 \
#-r 12500 \
