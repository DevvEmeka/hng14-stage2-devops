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