from flask import Flask, render_template
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Flask(__name__)



# Add a route to serve your CSS file
@app.route('/css/<filename>')
def serve_css(filename):
    return app.send_static_file('css/' + filename)

# Add a route to serve your image files
@app.route('/IMG/<filename>')
def serve_images(filename):
    return app.send_static_file('IMG/' + filename)

# Add a route to serve your JavaScript files
@app.route('/js/<filename>')
def serve_js(filename):
    return app.send_static_file('js/' + filename)

# Add routes for specific HTML pages
@app.route('/')
def serve_index():
    return render_template('index.html')


@app.route('/blog')
def serve_blog():
    return render_template('blog.html')

@app.route('/request-estimate')
def serve_request_estimate():
    return render_template('request-estimate.html')

@app.route('/service')
def serve_service():
    return render_template('service.html')

@app.route('/identify-issue')
def serve_identify_issue():
    return render_template('identify-issue.html')

@app.route('/filter-maintenance')
def serve_filter_maintenance():
    return render_template('filter-maintenance.html')




if __name__ == '__main__':
    if sys.platform == 'win32':
        # Windows-specific code
        import msvcrt
        # Perform Windows-specific file operations using msvcrt

    # Function to handle changes and restart the server
    def on_change(event):
        print("Change detected. Restarting the server.")
        observer.stop()
        observer.join()
        app.run(host='0.0.0.0', port=8000, threaded=True)

    # Create a watchdog event handler
    class FileChangeHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            on_change(event)

    # Set up the observer to watch for file system changes
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    app.run(host='0.0.0.0', port=80, threaded=True)