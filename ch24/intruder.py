#S3C2 Carl Zhao Monitoring System
#
#
#
#
#
while 1:
    print("Start")
    print("System Inactive")
    SystemActive=False
    
    ButtonPressed1=int(input("If press button, type 1; otherwise type 2"))
    if ButtonPressed1 == 1:
          print("System Active")
          SystemActive=True
    else:
          print("")
          Pin=int(input("Please enter your pin# For this occassion only, 1=pin entered, otherwise 2"))
          if  Pin==1:
                print("System Inactive")
                SystemActive=False
                break
          else:
                print("System Active")
                print("Sensor Activated")

              
                Pin2=int(input("Please enter your pin# For this occassion only, 1=pin entered, otherwise 2"))
                if Pin2==1:
                    print("System Inactive")
                    SystemActive=False
                    break
                else:
                    SystemActove=True
                    print("System Active")
                    print("After 2 mins, bell will ring")

                    Pin3=int(input("Please enter your pin# For this occassion only, 1=pin entered, otherwise 2"))
                    if Pin3==1:
                        print("SystemInactive")
                        SystemActive=False
                    else:
                        SystemActive=True
                        BellRings=True
                
         

        
