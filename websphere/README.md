# WebSphere Traditional Deployment with Docker Compose

## Execution Steps

```bash
git clone https://github.com/gstvo2k15/docker-compose.git
cd websphere
curl -fsSL https://clis.cloud.ibm.com/install/linux | sh

ibmcloud plugin install container-registry
ibmcloud plugin list
ibmcloud cr region-set global

mkdir -p server/{apps,resources}
echo "com.ibm.ws.config=example" > was-config.props
touch myApp.war

mkdir -p logs
chmod -R 775 logs
touch {myAppDeploy,dataSourceConfig}.py

docker compose up -d --build
docker compose ps && docker compose logs -f --tail=15
```

### URL access

`https://192.168.1.122:9043/ibm/console`


### How to obtain credentials

```bash
docker compose exec -it websphere-traditional bash

/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/wsadmin.sh -lang jython -conntype NONE -f /work/config/disableSecurity.py

exit

docker compose restart
```


### Logs review:

`docker compose logs -f --tail=15`

```
websphere-traditional  | ADMU0116I: Tool information is being logged in file
websphere-traditional  |            /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/logs/server1/startServer.log
websphere-traditional  | ADMU0128I: Starting tool with the AppSrv01 profile
websphere-traditional  | ADMU3100I: Reading configuration for server: server1
websphere-traditional  | Configure logging mode
websphere-traditional  | WASX7357I: By request, this scripting client is not connected to any server process. Certain configuration and application operations will be available in local mode.
websphere-traditional  | WASX7357I: By request, this scripting client is not connected to any server process. Certain configuration and application operations will be available in local mode.
websphere-traditional  | WASX7303I: The following options are passed to the scripting environment and are available as arguments that are stored in the argv variable: "[/work/config-ibm/webContainer.props]"
websphere-traditional  | HPEL is enabled
websphere-traditional  | Starting logViewer ................
websphere-traditional  | Starting server ...................
websphere-traditional  | ADMU0116I: Tool information is being logged in file
websphere-traditional  |            /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/logs/server1/startServer.log
websphere-traditional  | ADMU0128I: Starting tool with the AppSrv01 profile
websphere-traditional  | ADMU3100I: Reading configuration for server: server1
```


### Posible ulimits to change

```bash
ulimit -n 65536
ulimit -s 16384
ulimit -l unlimited
```
