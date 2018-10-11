# Distributed Tracing with APM Workshop

This is repo for a log workshop based on [2018 Dash APM Workshop](https://github.com/burningion/dash-apm-workshop) made by [Burningion](https://github.com/burningion).

# Running the Application

![Water Sensor App](https://github.com/burningion/distributed-tracing-with-apm-workshop/raw/master/images/dashboard.png)

You'll need to have a Datadog account with APM and logging enabled. A free trial should work to play with.

```bash
$ POSTGRES_USER=postgres POSTGRES_PASSWORD=<pg password> DD_API_KEY=<api key> docker-compose up
```

You can open the web app at `http://localhost:5000`, create some pumps, and look at your Datadog traces to see the distributed traces.

The frontend of the app is a React node app using [Material UI](https://material-ui.com/). It lives in the `single-page-frontend` folder. You can start it up for development with a:

```bash
$ npm install
$ npm start
```

It should connect to the running frontend API container, allowing for easier development. When you're finished making changes, you can do a `npm build`, and then copy the javascript from the `build` subdirectory into the Flask frontend app.