# serratus-summary-api

## Example routes

- [`/index/run=ERR2756788`](https://api.serratus.io/index/run=ERR2756788)
- [`/summary/nucleotide/run=ERR2756788`](https://api.serratus.io/summary/nucleotide/run=ERR2756788)
- [`/matches/nucleotide/paged?family=Coronaviridae`](https://api.serratus.io/matches/nucleotide/paged?family=Coronaviridae)
- [`/matches/nucleotide/paged?family=Coronaviridae&page=5&perPage=10`](https://api.serratus.io/matches/nucleotide/paged?family=Coronaviridae&page=5&perPage=10)
- [`/matches/nucleotide/paged?family=Coronaviridae&scoreMin=90&scoreMax=100&page=5`](https://api.serratus.io/matches/nucleotide/paged?family=Coronaviridae&scoreMin=90&scoreMax=100&page=5)
- [`/matches/nucleotide/paged?family=Coronaviridae&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/matches/nucleotide/paged?family=Coronaviridae&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)
    - [`/matches/nucleotide?family=Coronaviridae&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/matches/nucleotide?family=Coronaviridae&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)
- [`/matches/nucleotide/paged?sequence=EU769558.1`](https://api.serratus.io/matches/nucleotide/paged?sequence=EU769558.1)
- [`/matches/nucleotide/paged?sequence=EU769558.1&page=5`](https://api.serratus.io/matches/nucleotide/paged?sequence=EU769558.1&page=5)
- [`/matches/nucleotide/paged?sequence=EU769558.1&scoreMin=90&scoreMax=100&page=5`](https://api.serratus.io/matches/nucleotide/paged?sequence=EU769558.1&scoreMin=90&scoreMax=100&page=5)
- [`/matches/nucleotide/paged?sequence=EU769558.1&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/matches/nucleotide/paged?sequence=EU769558.1&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)
- [`/counts/nucleotide?family=Coronaviridae`](https://api.serratus.io/counts/nucleotide?family=Coronaviridae)
- [`/counts/nucleotide?sequence=EU769558.1`](https://api.serratus.io/counts/nucleotide?sequence=EU769558.1)
- [`/list/nucleotide/family`](https://api.serratus.io/list/nucleotide/family)
- [`/list/nucleotide/sequence`](https://api.serratus.io/list/nucleotide/sequence)
- [`/palmprint/run=ERR2756788`](https://api.serratus.io/palmprint/run=ERR2756788)


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

## (Beta) Data API

The Data API is meant to be a general purpose interface for accesing the data in the serratus db. It is a thin REST layer on top of the db that lets you access any of its tables (as one would do with SQL) in a uniform and predictable way.

The Data API resides on the `/data` endpoint. Each table is mapped to path in this endpoint like `/data/<table>`.

### POST Request

The primary way to request data from the Data API is through a POST request to any `/data/<table>` path with a JSON payload that may contain some of the following keys:

- **offset**: retrieves rows from the specified offset, defaults to **0**
- **limit**: number of rows to retrieve, defaults to **8**

- **<column_name>**: if a column is a primary key, one could pass (a single or) a list of values to limit the query to a subset of matches, if they exist. In code, this adds a `WHERE <column_name> in (values)` clause to the query.

### GET Request

GET requests to any `/data/<table>` path get resolved by translating them to a corresponding POST request, as follows:

- The path remains the same.
- Any URL parameters in the GET request are sent as part of the JSON payload of the POST request. Example: `?param_one=one&param_two=two&param_three=three` will send a `{"param_one":"one","param_two":"two","param_three":"three"}` payload.
- All parameters are mapped as string values and no further syntactic transformations are considered at the moment.

GET requests are meant for trivial queries to the db and one big difference against POST requests is that all of them are cached for (at least) a day.

### Authentication

The Data API uses [HTTP Basic authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).

The credentials are `serratus:serratus`.

This doesn't do much at the moment but is it in place in case we need some sort of access/rate control in the future, ... also to make sure that you read this small guide before using the API.

### Examples

Sample POST request to get data of two `run_ids`s from the `rfamily` table:

```sh
curl -H 'Content-Type: application/json' -X POST -d '{"limit":8,"offset":0,"run_id":["DRR000614","DRR001252"]}' -u 'serratus:serratus' https://api.serratus.io/data/rfamily
```

Same query using a GET request and default field values:

```sh
curl -u 'serratus:serratus' https://api.serratus.io/data/rfamily?run_id=DRR000614,DRR001252
```

Sample response:

```sh
{
  "data": [
    {
      "run_id": "DRR000614",
      "phylum_name": "Kitrinoviricota",
      "family_name": "Alphaflexiviridae",
      "family_group": "Alphaflexiviridae-1",
      "coverage_bins": "___________________:_____",
      "score": 1,
      "percent_identity": 73,
      "depth": 0.1,
      "n_reads": 2,
      "aligned_length": 22
    },
    ... x 10 times
  ]
}
```

Errors look like:

```sh
{
  "error": "<some error message>"
}
```

For examples on how to make HTTP requests in your favorite framework/language, take a look at [this site](https://www.google.com).
