#pywin32_draw.py
import win32gui, win32api

class draw:
    def __init__(self):
        hwnd = win32gui.GetDesktopWindow()
        self.hdc = win32gui.GetDC(hwnd)
    def rect(self, x, y, w, h, color=False):
        # color = (255,0,0) int type
        color = win32api.RGB(0,255,0) if not color else win32api.RGB(color[0], color[1], color[2])
        for i in range(x, x + w):
            win32gui.SetPixel(self.hdc, i, y, color)
            win32gui.SetPixel(self.hdc, i, y + h, color)
        for j in range(y, y + h):
            win32gui.SetPixel(self.hdc, x, j, color)
            win32gui.SetPixel(self.hdc, x + w, j, color)
