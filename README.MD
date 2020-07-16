# What the hell is this

This is just a tech assesment, that I decided to do in Flask; rather than Java.

I like Python and Flask, why not.

This isn't perfect, but I did it in under 45 minutes ~

## How do I set this up?

I would first get a Python3 venv up and running

`python3 -m venv venv`

Activate it for your session

`source venv/bin/activate`

Install dependancies that I used (Not much for this at all)

`pip install -r requirements.txt`

Once that's all set, run it!

```
$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [15/Jul/2020 19:26:13] "GET / HTTP/1.1" 200 -
```

## How do I use the notes app?

Well you can curl it, but the default route isn't fun

```
$ curl http://127.0.0.1:5000/
You're not looking for me...Use the api kid!
```

How about we check all of the notes we currently have

```
$ curl http://127.0.0.1:5000/api/notes
{"notes":[{"body":"Buy car parts","id":1},{"id":2,"title":"Learn Elastic better"}]}
```

Hey now, that's better; but I only want note 2?

```
$ curl http://127.0.0.1:5000/api/notes/2
{"note":{"id":2,"title":"Learn Elastic better"}}
```

But I wanna add my own note, Mike!  I've got you covered

```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"body":"Listen to more DMB!"}' http://localhost:5000/api/notes
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 47
Server: Werkzeug/1.0.1 Python/3.7.7
Date: Thu, 16 Jul 2020 01:30:36 GMT

{"note":{"body":"Listen to more DMB!","id":3}}

$ curl http://127.0.0.1:5000/api/notes/3
{"note":{"body":"Listen to more DMB!","id":3}}
```
