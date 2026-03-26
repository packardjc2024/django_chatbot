# **Website Builder**

### Description

The Webstie Builder is a application to quickly spin up a new Django application. It use Docker and docker compose but abstracts all of the code away so that the only thing that needs to change to start a new basic web application is the configuration file (currently .env). 

---

### Layout

The weather app is a single page web application. From top to bottom the sections are:  

- The locations that have already been selected and stored in the database are at the top of the page. The name and high and low for the current day are listed.
- The next section contains a form for adding a new location.
- The final section is where the full forecasts are displayed for the selected locations

---

### Use

- Edit the .env file to change basic configurations
- Run [run_dev.sh](./run_dev.sh) to spin up the localhost development application. 
- Begin working on the specifics of your new application!

---

### Technologies Used

- Python
- Django
- HTML/CSS
- Ubuntu
- Docker
- Bash
- Nginx
- PostgreSQL


---

### Build

The application is built using Docker on Ubuntu. Nginx is on the host server while the database and python code are containerized. All of the complexities of building and running the app are abstracted away in [run_dev.sh](./run_dev.sh) for development and [run_prod.sh](./run_prod.sh) for production. run_prod.sh does the following:

- Pulls the latest version from GitHub
- Manipulates files and permissions as necessary to enable persistent storage.
- Builds the containers and deploys using `docker compose up --build -d`

---

### Links

- [Production App](https://test.programmingondemand.com)
- [GitHub Code](https://github.com/packardjc2024/website_builder)
- [Portfolio](https://www.programmingondemand.com)


