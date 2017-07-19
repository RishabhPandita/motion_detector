# motion_detector

Using cv2 this applicaiton captures inital frame as a reference and then keep on capturing frame and calculating delta, 
if there is a significant delta found between two frames it stores that in a csv file. At the end it shows a list of start 
and end time point when there was any movement in front of the camera. Using this data it then uses bokeh to plot a graph 
as a html file for the user. 

In order to calculate delta between two frames it converts the frame into binary frame with respect to the reference frame 
using cv2.absdiff and cv2.threshold. After this number of contours are calculated of the same frame. If that area crosses a
threshold it identifies it as movement in the new frame and stores  it. 

This can be easily run on a raspberry pi with a camera hardware and we will have a security recipe. 

Python libraries used
1) cv2    : http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html
2) pandas : pandas.pydata.org
3) bokeh  : http://bokeh.pydata.org/en/latest/

