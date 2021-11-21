from django.db import models
import re
import bcrypt
from django.db.models.deletion import CASCADE

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['firstName']) < 2:
            error['firstName'] = "First Name must be at least 2 characters"

        if len(form['lastName']) < 2:
            error['lastName'] = "Last Name must be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Format'

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email addres is already in use'

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] ='Sorry that username has been taken please chose a different one'

        if len(form['password']) < 5:
            errors['password'] = 'Password must be at least 5 characters long'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Password do not match'

        return errors

    def authenticate(self, username, password):
        users = self.filter(username=username)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            firstName = form['firstName'],
            lastName = form['lastName'],
            email = form['email'],
            username = form['username'],
            password = pw,
        )

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=255)

    objects = UserManager()

class Page(models.Model):
    page = models.CharField(max_length=255)

class Type(models.Model):
    theType = models.CharField(max_length=255)

class Topic(models.Model):
    topic = models.CharField(max_length=255)

class Link(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    page = models.ForeignKey(Page, related_name='pages', on_delete=CASCADE)
    theType = models.ForeignKey(Type, related_name='types', on_delete=CASCADE)
    topic = models.ForeignKey(Topic, related_name='topics', on_delete=CASCADE)
    order = models.IntegerField()