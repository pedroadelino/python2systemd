#!/usr/bin python3

import os, subprocess
from platform import python_version
# this app installs python apps
# and activate the apps as System D services
# it also lets you check if service is running
# and disable and uninstall the service

# var
python_bin_folder = "/usr/bin"
python_bin_folder_exists = False
python_bin = ""
python_bin_exists = False
py_apps_folder = os.getcwd() + "/python_apps"
py_apps_folder_exists = False
systemd_folder = "/etc/systemd/system"
systemd_folder_exists = False
total_py_apps = 0
app_selected = ""
service_selected = ""
service_name = ""
service_filename = ""

def menu():
    print("M E N U")
    print("1 - Install service")
    print("2 - Remove service")
    print("3 - Start service")
    print("4 - Stop service")
    print("5 - Enable service")
    print("6 - Disable service")
    print("7 - Check service status")
    print("8 - Reload Daemon")
    print("9 - Exit app")
    try:
        print(python_bin)
        if python_bin == "python":
           option = raw_input("Choose an option : ")
        elif python_bin == "python3":
           option = input("Choose an option : ")
    except:
        print("Fatal error! Exiting app..")
        exit()
    if option == "1" or option == 1:
       install_service()
    elif option == "2" or option == 2:
       remove_service()
    elif option == "3" or option == 3:
       start_service()
    elif option == "4" or option == 4:
       stop_service()
    elif option == "5" or option == 5:
       enable_service()
    elif option == "6" or option == 6:
       disable_service()
    elif option == "7" or option == 7:
       check_status()
    elif option == "8" or option == 8:
       reload_systemd_daemon()
    elif option == "9" or option == 9:
       print("Bye")
       exit()
    else:
       print("No option selected! Bye!")
       exit()

def start_service():
    list_services()
    read_input_service()
    start_systemd_service()

def stop_service():
    list_services()
    read_input_service()
    stop_systemd_service()

def enable_service():
    list_services()
    read_input_service()
    enable_systemd_service()

def disable_service():
    list_services()
    read_input_service()
    disable_systemd_service()

def remove_service():
    list_services()
    read_input_service()
    remove_systemd_service()

def check_status():
    list_services()
    read_input_service()
    status_systemd_service()

def sys_check():
    global python_bin
    print(python_version())
    if python_version()[0] == "3":
        python_bin = "python3"
    #elif python_version()[0] == "3":
       #python_bin = "python3"
    #try:
        # python 3
        print(subprocess_get_output("uname -mrs"))
        print(subprocess_get_output("python3 --version"))
        print(subprocess_get_output("systemd --version"))
        #python_bin = "python3"
    #except:
    elif python_version()[0] == "2":
        python_bin = "python"
        # python 2 - not supported
        #cmd = ['uname','-mrs']
        # returns output as byte string
        #returned_output = subprocess.check_output(cmd)
        # using decode() function to convert byte string to string
        print(subprocess_check_output('uname','-mrs')) #.decode("utf-8"))
        print(subprocess_check_output('python','--version')) #.decode("utf-8"))
        print(subprocess_check_output('systemd','--version')) #.decode("utf-8"))
        #python_bin = "python"
        #print("Fatal error! Python version not supported yet. Exiting app...")
        #exit()

def subprocess_check_output(a, b):
    # python
    try:
       res = subprocess.check_output([a,b]).strip()
       #rc=res.wait()
       subprocess._cleanup()
       #res.stdout.close()
       #res.stderr.close()
    except:
       print("Subprocess")
       print("Fatal error! Exiting app...")
       exit()
    #subprocess.checkoutput.kill()
    return res

def subprocess_get_output(cmd):
    # python 3
    try:
       res = subprocess.getoutput(cmd)
       #rc=res.wait()
       subprocess._cleanup()
       #res.stdout.close()
       #res.stderr.close()
    except:
       print("Subprocess 3")
       print("Fatal error! Exiting app...")
       exit()
    #subprocess.kill()
    return res

def check_folders():
    global systemd_folder, systemd_folder_exists, py_apps_folder, py_apps_folder_exists, python_bin_folder, python_bin_folder_exists, python_bin, python_bin_exists
    systemd_folder_exists = os.path.exists(systemd_folder)
    if systemd_folder_exists == True:
        print("Found System D folder")
    else:
        print("No System D folder found!")
        print("Exiting app...")
        exit()
    py_apps_folder_exists = os.path.exists(py_apps_folder)
    if py_apps_folder_exists == True:
        print("Found Python apps folder")
    else:
        print("No Python apps folder found!")
        print("Exiting app...")
        exit()
    python_bin_folder_exists = os.path.exists(python_bin_folder)
    if python_bin_folder_exists == True:
        print("Found Python bin folder")
    else:
        print("No Python bin folder found!")
        print("Exiting app...")
        exit()
    python_bin_exists = os.path.exists(python_bin_folder + "/" + python_bin)
    if python_bin_exists == True:
       print("Found Python bin")
       bytes = os.path.getsize(python_bin_folder + "/" + python_bin)
       print("File size : " + str(bytes) + " bytes")
    else:
       print("No Python bin file found!")
       print("Exiting app...")
       exit()

def list_apps():
    global py_apps_folder
    nr_apps = 0
    print("Searching for apps...")
    for root, dirs, files in os.walk(py_apps_folder):
       for filename in files:
          if filename.endswith(".py"):
             nr_apps += 1
             bytes = os.path.getsize(py_apps_folder + "/" + filename)
             print(str(nr_apps) + " : " + filename + " , " + str(bytes) + " bytes")
    #print(nr_apps)
    if nr_aps == 0:
       print("No apps found!")
       print("Exiting app...")
       exit()
    else:
       print("Choose the app to install :")

def list_services():
    global systemd_folder
    nr_services = 0
    print("Searching for services...")
    for root, dirs, files in os.walk(systemd_folder):
       for filename in files:
          if filename.endswith("_p2sd.service"):
             nr_services += 1
             bytes = os.path.getsize(systemd_folder + "/" + filename)
             print(str(nr_services) + " : " + filename + " , " + str(bytes) + " bytes")
    if nr_services == 0:
       print("No services found!")
       print("Exiting app..")
       exit()
    else:
       print("Choose the service to install :")

def list_apps_3():
    global py_apps_folder
    nr_apps = 0
    print("Searching for apps...")
    #res = subprocess.getoutput("ls " + py_apps_folder + "/*.py")
    for path in os.scandir(py_apps_folder):
        if path.is_file():
            if os.path.splitext(path.name)[1] == ".py":
                nr_apps += 1
                bytes = os.path.getsize(py_apps_folder + "/" + path.name)
                print(str(nr_apps) + " : " + path.name + " , " + str(bytes) + " bytes")
    if nr_apps == 0:
        print("No apps found!")
        print("Exiting app...")
        exit()
    else:
        print("Choose the app to install : ")
        #print(res)

def list_services_3():
    global systemd_folder
    nr_services = 0
    print("Searching for services...")
    #res  = subprocess.getoutput("ls " + systemd_folder + "/*_p2sd.service")
    for path in os.scandir(systemd_folder):
        if path.is_file():
            if os.path.splitext(path.name)[1] == "_p2sd.service":
                nr_services += 1
                bytes = os.path.getsize(systemd_folder + "/" + path.name)
                print(str(nr_services) + " : " + path.name + " , " + str(bytes) + " bytes")
    if nr_services == 0:
       print("No p2sd services found!")
       print("Exiting app...")
       exit()
    else:
       print("Choose the service : ")
       #print(res)

def read_input_app():
    global app_selected, py_apps_folder
    app = input("App : ")
    if app == "":
        print("No app selected!")
        print("Exiting app...")
        exit()
    else:
        print("App selected : " + app)
        app_exists = os.path.exists(py_apps_folder + "/" + app)
        if app_exists == True:
            app_selected = app
            print("App exists, getting ready to install service.")
        elif app_exists == False:
            print("App selected is NOT present!")
            print("Exiting app...")
            exit()
        else:
            print("Fatal error!")
            exit()
    # check if app exists in folder, exit app if no app exists

def read_input_service():
    global service_selected, systemd_folder
    service = input("Service : ")
    if service == "":
        print("No service selected!")
        print("Exiting app...")
        exit()
    else:
        print("Service selected : " + service)
        service_exists = os.path.exists(systemd_folder + "/" + service)
        if service_exists == True:
            service_selected = service
            print("Service exists.")
        elif service_exists == False:
            print("Service selected is NOT present!")
            print("Exiting app...")
            exit()
        else:
            print("Fatal error!")
            exit()
    # check if service exists in folder, exit app if no app exists

def read_name_service():
    global service_name, service_filename, app_selected, systemd_folder
    service_name = input("Enter the name of the service : ")
    if service_name == "":
        print("No name entered!")
        exit()
    filename_no_py = os.path.splitext(app_selected)[0]
    service_filename = filename_no_py + '_p2sd.service'
    print("Service filename : " + service_filename)
    service_exists = os.path.exists(systemd_folder + "/" + service_filename)
    if service_exists == True:
        print("Error : Service already exists!")
        print("Exiting app.")
        exit()
    else:
        print("Ready to install service.")

def save_systemd_service():
    global service_filename, service_name, app_selected, service_selected, systemd_folder, py_apps_folder, python_bin_folder, python_bin
    if service_filename == "":
        print("Error. No service filename.")
        exit()
    elif service_name == "":
        print("Error : No service name.")
        exit()
    elif app_selected == "":
        print("Error : No app selected.")
        exit()
    else:
        print("Are you sure you want to install this service?")
        option = input("(yes = confirm) : ")
        if option == "yes":
            print("Saving service...")
            f = open(systemd_folder + "/" + service_filename, "w")
            f.write("[Unit]\n")
            f.write("Description=" + service_name + "\n")
            f.write("After=multi-user.target\n")
            f.write("[Service]\n")
            f.write("Type=simple\n")
            f.write("Restart=always\n")
            f.write("ExecStart=" + python_bin_folder + "/" + python_bin + " " + py_apps_folder + "/" + app_selected + "\n")
            f.write("[Install]\n")
            f.write("WantedBy=multi-user.target\n")
            f.close()
            print("Service installed.")
            bytes = os.path.getsize(systemd_folder + "/" + service_filename)
            print(str(bytes) + " bytes written.")
            service_selected = service_filename
        else:
            print("Installation aborted! Try again!")
            exit()
def run_system_cmd(task, command):
    global service_selected, python_bin
    print(task + service_selected)
    if python_bin == "python3":
       print(subprocess_get_output(command + service_selected))
    elif python_bin == "python":
       print(subprocess_check_output(command + service_selected))

def enable_systemd_service():
    global service_selected, python_bin
    print("Enabling service : " + service_selected)
    if python_bin == "python3":
        print(subprocess_get_output("sudo systemctl enable " + service_selected))
    #print(subprocess_check_output('sudo','systemctl enable ' + service_selected))

def disable_systemd_service():
    global service_selected
    print("Disabling service : " + service_selected)
    print(subprocess_get_output("sudo systemctl disable " + service_selected))
    #print(subprocess_check_output('sudo','systemctl disable ' + service_selected))

def start_systemd_service():
    global service_selected
    print("Starting service : " + service_selected)
    print(subprocess_get_output("sudo systemctl start " + service_selected))
    #print(subprocess_check_output('sudo','systemctl start ' + service_selected))

def stop_systemd_service():
    global service_selected
    print("Stopping service : " + service_selected)
    print(subprocess_get_output("sudo systemctl stop " + service_selected))
    #print(subprocess_check_output('sudo','systemctl stop ' + service_selected))

def restart_systemd_service():
    global service_selected
    print("Restarting service : " + service_selected)
    print(subprocess_get_output("sudo systemctl restart " + service_selected))
    #print(subprocess_check_output('sudo','systemctl restart ' + service_selected))

def status_systemd_service():
    global service_selected
    print("Checking service : " + service_selected)
    print(subprocess_get_output("sudo systemctl status " + service_selected))
    #print(subprocess_check_output('sudo','systemctl status ' + service_selected))

def remove_systemd_service():
    global service_selected, systemd_folder
    print("Are you sure you want to remove this service?")
    option = input("yes or no? : ")
    if option == "no":
       print("Service NOT removed!")
       print("Bye")
       exit()
    elif option == "yes":
       print("Removing service...")
       print(subprocess_get_output("rm " + systemd_folder + "/" + service_selected))
       #print(subprocess_check_output('rm', systemd_folder + "/" + service_selected))
       print("Done")
       print("Bye")
       exit()

def reload_systemd_daemon():
    print("Reloading System D daemon...")
    print(subprocess_get_output("sudo systemctl daemon-reload"))
    #print(subprocess_check_output('sudo systemctl', 'daemon-reload'))

def install_service():
    list_apps()
    read_input_app()
    read_name_service()
    save_systemd_service()
    reload_systemd_daemon()
    enable_systemd_service()
    start_systemd_service()

# Main
def main():
    #print(raw_input("Teste:"))
    print("Python 2 System D")
    print("Made by Pedro Adelino")
    print("Starting...")
    sys_check()
    check_folders()
    menu()
    print("Bye!")

if __name__ == "__main__":
    main()
