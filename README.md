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

To produce the MVP within the time-frame provided i realised that the application i was building would be less important than the implementation of my CI/CD, so my application is quite simple.

Meal Maker
<br>Service 1: Displays the results of the following 3 services to the user
<br>Service 2: returns a random main dish
<br>Service 3: returns a random side dish
<br>Service 4: returns a total price based off service 2 and 3

Here is my ED for my application
<br>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/RHpgkH0/Project-2-ed.jpg" alt="Project-2-ed" border="0"></a>

Project tracking
 
I used trello to track my progress of development throughout the development process. The image below is a screenshot of my board and the link to my board is [here](https://trello.com/b/KcwQIRcu/qa-project-2)

Risk assesment

Here is the updated risk assessment for my project.

<a href="https://ibb.co/Vv0Yzkk"><img src="https://i.ibb.co/gDbZfcc/Screenshot-16.png" alt="Screenshot-16" border="0"></a>
<a href="https://ibb.co/T4hz5fh"><img src="https://i.ibb.co/2vKXB9K/Screenshot-18.png" alt="Screenshot-18" border="0"></a>

Continuous Intergration pipeline

Here is a diagram for the CI/CD

<a href="https://ibb.co/z2Vr5M0"><img src="https://i.ibb.co/hdFyM6t/Screenshot-22.png" alt="Screenshot-22" border="0"></a>

Services diagram

Here is a diagram illustrating the interaction between the 4 services in my app.

<a href="https://ibb.co/MNjK98K"><img src="https://i.ibb.co/LpqBvQB/Screenshot-24.png" alt="Screenshot-24" border="0"></a>
