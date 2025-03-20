connect('weblogic', 'weblogic123', 't3://localhost:7001')
edit()
startEdit()

cd('/Servers/AdminServer')
set('ListenAddress', '0.0.0.0')
set('ListenPort', 7001)

cd('/Servers/AdminServer/ServerDebug/AdminDebug')
set('DebugJMX', 'true')

save()
activate()
exit()
