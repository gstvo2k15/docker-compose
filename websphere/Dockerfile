FROM icr.io/appcafe/websphere-traditional:8.5.5.22

COPY --chown=was:root was-config.props /work/config/
COPY --chown=was:root myApp.war /work/app/
COPY --chown=was:root myAppDeploy.py dataSourceConfig.py disableSecurity.py /work/config/

RUN /work/configure.sh
