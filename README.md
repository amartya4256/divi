# DIVI - A.I. Assistant
## WHAT IS D.I.V.I.? 

D.I.V.I. stands for Desktop Imbrutization using Virtual Intellect. It is a virtual assistant capable of running on any machine irrespective of platform. D.I.V.I. is mainly developed in Python & Java and is a platform independent software capable of providing you virtual support in almost every field, such as, home automation, chatbot, device management, remote access to any of your device, managing your virtual information and resources, etc. It can be used in the corporate sector to break business barriers, as it is readily available to take the responsibility of the admin system.
D.I.V.I. is a software that can be installed on either laptop or mobile phone, running any OS, such as, Windows, IOS, Android, Linux, etc. D.I.V.I. is an easy-to-use handy application. It features a familiar and well-thought-out, an attractive interface, combined with high virtual intelligence. The custom chatbot of D.I.V.I. can easily compel its user in a long conversation.
D.I.V.I. has 3 major modules :
1. D.I.V.I. Interface
2. Application Backend
3. Main server
D.I.V.I. works on a decentralized system model as all the modules are running independently and interacting with each other to get the jobs done. D.I.V.I. stands out to be very reliable for both personal as well as official purposes.
The application is easily installable through the installer package (Setup). Users just have to sign up and register their device with the system to get it running in no time. D.I.V.I. is a very light application which doesn’t consume any significant resource of the system and is very small in size. So, users never have to worry about running out of space due to the application.

## DEVELOPMENT PHASES
The application development process is carried out in 6 phases :
1. Requirement Analysis
2. UI/UX design and application design
3. Web Scraping, data pre-processing and model development
4. Client and Chatbot server development
5. Integration and testing
6. Packaging

The whole development phase comprises of development of  total of 3 modules:
1. D.I.V.I. Interface
2. Application Backend
3. Main Server

## APPLICATION WORKFLOW
The application workflow is a sequence of tasks that processes a set of data. Workflows occur across every kind of business and industry. Anytime data is passed between humans and/or systems, a workflow is created. Workflows are the paths that describe how something goes from being undone to done, or raw to processed.
In D.I.V.I., the User is allowed to interact with the user interface through where any exchange of data starts. The data is passed to the modules on the basis of requirements.

## LOGIN, LOGOUT, REGISTRATION AND FORGOT PASSWORD
When users start the app for the first time, he/she is asked to login. The user can also create a new account using the Sign up button. If a user has forgotten the password, he/she can enter his/her email address to receive the credentials of his/her account on the mail through D.I.V.I. SMTP server. The user can log out of the device whenever he/she wants. After logging in, the user lands on the D.I.V.I. main interface, from where he/she can make several requests to the application.


## USER REQUESTS
The user is allowed to send any data using the interface. The interface uses the fetch/XHR request to send requests. All the requests from the user interface are sent to the Application backend at first. There is a list of operations, a user can send as a request to the application backend. They are :
Local system execution : These kinds of requests are made to access any application within the local device.
Remote device access : These requests are used to access any remote device within user permit.
Registration, Login, Logout and forgot password : These are the session based requests.
Chatbot communication : These requests are use to communicate with chatbot
Speak request : It enables the microphone and the application starts listening to what the user wants to say.
DECIDER
Decider is a backend sub-module. It listens to the request of the user and resolves which kind of request it is. The decider builds its own regular expression on experience with the user and categorizes requests efficiently. The four major categorization it does are :
Local application execution
Chatbot request
IOT based request
Remote device access request
Based on which category, request lies in, it forwards the request.
The decider, locally comprises multiple features, such as, effective file searching, application searching and other features. It checks for the request and if it matches none then it forwards the request to chatbot, identifying as a chatbot request. If the request is executed and finished on the backend itself then it would send a response to the user interface and show it on screen.

## AUTHORIZATION
 The authorization protocol is run both at Application backend and server to promise 100% security. The cookies are stored on the device in the application and verified on every action with the server. When a user opens the application, the application checks for the session and then gives access to the user. If the session has expired, he/she is automatically logged out of application. Then, he/she will have to login again.

## MAIN SERVER FUNCTIONALITY
The main server, when receiving a request at a controller, would map the request to the respective function and would execute it. It’s major functionalities are authorization, authentication, database queries, managing sessions, managing devices, chatbot, etc. Server would send a response after executing the request.

## REMOTE LISTENER
Remote listener is a HTTP Server running on port 16286 which connects with the decider running on the backend to perform actions. A remote listener would listen to all the requests coming on the port and authenticate it before executing the request. If the request is unauthenticated, it would not execute it.





The work flow of remote listener is as follows:
User requests to access one of his/her devices remotely.
Decider identifies it to be a remote device access request and checks if the device is accessible to the user.
Decider forwards the request to the server.
Server authenticates the request and forwards the request to the remote listener port of the targeted device.
The remote listener of the targeted device receives the request and authenticates it and further passes it on to the decider on its application backend.
The decider would identify the action and execute it and send a response back to the remote listener on the same system.
The remote listener would send the response back to the server which would be forwarded to the decider of the source system.
The decider of source on receiving the response would respond to the interface which would display the response on the screen.

