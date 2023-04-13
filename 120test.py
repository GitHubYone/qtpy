import tkinter as tk
import imageio

class VideoPlayer(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.grid(sticky="NEWS")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, columnspan=3, sticky="NEWS")
        self.play_button = tk.Button(self, text="Play", command=self.play)
        self.play_button.grid(row=1, column=0, sticky="W")
        self.pause_button = tk.Button(self, text="Pause", command=self.pause)
        self.pause_button.grid(row=1, column=1, sticky="W")
        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.grid(row=1, column=2, sticky="W")
        self.after_id = None

    def play(self):
        self.stop()
        self.video = imageio.get_reader("./dualHA_BSH2.mp4")
        self.stream = self.video.iter_data()
        self.play_next_frame()

    def play_next_frame(self):
        try:
            frame = next(self.stream)
        except StopIteration:
            self.video.close()
            return
        self.photo = tk.PhotoImage(data=frame)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.after_id = self.after(33, self.play_next_frame)

    def pause(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            self.after_id = None

    def stop(self):
        self.pause()
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    app.mainloop()
