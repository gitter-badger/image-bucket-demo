from image_bucket import app
from flask import render_template, request, flash, session, url_for, redirect

@app.route('/')
def index():
    return render_template('loginsign.html')
