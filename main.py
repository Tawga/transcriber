from ui import Ui
from transcriber import Transcriber


def main():
    transcriber = Transcriber()
    ui = Ui(transcriber)

if __name__ == "__main__":
    main()    
