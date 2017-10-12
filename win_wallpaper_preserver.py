import winreg
import ctypes

from time import sleep
REG_PATH = r"Control Panel\Desktop"
wallpaper_path = r"PATH\TO\WALLPAPER"
previous_wallpaper = ""


def main():
    global previous_wallpaper
    previous_wallpaper = get_reg("TranscodedImageCache")

    while True:
        sleep(1)
        current_wallpaper = get_reg("TranscodedImageCache")

        if current_wallpaper != previous_wallpaper:
            print("Change Detected!")
            set_back()
            print("Changed Wallpaper To Default")
            previous_wallpaper = get_reg("TranscodedImageCache")


def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


def set_back():
    sleep(5)
    SPI_SETDESKWALLPAPER = 0x14  # which command (20)
    SPIF_UPDATEINIFILE = 0x2  # forces instant update
    print(ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, SPIF_UPDATEINIFILE))
    sleep(5)
    return

if __name__ == '__main__':
    main()
