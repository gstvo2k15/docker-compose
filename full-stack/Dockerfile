FROM gstvo2k15/weblogic:12.2.1.4-developer

COPY domain.properties /u01/oracle/properties/domain.properties
COPY jmx.properties /u01/oracle/properties/jmx.properties

RUN /u01/oracle/createAndStartEmptyDomain.sh

EXPOSE 7001 9092

CMD ["/u01/oracle/user_projects/domains/base_domain/bin/startWebLogic.sh"]
