# Moodle-Submissions-Viewer
A python website viewer for online-text submissions of assignment activity on Moodle. 

# Install
Install Flask
```
pip install -U Flask
```

# Deploy and View Submissions
1. Download submissions on Moodle (Download submissions in folders) and unzip the folder.
1. Put viewer.py, the templates folder and the unzipped folder together.
1. Run ```python viewer.py <folder_name> <port_number>```. Recommended port number is 5000. Use a different port if you run multiple instances.
1. Open the displayed link in a web browser.
