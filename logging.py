import datetime
class Logger:
    def __init__(self) -> None:
        x = str(datetime.datetime.now()).replace(":", " ")
        self.file = open(str(x) + ".log", "w+")
    def info(self, text):
        x = datetime.datetime.now()
        self.file.writelines(f"[{x}] {text}\n")
    def criticalError(self, text):
        x = datetime.datetime.now()
        self.file.writelines(f"[{x}] !!! critical Error !!! {text} !!! critical Error !!!\n")
    def end(self):
        self.file.close()