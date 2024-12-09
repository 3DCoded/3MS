# Legacy 3MS Docs

The 3MS will soon migrate completely to Happy Hare firmware. For users wanting to use the old software, follow the below instructions to run the documentation locally.

## Running Locally

1. Install [Python](https://python.org)
2. Install [Pipenv](https://pypi.org/project/pipenv/)
3. Clone this repository

    ```
    git clone https://github.com/3DCoded/3MS
    ```
4. Select `docs-legacy`

   ```
   cd 3MS
   git checkout docs-legacy
   ```
5. Install dependencies

   ```
   pipenv install
   pipenv shell
   ```
6. Run the documentation

   ```
   mkdocs serve
   ```

The documentation will be available at [localhost:8000](http://localhost:8000)
