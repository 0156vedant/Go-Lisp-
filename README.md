# Go-Lisp-
The Go Lisp project seeks to build an interactive Lisp interpreter, leveraging the robust performance of C++ for backend processing and the flexibility of modern web development technologies like HTML, JavaScript, and FastAPI for the frontend and middleware. 

Dependencies:
pip , c++ compiler, python, javascript, fastApi

Project Link: https://go-lisp.vercel.app/

Backend Development:
Created a FastAPI application (server.py) to handle Lisp code execution.
Integrated a C++ interpreter (wisp2.cpp) using subprocess.
Tested the backend locally using uvicorn.

Frontend Development:
Built a user interface (index.html) to allow users to write and run Lisp code.
Added functionality to send code to the backend API and display the output.

Hosting Backend:
Uploaded the project to a Git repository.
Deployed the backend on Render with a build command to compile the C++ file and run the FastAPI server.

Hosting Frontend:
Hosted the frontend (index.html) on GitHub Pages.
Updated the API endpoint in the frontend to point to the Render-deployed backend. 

CORS Configuration:
Configured CORS in the backend to allow requests from the frontend domain (https://0156vedant.github.io).

Testing and Debugging:
Verified the backend routes and frontend API integration locally.
Fixed errors like CORS policy and 404 by updating configurations and redeploying the backend.
