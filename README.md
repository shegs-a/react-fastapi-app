## Deployment
1. To deploy the backend on your local machine do the following
  - cd into the `api` folder
  - create and activate virtual environment using `python3.10 -m venv env && source env/bin/activate`
  - install dependencies using `pip install -r requirements.txt`
  - start the app `python main.py`

  ### Default environment values
  These are some values that need to be provided before the app can run
  
| Name                              | Description                                              | Type   | Default Value           |
|-----------------------------------|----------------------------------------------------------|--------|-------------------------|
|`HNG_LESSON_DAY`                   | The day of the lesson assignment or practical            | String | "day1"                  |
| `HNG_API_ORIGINS`                 | The url of the frontend code for cors setting            | List   | 'http://localhost:3000' |
| `HNG_API_HOST`                    | The host where you want to deploy the code               | String | "localhost"             |
| `HNG_API_PORT`                    | The api port                                             | int    | 8000                    |

2. To deploy the frontend on your local machine do the following
  - cd into the `fe` folder
  - install the npm packages `npm install`
  - start the app `npm run start`

### Default environment values
| Name                              | Description                                              | Type   | Default Value           |
|-----------------------------------|----------------------------------------------------------|--------|-------------------------|
| `REACT_APP_API_URL`               | URL of the api endpoint                                  | String | <no-defaults>           |
| `REACT_APP_LESSON_DAY`            | The day of the lesson assignment of practical            | String | <no-defaults>           |
  
  The default `port` and `host` for the react app is `3000` and `localhost` respectively, these can be changed at runtime using the flags `--port <port>` and `--host <host>`

