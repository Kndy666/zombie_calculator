import subprocess
import os
import shutil
import py7zr
from colorama import init, Fore

init(autoreset=True)
print(Fore.YELLOW + "Start initializing.")

cwd = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zombie_calculator")

def convertDlls(dlls):
    return list(map(lambda x : f"--noinclude-dlls={x}", dlls))
def convertDataDir(dirs):
    return list(map(lambda x : f"--include-data-dir={os.path.join(cwd, x)}={x}", dirs))
def convertFiles(files):
    return list(map(lambda x : f"--include-data-files={os.path.join(cwd, x)}={x}", files))
def getVersion():
    with open("version", encoding="utf-8") as f:
        ver = f.read()
    return ver

noneCmd = ["nuitka", "--mingw64", "--standalone", "--show-progress", "--remove-output", "--windows-disable-console"]
stringCmd = ["--lto=no", "--enable-plugin=pyqt5", f"--windows-icon-from-ico={os.path.join(cwd, 'pack_resources/icon.ico')}",
            "--windows-product-name=zombie_calculator", f"--windows-product-version={getVersion()}", "--windows-company-name=Kndy666",
            "--windows-file-description=A program used to calculate specific pvz spawn seed.",
            f"--output-dir={os.path.join(cwd, 'release')}"]

include_data_dir = ["pack_resources/help", "qt_material", "pack_resources/language"]
include_data_files = ["pack_resources/icon.ico", "pack_resources/material.css.template"]
noinclude_dlls = ["qt5network.dll", "qt5multimedia.dll", "qt5qml.dll", "qt5qmlmodels.dll", "qt5quick.dll",
                 "qt5websockets.dll", "qt5printsupport.dll", "qt5dbus.dll", 
                 "api-ms-win-core-console-l1-1-0.dll", "api-ms-win-core-datetime-l1-1-0.dll", "api-ms-win-core-debug-l1-1-0.dll",
                 "api-ms-win-core-errorhandling-l1-1-0.dll", "api-ms-win-core-file-l1-1-0.dll", "api-ms-win-core-file-l1-2-0.dll",
                 "api-ms-win-core-file-l2-1-0.dll", "api-ms-win-core-handle-l1-1-0.dll", "api-ms-win-core-heap-l1-1-0.dll",
                 "api-ms-win-core-interlocked-l1-1-0.dll", "api-ms-win-core-libraryloader-l1-1-0.dll", "api-ms-win-core-localization-l1-2-0.dll",
                 "api-ms-win-core-memory-l1-1-0.dll", "api-ms-win-core-namedpipe-l1-1-0.dll", "api-ms-win-core-processenvironment-l1-1-0.dll",
                 "api-ms-win-core-processthreads-l1-1-0.dll", "api-ms-win-core-processthreads-l1-1-1.dll", "api-ms-win-core-profile-l1-1-0.dll",
                 "api-ms-win-core-rtlsupport-l1-1-0.dll", "api-ms-win-core-string-l1-1-0.dll", "api-ms-win-core-synch-l1-1-0.dll",
                 "api-ms-win-core-synch-l1-2-0.dll", "api-ms-win-core-timezone-l1-1-0.dll", "api-ms-win-core-util-l1-1-0.dll",
                 "api-ms-win-crt-conio-l1-1-0.dll", "api-ms-win-crt-convert-l1-1-0.dll", "api-ms-win-crt-environment-l1-1-0.dll",
                 "api-ms-win-crt-filesystem-l1-1-0.dll", "api-ms-win-crt-heap-l1-1-0.dll", "api-ms-win-crt-locale-l1-1-0.dll",
                 "api-ms-win-crt-math-l1-1-0.dll", "api-ms-win-crt-process-l1-1-0.dll", "api-ms-win-crt-runtime-l1-1-0.dll", 
                 "api-ms-win-crt-stdio-l1-1-0.dll", "api-ms-win-crt-string-l1-1-0.dll", "api-ms-win-crt-time-l1-1-0.dll",
                 "api-ms-win-crt-utility-l1-1-0.dll", "api-ms-win-core-sysinfo-l1-1-0.dll", "concrt140.dll", "libssl-1_1-x64.dll",
                 "libeay32.dll", "msvcp140.dll", "msvcp140_1.dll", "libcrypto-1_1-x64.dll",
                 "ssleay32.dll", "ucrtbase.dll", "vcruntime140.dll","vcruntime140_1.dll"]

remove_files = ["_asyncio.pyd", "_bz2.pyd", "_decimal.pyd", "_elementtree.pyd", "_hashlib.pyd", "_lzma.pyd", "_multiprocessing.pyd",
                "_overlapped.pyd", "_queue.pyd", "_socket.pyd", "_ssl.pyd", "select.pyd", "unicodedata.pyd", 
                "PyQt5/qt-plugins/imageformats/qgif.dll", "PyQt5/qt-plugins/imageformats/qicns.dll", "PyQt5/qt-plugins/imageformats/qjpeg.dll",
                "PyQt5/qt-plugins/imageformats/qtga.dll", "PyQt5/qt-plugins/imageformats/qtiff.dll", "PyQt5/qt-plugins/imageformats/qwbmp.dll",
                "PyQt5/qt-plugins/imageformats/qwebp.dll", "PyQt5/qt-plugins/platforms/qminimal.dll", "PyQt5/qt-plugins/platforms/qoffscreen.dll",
                "PyQt5/qt-plugins/platforms/qwebgl.dll"]
remove_dirs = ["PyQt5/qt-plugins/mediaservice", "PyQt5/qt-plugins/platformthemes", "PyQt5/qt-plugins/printsupport"]

print(Fore.GREEN + "Initialization completed.\n", Fore.YELLOW + "Start compiling.")

subprocess.run(noneCmd + stringCmd + 
               convertDlls(noinclude_dlls) + convertDataDir(include_data_dir) + convertFiles(include_data_files) + 
               [os.path.join(cwd, "zombie_calculator.py")],
               shell=True)

print(Fore.GREEN + "Compilation completed.\n", Fore.YELLOW + "Start removing extra dlls.")

for removeFile in remove_files:
    path = os.path.join(cwd, "release/zombie_calculator.dist", removeFile)
    if os.path.exists(path):
        os.remove(path)
for removeDir in remove_dirs:
    path = os.path.join(cwd, "release/zombie_calculator.dist", removeDir)
    if os.path.exists(path):
        shutil.rmtree(path)

print(Fore.GREEN + "Removation completed.\n", Fore.YELLOW + "Start compressing the program into 7zip.")

path = os.path.join(cwd, "release")
with py7zr.SevenZipFile(os.path.join(cwd, f"release/zombie_calculator_{getVersion()[2:]}v-release.7z"), 'w') as archive:
    os.chdir(path)
    archive.writeall("zombie_calculator.dist/")
if os.path.exists(os.path.join(path, "zombie_calculator.dist")):
    shutil.rmtree(os.path.join(path, "zombie_calculator.dist"))

print(Fore.GREEN + "Everything is done.")