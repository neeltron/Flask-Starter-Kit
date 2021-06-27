from flask import Flask, render_template



app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page
@app.route('/')
def index():
  return render_template('index.html')



# Creating different routes
@app.route('/second')
def second():
  return "I'm on a separate route"



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
