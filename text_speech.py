
# text to speech convertor 

import pyttsx3

engine = pyttsx3.init()

list_1 = "Python is a cross-platform programming language, which means that it can run on multiple platforms \
    like Windows, macOS, Linux, and\
 has even been ported to the Java and .NET virtual machines.\
 It is free and open-source.\
     Even though most of today's Linux and Mac have Python pre-installed in it, the version might be out-of-date.\
          So, it is always a good idea to install the most current version.\
              If you want to learn python then join Dhiraj's coding class call @8742074156"
engine.say(list_1)
engine.runAndWait()
