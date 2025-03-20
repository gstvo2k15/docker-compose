# docker-compose
Basic repo for docker compose v2 util tools

## Observability & middleware steps

```bash
cd observability

docker network create app-tier

docker compose up -d --build

cd -
/root/docker-compose/middleware

docker compose up -d --build

docker compose ps
NAME        IMAGE                                   COMMAND                  SERVICE     CREATED         STATUS         PORTS
jboss       jboss/wildfly:latest                    "/bin/sh -c '/opt/jb…"   jboss       9 seconds ago   Up 9 seconds   0.0.0.0:9091->9091/tcp, [::]:9091->9091/tcp, 0.0.0.0:9082->8080/tcp, [::]:9082->8080/tcp
tomcat      tomcat:9.0                              "catalina.sh run"        tomcat      9 seconds ago   Up 9 seconds   0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp, 0.0.0.0:9081->8080/tcp, [::]:9081->8080/tcp
weblogic    gstvo2k15/weblogic:12.2.1.4-developer   "/u01/oracle/createA…"   weblogic    9 seconds ago   Up 9 seconds   0.0.0.0:7001->7001/tcp, [::]:7001->7001/tcp, 0.0.0.0:9092->9092/tcp, [::]:9092->9092/tcp, 9002/tcp
websphere   websphere-liberty:latest                "/opt/ibm/helpers/ru…"   websphere   9 seconds ago   Up 9 seconds   0.0.0.0:9094->9094/tcp, [::]:9094->9094/tcp, 9443/tcp, 0.0.0.0:9084->9080/tcp, [::]:9084->9080/tcp

cd -
/root/docker-compose/observability

docker compose ps
NAME                     IMAGE                         COMMAND                  SERVICE                  CREATED          STATUS          PORTS
alertmanager             prom/alertmanager:latest      "/bin/alertmanager -…"   alertmanager             23 seconds ago   Up 22 seconds   0.0.0.0:9993->9093/tcp, [::]:9993->9093/tcp
grafana                  grafana/grafana:latest        "/run.sh"                grafana                  23 seconds ago   Up 22 seconds   0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp
jmx-exporter-jboss       bitnami/jmx-exporter:latest   "java -jar jmx_prome…"   jmx-exporter-jboss       23 seconds ago   Up 22 seconds   0.0.0.0:1235->1235/tcp, [::]:1235->1235/tcp, 5556/tcp
jmx-exporter-tomcat      bitnami/jmx-exporter:latest   "java -jar jmx_prome…"   jmx-exporter-tomcat      23 seconds ago   Up 22 seconds   0.0.0.0:1234->1234/tcp, [::]:1234->1234/tcp, 5556/tcp
jmx-exporter-weblogic    bitnami/jmx-exporter:latest   "java -jar jmx_prome…"   jmx-exporter-weblogic    23 seconds ago   Up 22 seconds   0.0.0.0:1236->1236/tcp, [::]:1236->1236/tcp, 5556/tcp
jmx-exporter-websphere   bitnami/jmx-exporter:latest   "java -jar jmx_prome…"   jmx-exporter-websphere   23 seconds ago   Up 22 seconds   0.0.0.0:1237->1237/tcp, [::]:1237->1237/tcp, 5556/tcp
node-exporter            prom/node-exporter:latest     "/bin/node_exporter"     node-exporter            23 seconds ago   Up 22 seconds   0.0.0.0:9100->9100/tcp, [::]:9100->9100/tcp
prometheus               prom/prometheus:latest        "/bin/prometheus --c…"   prometheus               23 seconds ago   Up 22 seconds   0.0.0.0:9990->9090/tcp, [::]:9990->9090/tcp
```
