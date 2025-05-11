### Steps to execute project

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
touch {myAppDeploy,dataSourceConfig}.py

docker compose up -d --build
docker compose ps && docker compose logs -f --tail=15
```

