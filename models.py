from google.appengine.ext import ndb

class Post(ndb.Model):
	title = ndb.StringProperty(required=True)
	description = ndb.StringProperty(required=True)
	content = ndb.TextProperty(required=True)
	created_at = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
	username = ndb.StringProperty(required=True)
	