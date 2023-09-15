# Getting Started

First, run the development server:

## Client Side

    ```bash
    cd client

    npm i

    npm run dev
    # or
    yarn dev
    # or
    pnpm dev
    ```

    Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Server Side

    ```bash
    cd server

    python3 -m venv .venv

    pip install Flask

    . .venv/bin/activate

    flask --debug run
    ```

    Open [http://127.0.0.1:5000](http://127.0.0.1:5000) with your browser to see the result.
