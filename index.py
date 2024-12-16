import gi
import subprocess
import time
from plyer import notification
gi.require_version("Gtk","3.0")
gi.require_version("GLib","2.0")
from gi.repository import Gtk,GLib

class pomodoroWin(Gtk.Window):
    def __init__(self):
        super().__init__(title="Pomodoro app")
        self.minutes=25
        self.seconds=0
       #creating vbox
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        self.add(self.vbox)
       #creating layouts 
        self.timeInputBox=Gtk.Box(spacing=6) 
        self.timerHbox = Gtk.Box(spacing=6)
        self.btnsHbox = Gtk.Box(spacing=6)
        self.vbox.pack_start(self.timeInputBox,False,True,0)
        self.vbox.pack_start(self.timerHbox,True,True,0)
        self.vbox.pack_start(self.btnsHbox,True,True,0)
        # first layout
        self.timeInput=Gtk.Entry()
        self.timeSaveBtn = Gtk.Button(label="Save")
        self.timeSaveBtn.connect("clicked",self.saveTime)
        self.timeInputBox.pack_start(self.timeInput,True,True,1)
        self.timeInputBox.pack_start(self.timeSaveBtn,False,True,1)
       #second layout 
        self.timerLabel=Gtk.Label()
        self.timerLabel.set_markup("<span size='70000'>"+str(self.minutes)+":"+str(self.seconds)+"</span>")
        self.timerHbox.pack_start(self.timerLabel,True,True,2)
       # third layout 
        self.playButton=Gtk.Button(label=" Play")
        self.playButton.connect("clicked",self.startTimer)
        self.stopButton=Gtk.Button(label=" Stop")
        self.stopButton.connect("clicked",self.stopTimer)
        self.btnsHbox.pack_start(self.playButton,True,True,2)
        self.btnsHbox.pack_start(self.stopButton,True,True,2)
        self.timeout_id=None 
   
    def saveTime(self,widget):
        if len(self.timeInput.get_text()) == 0:
            self.minutes=25
        else:
            self.minutes=int(self.timeInput.get_text())
            self.timerLabel.set_markup("<span size='70000'>"+str(self.minutes)+":"+str(self.seconds)+"</span>")


    def updateTime(self):
        self.seconds-=1 
        if self.seconds <= 0 :
            self.seconds=59
            self.minutes-=1
        
        self.timerLabel.set_markup("<span size='70000'>"+str(self.minutes)+":"+str(self.seconds)+"</span>")
        if self.minutes<0:
            self.notify()
            subprocess.run(["paplay","music/notify.wav"])
            self.timerLabel.set_markup("<span size='70000'>Time Ended</span>")
            self.minutes=25
            self.seconds=0
            GLib.source_remove(self.timeout_id)
            self.timeout_id=None
            return GLib.SOURCE_REMOVE
        return GLib.SOURCE_CONTINUE 
    
    def stopTimer(self,widget):
        self.minutes=-1
        self.updateTime()
        self.timerLabel.set_markup("<span size='70000'>Time Stopped</span>")

    def startTimer(self,widget):
        if self.timeout_id is None:
            self.timeout_id= GLib.timeout_add_seconds(1,self.updateTime)
    
    def notify(self):
        notification.notify(
            title="Time Ended",
            message="Time Ended Successfully"
        )


win = pomodoroWin()
win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()


