# docker-compose
Basic repo for docker compose v2 util tools

## Observability & middleware steps

```bash
cd observability

docker network create app-tier

docker compose up -d --build

docker compose ps
```

```bash
NAME                     IMAGE                         COMMAND                  SERVICE                  CREATED         STATUS         PORTS
alertmanager             prom/alertmanager:latest      "/bin/alertmanager -…"   alertmanager             9 seconds ago   Up 8 seconds   0.0.0.0:9093->9093/tcp, [::]:9093->9093/tcp
grafana                  grafana/grafana:latest        "/run.sh"                grafana                  9 seconds ago   Up 8 seconds   0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp
jmx-exporter-jboss       bitnami/jmx-exporter:latest   "java -jar jmx_prome…"   jmx-exporter-jboss       9 seconds ago   Up 8 seconds   0.0.0.0:1235->1235/tcp, [::]:1235->1235/tcp, 5556/tcp
jmx-exporter-tomcat      bitnami/jmx-exporter:latest   "java -jar jmx_prome…"   jmx-exporter-tomcat      9 seconds ago   Up 8 seconds   0.0.0.0:1234->1234/tcp, [::]:1234->1234/tcp, 5556/tcp
jmx-exporter-weblogic    bitnami/jmx-exporter:latest   "java -jar jmx_prome…"   jmx-exporter-weblogic    9 seconds ago   Up 8 seconds   0.0.0.0:1236->1236/tcp, [::]:1236->1236/tcp, 5556/tcp
jmx-exporter-websphere   bitnami/jmx-exporter:latest   "java -jar jmx_prome…"   jmx-exporter-websphere   9 seconds ago   Up 8 seconds   0.0.0.0:1237->1237/tcp, [::]:1237->1237/tcp, 5556/tcp
node-exporter            prom/node-exporter:latest     "/bin/node_exporter"     node-exporter            9 seconds ago   Up 8 seconds   0.0.0.0:9100->9100/tcp, [::]:9100->9100/tcp
prometheus               prom/prometheus:latest        "/bin/prometheus --c…"   prometheus               9 seconds ago   Up 8 seconds   0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp
```
