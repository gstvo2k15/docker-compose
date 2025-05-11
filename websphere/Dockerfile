FROM icr.io/appcafe/websphere-traditional:8.5.5.23

COPY --chown=was:root was-config.props /work/config/
COPY --chown=was:root myApp.war /work/app/
COPY --chown=was:root myAppDeploy.py dataSourceConfig.py /work/config/

RUN /work/configure.sh
