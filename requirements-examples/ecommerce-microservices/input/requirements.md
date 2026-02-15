# Requirements

## Business requirements

| ID       | Summary                         | Description                                                                                                                                 |
|----------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| BR-001   | Cart microservice scope         | Cart service is responsible for cart functionality: add/remove items, persist cart, and checkout flow.                                      |
| BR-002   | Product microservice scope      | Product service is responsible for product functionality: catalog, product details, and availability.                                     |
| BR-003   | Customer-facing application     | A front-end application for customers to browse products, manage cart, and complete checkout.                                              |
| BR-004   | Admin application               | A front-end application for administrators to manage products, orders, and back-office operations.                                        |
| BR-005   | Budget and throughput            | Budget constraint: **$500/month** to support **1000 requests/min** for Cart and **5000 requests/min** for Product.                         |
| BR-006   | Customer privacy (RGPD/GDPR)    | Personal data must be processed in line with RGPD/GDPR: lawful basis, purpose limitation, data minimization, and respect of data subject rights (access, rectification, erasure, portability, objection). |

## Technical requirements

| ID       | Summary                         | Description                                                                                                                                 |
|----------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| TR-001   | Event-driven architecture       | No direct communication between Cart and Product services; use event-driven architecture (e.g. message broker or event bus).                  |
| TR-002   | Backend technology               | Backend services are implemented in **Spring Boot**.                                                                                        |
| TR-003   | Front-end technology             | Customer-facing and admin applications are **React**-based.                                                                                |
| TR-004   | Security standards compliance    | Architecture must comply with security standards: encryption in transit and at rest, identity and access control, secure configuration.     |
| TR-005   | Scalability                      | Architecture must be scalable and able to handle growth in traffic and data without major redesign.                                        |
| TR-006   | Cost effectiveness               | Architecture must be cost effective and aligned with the defined budget and efficient use of resources.                                   |
| TR-007   | Extensibility                    | Architecture must be easy to extend: straightforward to add new features, services, or integrations.                                      |
| TR-008   | RGPD/GDPR technical compliance   | Technical measures to support RGPD/GDPR: data minimization, retention limits, secure storage and processing, support for erasure and portability, audit trail for personal data processing. |
