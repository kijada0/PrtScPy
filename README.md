# PrtScPy
### Tool for automatic screenshots during the presentation and online meeting

---

### How it works
Script takes screenshots of the screen, then compares them with the previous one. If the difference is greater than the threshold, the screenshot is saved to the specified directory. The script also plays a sound after each saved screenshot.
\
\
Comparison involves first resizing the old and new screenshot and then calculating the absolute difference between them. Performs grayscale conversion, dilation and thresholding to highlight pixel differences. The contours of the thresholded image are then found and returned as areas representing the different areas between the two images.

---

### Python Dependencies
- OpenCV
- PyAutoGUI
- playsound
- imutils
- numpy

--- 

### Configuration
- target_directory - directory where screenshots will be saved 
- sound_path - path to sound file which will be played after each screenshot
- start - start of capturing screenshots
- size - size of the screenshot
- height - height of the screenshot for analysis

