'''
all the static variables are defined here and imported in other files 

'''




Config = { 
'SECRET_KEY' : 'dev' , 
'DATABASE_NAME' : 'database.db' ,
'database_pathe' : '',
'static_folder' : 'static' , 
'template_folder' : 'templates' , 

}


# Path: views.py 
routes_name ={
'index' : '/' ,
'login' : '/login' ,
'logout' : '/logout' ,
'signup' : '/signup' , 


}