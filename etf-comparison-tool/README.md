# ETF Comparison Tool

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

### Prerequisites

Make sure you have PostgreSQL installed and running on your system.

### Setting Up the Database

1. **Create the Database:**

    Open your terminal and start the PostgreSQL shell:
    ```bash
    psql -U postgres
    ```

    Once in the PostgreSQL shell, create a new database:
    ```bash
    CREATE DATABASE etf_database;
    ```

    Exit the PostgreSQL shell:
    ```bash
    \q
    ```

2. **Configure the .env File:**

    In the root directory of your project, create a .env file if it doesn't already exist. Add the following line to specify your database connection:
    ```bash
    DATABASE_URL="postgresql://postgres:<your_password>@localhost:5432/etf_database?schema=public"
    ```
    Replace <your_password> with your PostgreSQL password.

3. **Apply Prisma Migrations:**

    Run the following command to apply the database schema defined in Prisma:
    ```bash
    npx prisma migrate dev --name init
    ```
    This will create the necessary tables in your etf_database.

## Running the Development Server

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```
