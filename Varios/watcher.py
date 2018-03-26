import time, os, sys
sys.path.append("../tools")
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class Handler(PatternMatchingEventHandler):

    def __init__(self):
        PatternMatchingEventHandler.__init__(self, patterns=["*/init.js"])

    def on_modified(self, event):
        have_compressor = []

        try:
            # tools/closure_library_jscompiler.py from: 
            #       http://code.google.com/p/closure-library/source/browse/trunk/closure/bin/build/jscompiler.py
            import closure_library_jscompiler as closureCompiler
            have_compressor.append("closure")
        except Exception as E:
            print("No closure (%s)" % E)

        use_compressor = None
        if 'closure' in have_compressor:
            use_compressor = options.compressor

        print "Archivo : %s %s"  % event.src_path % event.src_path
        #content = open(event.src_path, "U").read()
        path = os.path.normpath(event.src_path).split(os.path.sep)
        dest = os.path.join(path[0], 'init.min.js').replace('\\', '/')
        #open(dest, "w").write(content)

        if use_compressor == "closure":
            jscompilerJar = "../tools/closure-compiler.jar"
            if not os.path.isfile(jscompilerJar):
                print("\nNo closure-compiler.jar; read README.txt!")
                sys.exit("ERROR: Closure Compiler \"%s\" does not exist! Read README.txt" % jscompilerJar)
            
            minimized = closureCompiler.Compile(
                jscompilerJar, 
                sourceFiles, [
                    "--externs", "closure-compiler/Externs.js",
                    "--jscomp_warning", "checkVars",   # To enable "undefinedVars"
                    "--jscomp_error",   "checkRegExp", # Also necessary to enable "undefinedVars"
                    "--jscomp_error",   "undefinedVars"
                ]
            ).decode()
            if minimized is None:
                print("\nAbnormal termination due to compilation errors." )
                sys.exit("ERROR: Closure Compilation failed! See compilation errors.") 
            
            print("Closure Compilation has completed successfully.")
            print("\nAdding license file.")
            minimized = open("license.txt").read() + minimized

            print("Writing to %s." % dest)
            open(dest, "w").write(minimized)
            print("Hecho.")
        else
            print("Hubo un error")


    on_created = on_modified

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(Handler(), path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
