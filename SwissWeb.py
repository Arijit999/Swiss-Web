import os
import qrcode
import requests 
import pyshorteners
from rich.console import Console
from rich.traceback import install
from tqdm import tqdm
from pyfiglet import Figlet

console = Console()

def ISO_Downloader(Url,Name,extension="iso"):
    
    try:
        data = requests.get(Url,stream=True)
        Total_Bytes=int(data.headers["Content-Length"]) # Get the total file size
        #print("Total_Bytes :",Total_Bytes)
        progress_bar=tqdm(total=Total_Bytes,unit='iB',unit_scale=True,leave=False,desc=f"Downloading {Name}")
        with open(f"{Name}.{extension}", "ab") as iso:
            for bytes in data.iter_content(chunk_size=10*1024*1024):
                iso.write(bytes)
                progress_bar.update(len(bytes))
        console.print("\nDownload completed!\n",style="Green")
    except:
        console.print("\nError occurred\n🌐 Check internet connection.",style="red")

def Linux_ISOs():
    '''
    Docstring for Linux_ISOs
    '''
    clear_screen()
    ISO_Name={1:"Kali Linux",2:"Ubuntu",3:"Fedora",4:"Debian",5:"Manjaro",6:"Opensuse",7:"Centos",8:"Popos",9:"Linux Mint",10:"Parrotos",0:"Quit"}
    ISO_Url={"Kali Linux":"https://cdimage.kali.org/kali-2025.2/kali-linux-2025.2-installer-amd64.iso",
             "Ubuntu":"https://releases.ubuntu.com/24.04.3/ubuntu-24.04.3-desktop-amd64.iso",
             "Fedora":"https://download.fedoraproject.org/pub/fedora/linux/releases/42/Workstation/x86_64/iso/Fedora-Workstation-Live-42-1.1.x86_64.iso",
             "Debian":"https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-13.1.0-amd64-netinst.iso",
             "Manjaro":"https://download.manjaro.org/gnome/25.0.10/manjaro-gnome-25.0.10-251013-linux612.iso",
             "Opensuse":"https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso",
             "Centos":"https://mirrors.centos.org/mirrorlist?path=/10-stream/BaseOS/aarch64/iso/CentOS-Stream-10-latest-aarch64-dvd1.iso&redirect=1&protocol=https",
             "Popos":"https://iso.pop-os.org/22.04/amd64/intel/58/pop-os_22.04_amd64_intel_58.iso",
             "Linux Mint":"https://pub.linuxmint.io/stable/22.2/linuxmint-22.2-cinnamon-64bit.iso",
             "Parrotos":"https://deb.parrot.sh/parrot/iso/6.4/Parrot-security-6.4_amd64.iso"}
    while(True):
        print("\n")
        # Display available iso 
        for n,iso in enumerate(ISO_Name.values()):
            if iso == "Quit":
                console.print(f"[red][0][/]{iso}")        
            else:
                console.print(f"[green][{n+1}]{iso}[/]")
        
        ch = input("Download ISO: ").upper()
        #if ch not in ['1','2','3','4','5','6','7','8','9','10','0']:
        if ch not in [str(i) for i in range(11)]:
            console.print("Invalid input.",style="Red")
            continue
        else:
            break
    if ch == '0': # Exit 
        pass
    else: 
        if os.path.exists("Linux iso"):
            os.chdir("Linux iso")
        else:
            os.mkdir("Linux iso") # Creating directory for ISO
            os.chdir("Linux iso")
        ISO_Downloader( ISO_Url.get(ISO_Name.get(int(ch))) , ISO_Name.get(int(ch)))
    os.chdir("..") # Return to original directory 

def QR_Generator():
    """
    Generate QR codes
    """
    clear_screen()
    while(True):
        console.print("[red]Q[/] to quit")
        URL=input("Enter url: ")
        if URL in ['Q','q']:
            break
        else:
            name = input("QR name: ")
            QR = qrcode.make(URL)
            if os.path.exists("QR code"):
                os.chdir("QR code")
            else:
                os.mkdir("QR code")
                os.chdir("QR code")
            QR.save(f"{name}.png")
            os.chdir("..")
            console.print(f"[green]QR has been generated![/]")

def short_url() -> str:
    """
    Takes a long url as input and
    returns a short url
    
    :return: Short url
    :rtype: str
    """
    clear_screen()
    s = pyshorteners.Shortener()
    while(True):
       
        try:
            console.print("\n[red]Q[/] to quit")
            URL = input("Enter Url : ")
            if URL in ['Q','q']:
                break
            short_url = s.tinyurl.short(URL)
            console.print("Short URl : ",short_url,style="green")
        except:
            console.print("Wrong url",style="red")
            continue


def main():
    console.print("\n[1]Linux ISOs \n[2]QR Generator \n[3]Url Shortner \n[red]'Q'[/] to quit",style="cyan")
    while(True):
        ch=console.input("[green]Enter option: ").upper()
        if ch not in ['1','2','3','Q']:
            console.print("Wrong input!",style="Red")
            continue
        else:
            break
    match ch:
        case "1":
            Linux_ISOs()
        case "2":
            QR_Generator()
        case "3":
            short_url()
        case "Q":
           quit()

def clear_screen():
    if os.name == 'posix':  # For macOS and Linux
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')

if __name__ == "__main__":
    clear_screen()
    figlet=Figlet(font="slant")
    Ascii=figlet.renderText('SwissWeb')
    console.print(f"[bold magenta]{Ascii}")
    install()
    while(True):
        main()
        