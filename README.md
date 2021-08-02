Objective
The objective provided for this project is as follows:

To create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

More specifically, these 4 services should comprise of 1 front-end wrapper service, 2 (or more) back-end services, and 1 other back-end service that relies on data from the previous 2 back-end services in some way.

The following constraints were also set:

Kanban Board: Asana or an equivalent Kanban Board <br>
Version Control: Git - using the feature-branch model <br>
CI Server: Jenkins <br>
Configuration Management: Ansible<br>
Cloud server: GCP virtual machines<br>
Containerisation: Docker<br>
Orchestration Tool: Docker Swarm<br>
Reverse Proxy: NGINX<br>
Database Layer: MySQL<br>

Proposal

To produce the MVP within the time-frame provided i realised that the application i was building would be less important than the implementation of my CI/CD, so my application is quite simple

Meal Maker
<br>Service 1: Displays the results of the following 3 services to the user
<br>Service 2: returns a random main dish
<br>Service 3: returns a random side dish
<br>Service 4: returns a total price based off service 2 and 3

Project tracking
 
I used trello to track my progress of development throughout the development process. The image below is a screenshot of my board and the link to my board is [here](https://trello.com/b/KcwQIRcu/qa-project-2)
