#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import webapp2
import jinja2

from models import Post
from datetime import datetime
from date_prettify import date_prettify

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)
jinja_env.filters['timesince'] = date_prettify

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainHandler(BaseHandler):
    def get(self):
    	posts = Post.query().order(-Post.created_at)
    	title = "My Project Blog"
    	description = "This is my cool blog"
        self.render('index.html', title=title, description=description, posts=posts)

class SignUpHandler(BaseHandler):
    def get(self):
        self.render('user/signin.html')
		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/user/signup', SignUpHandler)
], debug=True)
