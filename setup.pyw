from cx_Freeze import setup, Executable # us this module to make an executable file"

setup(name = "test" ,#giving name to the exe
      version = "0.1" , # giving version to the exe
      description = "" ,  # giving description to the exe
      executables = [Executable("hello.pyw")]) # giving command to make an excutable
# for the file hello.pyw

#for amkeing an exe file we need to dir through command prompt where the file is located
# use command "python "file name.pyw" build"p
