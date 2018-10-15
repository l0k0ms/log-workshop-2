# Distributed Tracing with APM Workshop

This is a repository for a log workshop based on [2018 Dash APM Workshop](https://github.com/burningion/dash-apm-workshop) made by [Burningion](https://github.com/burningion).

# Before the Workshop / Prerequisites

The workshop is scheduled for an hour and a half. In this short time frame, having prerequisites installed is crucial to maximize everyone's hands on time.

Please ensure you accomplished the following steps before the event:

1. Install [Docker CE](https://store.docker.com/search?type=edition&offering=community).

2. Install [Docker Compose](https://docs.docker.com/compose/install/).

3. Clone this repository on your local machine: ```git clone https://github.com/l0k0ms/log-workshop-2.git```

4. Pull Docker images to your local machine **before the event**, so we don't all overwhelm the WiFi: `docker-compose up` (this make take several minutes).
    When it finishes, load [http://localhost:5000](http://localhost:5000) in a private window and check that everything is up and running. 

5. (Optional) The workshop itself is written in a [Jupyter notebook](http://jupyter.org/), allowing you to mix and edit content locally. 
    If you want to be able to add notes and save them locally, [install Jupyter](http://jupyter.org/install), and then open the `log_workshop_instructions.ipynb` by doing a `jupyter-notebook` in the workshop directory.
    This is completely optional, as Github has a built in viewer for Jupyter notebooks. [Check the repository notebook](https://github.com/l0k0ms/log-workshop-2/blob/master/log_workshop_instructions.ipynb).

# Running the Application

![Water Sensor App](https://github.com/burningion/distributed-tracing-with-apm-workshop/raw/master/images/dashboard.png)

1. If not done already [create a Datadog account](https://app.datadoghq.com/signup). A free trial should work to play with.

2. (Optional) - If the application was already running, stop it with the following command: `docker-compose stop && docker-compose rm`

3. Launch the application with the following parameters:

    ```bash
    POSTGRES_USER=postgres POSTGRES_PASSWORD=122356 DD_API_KEY=<DATADOG_API_KEY> docker-compose up
    ```
    Replace `<DATADOG_API_KEY>` by the [API key provided for your Datadog platform](https://app.datadoghq.com/account/settings#api).

4. Then open the web app at [http://localhost:5000](http://localhost:5000), create some pumps and cities.

5. Finally follow the [instructions of this workshop](https://github.com/l0k0ms/log-workshop-2/blob/master/log_workshop_instructions.ipynb).
