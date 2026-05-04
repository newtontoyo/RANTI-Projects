#Cloud-Native Voting Application (OpenShift)

A full **event-driven microservices application deployed on OpenShift CRC, demonstrating real-time data processing using Redis queues and PostgreSQL persistence.

---

##Overview

This project implements a distributed voting system where users can vote for **Cats or Dogs, with results updated in near real-time.

The system is built using a **microservices architecture** and deployed on Kubernetes via OpenShift, showcasing service-to-service communication, containerization, and platform-native builds.

---

##Architecture

Browser
   ↓
OpenShift Route
   ↓
Nginx (Frontend + Reverse Proxy)
   ↓
Vote API (Flask)
   ↓
Redis (Queue)
   ↓
Worker (Background Processor)
   ↓
PostgreSQL (Persistence)
   ↓
Results API (Flask)


---

##Tech Stack

* **Container Platform:** OpenShift
* **Web Server / Proxy:** Nginx
* **Backend APIs:** Python (Flask)
* **Queue:** Redis
* **Database:** PostgreSQL
* **Build System:** OpenShift BuildConfig (binary builds)
* **Containerization:** Docker

---

##How It Works

1. Uer clicks **Vote Cats or Dogs**
2. Frontend sends request to `/vote`
3. Vote API pushes message to Redis queue
4. Worker consumes messages from Redis
5. Worker writes vote into PostgreSQL
6. Results API aggregates vote counts
7. Frontend polls `/results` and updates UI

---

##Microservices

| Service      | Description                                      |
| ------------ | ------------------------------------------------ |
| **nginx**    | Serves UI and routes traffic to backend services |
| **vote**     | Receives votes and pushes to Redis               |
| **redis**    | Acts as a message queue                          |
| **worker**   | Processes votes and writes to DB                 |
| **postgres** | Stores votes                                     |
| **results**  | Aggregates and returns vote counts               |

---

##Deployment Steps (OpenShift)

### 1. Create Project

bash
oc new-project voting-app

---

### 2. Deploy Core Services

bash
oc apply -f redis.yaml
oc apply -f postgres.yaml
oc apply -f worker.yaml

---

3. Build & Deploy APIs

bash
oc new-build --binary --name=vote
oc start-build vote --from-dir=. --follow

oc new-build --binary --name=results
oc start-build results --from-dir=. --follow

---

### 4. Deploy Nginx

bash
oc apply -f nginx-config.yaml
oc apply -f nginx.yaml
oc apply -f nginx-service.yaml


---

### 5. Expose Application

bash
oc expose svc nginx
oc get route

---

## Usage

1. Open the provided route URL
2. Click **Vote Cats 🐱** or **Vote Dogs 🐶**
3. Watch results update in real time

---

##Troubleshooting Highlights

This project involved solving real-world cloud engineering challenges:

* Fixed **PodSecurity (restricted) violations**
* Resolved **Nginx 502 reverse proxy errors**
* Debugged **Redis persistence (RDB) failures**
* Fixed **Flask container CrashLoopBackOff**
* Corrected **service-to-service routing issues**
* Implemented **retry logic for Redis & PostgreSQL**

---

## Key Learnings

* Designing **event-driven architectures**
* Debugging **Kubernetes networking and services**
* Handling **stateful vs stateless components**
* Working with **OpenShift security constraints**
* Building **resilient microservices**

---

##Future Improvements

* Add CI/CD pipeline (Jenkins / GitHub Actions)
* Integrate security scanning (Prisma Cloud)
* Add health checks and readiness probes
* Add authentication layer
* Deploy using Helm or GitOps

---

## Author

Oluranti Newton Omotayo**
Cloud Security Engineer | CNAPP Specialist


