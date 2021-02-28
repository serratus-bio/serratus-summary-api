# serratus-summary-api

## Example routes

- [`/summary/nucleotide/run=ERR2756788`](https://api.serratus.io/summary/nucleotide/run=ERR2756788)
- [`/matches/nucleotide/paged?family=Coronaviridae`](https://api.serratus.io/matches/nucleotide/paged?family=Coronaviridae)
- [`/matches/nucleotide/paged?family=Coronaviridae&page=5&perPage=10`](https://api.serratus.io/matches/nucleotide/paged?family=Coronaviridae&page=5&perPage=10)
- [`/matches/nucleotide/paged?family=Coronaviridae&scoreMin=90&scoreMax=100&page=5`](https://api.serratus.io/matches/nucleotide/paged?family=Coronaviridae&scoreMin=90&scoreMax=100&page=5)
- [`/matches/nucleotide/paged?family=Coronaviridae&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/matches/nucleotide/paged?family=Coronaviridae&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)
    - [`/matches/nucleotide?family=Coronaviridae&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/matches/nucleotide?family=Coronaviridae&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)
- [`/matches/nucleotide/paged?genbank=EU769558.1`](https://api.serratus.io/matches/nucleotide/paged?genbank=EU769558.1)
- [`/matches/nucleotide/paged?genbank=EU769558.1&page=5`](https://api.serratus.io/matches/nucleotide/paged?genbank=EU769558.1&page=5)
- [`/matches/nucleotide/paged?genbank=EU769558.1&scoreMin=90&scoreMax=100&page=5`](https://api.serratus.io/matches/nucleotide/paged?genbank=EU769558.1&scoreMin=90&scoreMax=100&page=5)
- [`/matches/nucleotide/paged?genbank=EU769558.1&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/nucleotide/genbank=EU769558.1&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)

## Local usage

### Setup

Add file `env.sh`:

```sh
export SQL_USERNAME=web_api
export SQL_PASSWORD=serratus
```

```sh
# [optional] create/load virtualenv
pip install -r requirements.txt
```

### Start server

```sh
bash run.sh
```

### Test

```sh
bash test.sh
```

## AWS Setup

### Elastic Beanstalk

- Application name: **serratus-summary-api-flask**
- Environment
    - Web server environment
    - Name: **serratus-summary-api**
    - Platform: Python (3.7 running on 64bit Amazon Linux 2)
    - Sample app (will be overidden by CodePipeline deployment)

After creation:

- Add load balancer listener
    - Port: 443
    - Protocol: HTTPS
    - SSL certificate: `*.serratus.io`
- Processes
    - Health check path: `/summary/nucleotide/run=ERR2756788`
- Environment variables
    - Add `SQL_USERNAME`, `SQL_PASSWORD` from to `env.sh`

### CodePipeline

1. Settings
    - Pipeline name: **serratus-summary-api-flask**
    - New service role
2. Source stage
    - Source provider: GitHub (Version 1)
    - Select this repo/branch
    - Change detection: GitHub webhooks
3. Build stage: skip
4. Deploy stage
    - Provider: AWS Elastic Beanstalk
    - Region: us-east-1
    - Application/environment names from above

### Route 53

- `A` record for `api.serratus.io` -> Elastic Beanstalk endpoint

### RDS

See https://github.com/ababaian/serratus/wiki/Serratus-SQL-Database-Management

## Debugging

- Disable caches: in `config.py` set `CACHE_DEFAULT_TIMEOUT = 1` (timeout after 1 second)

## TODO

- `/protein/*`
- `/rdrp/*`
- handle timeouts e.g.
    > DatabaseError: current transaction is aborted, commands ignored until end of transaction block
- investigate `CACHE_TYPE = 'filesystem'` and `CACHE_THRESHOLD`
