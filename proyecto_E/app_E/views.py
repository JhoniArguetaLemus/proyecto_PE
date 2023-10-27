from django.shortcuts import render

"""



config={
    
    "apiKey": "AIzaSyCTeYnMMeRkMyB1HKe4qx03Q4j8xADaqHc",

    "authDomain": "electronica-75518.firebaseapp.com",

    "databaseURL": "https://electronica-75518-default-rtdb.firebaseio.com",

    "projectId": "electronica-75518",

    "storageBucket": "electronica-75518.appspot.com",

    "messagingSenderId": "492949454110",

    "appId": "1:492949454110:web:5fc1d41cdd6b91c7dedd0f"

    
}

firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()
"""
def vista1(request):
   # channel_name=database.child('Data').child('nombre').get().val()
    #channel_last_name=database.child('Data').child('apellido').get().val()
    
    return render(request, "index.html"
                  )
