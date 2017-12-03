import sys
import sdl2
import sdl2.ext

window_width, window_height = 640, 480

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Hello World!", size=(window_width, window_height))
    window.show()

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        window.refresh()
    return 0


if __name__ == "__main__":
    sys.exit(run())
