# fastAPI_project
This is a project made with the fastAPI framework, it consists of a db that saves the user info and can apply http requests to it (get, update, put and delete).

You can use postman in order to send this requests, or in case you are using it in your local machine, you can do it in http://localhost:8000/docs in your web browser.



USEFUL INFO:
--------------------------------------------------------------------------------------------------------------------------------

HTTP request methods used:

-GET

The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.


-POST

The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.

-PUT

The PUT method replaces all current representations of the target resource with the request payload.

-DELETE

The DELETE method deletes the specified resource.

--------------------------------------------------------------------------------------------------------------------------------


HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:
1. Informational responses (100 – 199)
2. Successful responses (200 – 299)
3. Redirection messages (300 – 399)
4. Client error responses (400 – 499)
5. Server error responses (500 – 599)

--------------------------------------------------------------------------------------------------------------------------------


General notes regarding the creation of this project:

-You can use id=UUID("the uuid") instead of id=uuid4() to have persistency in the UUIDs NOTE: you first need to import UUID from uuid

-You can do "from typing  import Optional" to have the option to have or not to have something

-With the POST requests you can submit a change in the server 

-We cannot send post requests with our web browser, instead we need to use a rest client(in this case, we used postman)

-We can send a POST request and insert JSON content into the body 

-We can use localhost:8000/docs to view the documentation created for our api  (created by default) this is in an interactive way, but if we want to access a non-interactive UI, we can use localhost:8000/redoc

-How can we show a 404 not found error? (in this case, we need it in the case that we are trying to delete an already deleted item)
First we need to import "HTTPException" from fastapi, then we apply a 
```
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
```
in the @app.delete part in order to send a 404 code if the user doesn't exists



