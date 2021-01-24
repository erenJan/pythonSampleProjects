import time
from plyer import notification

notification.notify(
            #title of the notification,
            title = "COVID19 Stats on {}",
            #the body of the notification
            message = "deneme",  
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = "corona.ico",
            # the notification stays for 50sec
            timeout  = 50
        )


#pync.notify('Hello World')
#pync.notify('Hello World', title='Python')
#pync.notify('Hello World', group=os.getpid())
#pync.notify('Hello World', activate='com.apple.Safari')
#pync.notify('Hello World', open='http://github.com/')
#pync.notify('Hello World', execute='say "OMG"')

