# scraper-organizer
organize collected business and companies data in any sector for future use

as we all know one of the most important elements for success of any marketing or sales team is to have some good data about the sector that they are targeting.
For that we are going to use the scraping method as a solution.

![image](https://user-images.githubusercontent.com/120245923/206844991-1d5de08b-0430-4a73-9d7c-0bda1325e2c5.png)


if this error occured
OSError: cannot load library 'gobject-2.0-0': error 0x7e.  Additionally, ctypes.util.find_library() did not manage to locate a library called 'gobject-2.0-0'       

just download GTK3-Runtime Win64 > put it in program files

def _load_backend_lib(backend, name, flags):
    import os
    # os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\gtk-nsis-pack\/bin")
    # or another way to do that
    # os.environ['PATH'] += os.pathsep + "C:\Program Files\GTK3-Runtime Win64\gtk-nsis-pack\/bin"
