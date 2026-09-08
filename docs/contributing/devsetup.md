---
icon: octicons/terminal-24
comments: true
---

# Development Setup

Follow this guide to setup your system for development with the 3MS. 

## Documentation Changes

1. Fork the 3MS repository
1. Create a new branch for your pull request (from the `docs` branch)
1. Install [Python](https://www.python.org/).
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
1. In your terminal, navigate to the 3MS folder, and run:
    ```sh
    uv venv
    uv sync
    ```
1. Develop changes in the new branch, using the following command to run the documentation locally:
    ```sh
    ./run.sh serve
    ```