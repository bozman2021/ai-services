# AI-Services ㊙️ 😶‍🌫️

### Inspired from these sites:
<br>
Collected over time:<br><br>
Host your own Local AI <br>
🎥 (https://www.youtube.com/watch?v=E2GIZrsDvuM)
<br><br>


# Installation

**Prerequisites**

- **Docker Desktop**
- **Python 3.8** or newer
- **Git 2.27** or newer

**Install Copier**

On Linux:
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install copier
```

Note that you probably need to start another terminal after installing ``pipx`` to make the pipx command available.

**Create a Folder for the Docker Stack**

If you keep all you docker stacks in a directory like $HOME/docker-stacks, you can use the following commands to create the Llama Tunnel stack in a new sub-directory.

macOS and Linux:
````
STACK_DIR="$HOME/docker-stacks/ai-services"
mkdir -p $STACK_DIR
cd $STACK_DIR
````

**Create a Data Directory for cloudflared**

````
mkdir -p ./data/flowise ./data/n8n/backup \
 ./data/api \
 ./data/functions \
 ./data/flowise \
 ./data/postgres_storage \
 ./data/n8n/backup/workflows \
 ./data/logs \
 ./data/shared \
 ./data/qdrant_storage \
 ./data/kong/api \
 ./data/supabase/imageproxy/storage \
 ./data/supabase/vector/logs \
 ./data/supabase/pooler \
 ./data/supabase/storage \
 ./data/supabase/edge/functions 

````

**Create the Project from the Template**

Create the project from the template with copier and answer the questions. If you forgot the tunnel id, you can find it in the data/cloudflared/credentials.json file or see it with cloudflared tunnel list.
````
copier copy gh:bozman2021/ai-services .
````

This will create a new directory in the STACK_DIR with the all the files necessary to run the tunnel.




**Start the Services**

Change into the project directory and start the services in the foreground:

**First start the supabase services.

````
docker compose -f docker-compose-supa.yml up --build
````
_in detached mode_

````
docker compose -f docker-compose-supa.yml up --build -d
````
wait 1 mim.

Second start the n8n services.

````
docker compose -f docker-compose-n8n.yml up --build
````
_in detached mode_

````
docker compose -f docker-compose-n8n.yml up --build -d
````




Easy chart over dependecies.
(https://mermaid.js.org/#/)<br>

```mermaid
graph TD;
    Client_on_Internet-->|202|Caddy;
    Caddy-->OpenWebUI;
    OpenWebUI-->Ollama;
    Ollama-->N8N;
    N8N-->Supabase;
    Supabase-->Studio;
    Supabase-->Kong;
    Supabase-->Auth;
    Supabase-->Rest;
    Supabase-->Realtime;
    Supabase-->Storage;
    Supabase-->ImgProxy;
    Supabase-->Meta;
    Supabase-->Functions;
    Supabase-->Analytics;
    Supabase-->PostgresDB;
    Supabase-->Vector;
    Supabase-->Supavisor;
    OpenWebUI-->N8N;
    N8N-->OpenWebUI;
    OpenWebUI-->LiteLLM;
    Ollama-->LiteLLM;
    Ollama-->Supabase;
    Web4ui-->Supabase;
    Web4ui-->Documentation;
    Web4ui-->Internet;
    Internet-->Savyint_Documentation;
    Internet-->Sailpoint_Documentation;
    Internet-->Opentext_Documentation;
    Internet-->Cyberark_Documentation;
    Internet-->ID-North_Documentation;
    Client_on_Internet-->|403|Ollama_gets_403_error;

```
