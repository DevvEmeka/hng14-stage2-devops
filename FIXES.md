# FIXES DOCUMENTATION

This document contains all bugs found and fixed in the Stage 2 DevOps microservices application.

---

## Bug 1: Worker crashed with "r is not defined"

File: worker/worker.py  
Problem: Redis client was created but not assigned to a variable, causing NameError  
Fix: Assigned Redis connection to variable `r`  
Why: Python requires a variable reference before method calls like brpop()

---

## Bug 2: Worker Redis connection failed (localhost issue)

File: worker/worker.py  
Problem: Redis host set to localhost instead of Docker service name  
Fix: Changed host from localhost → redis  
Why: Docker containers communicate using service names, not localhost

---

## Bug 3: Frontend Dockerfile misnamed

File: frontend  
Problem: Dockerfile saved as Dockerfile.txt  
Fix: Renamed file to Dockerfile  
Why: Docker only recognizes files named exactly "Dockerfile"

---

## Bug 4: Docker networking issue (initial run failure)

File: docker-compose.yml  
Problem: Redis port conflict (6379 already in use)  
Fix: Removed external port binding for Redis  
Why: Redis should remain internal and not exposed externally

## Bug 5
File: frontend/app.js  
Problem: "Submitted: undefined" is shown on UI  
Cause: frontend expects "status" field but API does not return it correctly  
Fix: updated frontend logic to handle correct API response field or fallback value

## Bug 6
File: frontend/app.js
Problem: Frontend displays undefined after submit
Cause: Frontend likely reading wrong field from POST /jobs response
Fix: Investigating API response structure via Swagger

## Bug 7
File: frontend/app.js
Problem: Frontend used localhost to reach API inside Docker
Cause: In containers, localhost points to same container, not api service
Fix: Changed API_URL from http://localhost:8000 to http://api:8000

## Bug 8
File: Full stack integration
Problem: Services required validation after startup.
Cause: Needed end-to-end verification of queue processing.
Fix: Tested job submission flow successfully until completed status.

## Bug 9
File: docker-compose.yml
Problem: Redis was exposed to host and services lacked health-based startup ordering.
Fix: Removed Redis port exposure, added healthchecks, internal network, env vars, and resource limits.

## Bug 10
File: .gitignore
Problem: Temporary files and secrets risked being committed.
Fix: Added Python cache, node_modules, .env, dist, and pytest cache exclusions.

## Bug 11
File: CI/CD pipeline
Problem: Repository had no automated validation or deployment workflow.
Fix: Added GitHub Actions pipeline with lint, test, build, integration test, and deploy stages.

## Bug 12
File: api/main.py, worker/worker.py
Problem: CI pipeline failed due to flake8 linting errors (bare except, missing blank lines, and missing newline at end of file).
Fix: Replaced bare except with Exception handling, corrected PEP8 spacing (blank lines between functions and classes), and added missing newline at end of files.