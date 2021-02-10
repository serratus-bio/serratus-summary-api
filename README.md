# serratus-summary-api

## Example routes

- [`/nucleotide/sra=ERR2756788`](https://api.serratus.io/nucleotide/sra=ERR2756788)
- [`/nucleotide/family=Coronaviridae`](https://api.serratus.io/nucleotide/family=Coronaviridae)
- [`/nucleotide/family=Coronaviridae?page=5&perPage=10`](https://api.serratus.io/nucleotide/family=Coronaviridae?page=5&perPage=10)
- [`/nucleotide/family=Coronaviridae?scoreMin=90&scoreMax=100&page=5`](https://api.serratus.io/nucleotide/family=Coronaviridae?scoreMin=90&scoreMax=100&page=5)
- [`/nucleotide/family=Coronaviridae?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/nucleotide/family=Coronaviridae?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)
- [`/nucleotide/genbank=EU769558.1`](https://api.serratus.io/nucleotide/genbank=EU769558.1)
- [`/nucleotide/genbank=EU769558.1?page=5`](https://api.serratus.io/nucleotide/genbank=EU769558.1?page=5)
- [`/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&page=5`](https://api.serratus.io/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&page=5)
- [`/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90`](https://api.serratus.io/nucleotide/genbank=EU769558.1?&scoreMin=90&scoreMax=100&identityMin=80&identityMax=90)

## Local usage

### Setup

Add file `env.sh`:

```sh
export SQL_USERNAME=XXXXX
export SQL_PASSWORD=XXXXX
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

## SQL indexes for optimal querying

```sql
CREATE INDEX nfamily_sra_id_index ON nfamily (sra_id);
CREATE INDEX nfamily_family_name_index ON nfamily (family_name);
CREATE INDEX nfamily_score_index ON nfamily (score);
CREATE INDEX nfamily_percent_identity_index ON nfamily (percent_identity);

CREATE INDEX nsequence_sra_id_index ON nsequence (sra_id);
CREATE INDEX nsequence_genbank_id_index ON nsequence (genbank_id);
CREATE INDEX nsequence_score_index ON nsequence (score);
CREATE INDEX nsequence_percent_identity_index ON nsequence (percent_identity);
CREATE INDEX nsequence_genbank_id_score_index ON nsequence (genbank_id, score);
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
    - Health check path: `/nucleotide/sra=ERR2756788`

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

## Debugging

- Disable caches: in `config.py` set `CACHE_DEFAULT_TIMEOUT = 1` (timeout after 1 second)

## TODO

- `/protein/*`
- `/rdrp/*`
- handle timeouts e.g.
    > DatabaseError: current transaction is aborted, commands ignored until end of transaction block
