# blackbox.arron.id
Blackbox style data recorder for Assetto Corsa Competizione (ACC)

Records session/stint/lap data within ACC and stores within a web app.

py_blackbox should be ran alongside the game. IT accesses the shared memory provided by the game to post data to py_blackbox_backend (django), The data is stored in a DB and request by ng-blackbox (Angular) and displayed in a nice interface. 
