# DBMS-PROJECT-26

# RelVeri+

### A Unified SQL-to-SMT Framework for Isolation Anomaly Detection and Verification in Relational Database Systems

## Overview

RelVeri+ is a research-oriented framework proposed as an extension of two recent database isolation analysis systems:

* **IsoRel** – Relational isolation anomaly detection
* **VeriStrong** – Strong isolation verification using Hyper-Polygraphs and SMT solving

The framework combines the strengths of both approaches into a single end-to-end pipeline capable of:

* Extracting dependencies from SQL workloads
* Constructing dependency graphs
* Building Hyper-Polygraphs
* Modeling predicate-based anomalies
* Detecting dependency cycles
* Verifying isolation guarantees using SMT solving
* Explaining detected anomalies

---

# System Architecture

```text
SQL Workload
      |
      v
Dependency Graph Builder
      |
      v
Hyper-Polygraph Constructor
      |
      v
Predicate HyperEdge Generator
      |
      v
Cycle Detection Engine
      |
      v
SMT Verification Engine
      |
      v
Anomaly Explanation Engine
      |
      v
Visualization & Report
```

---

# Repository Structure

```text
RelVeri+
│
├── main.py
├── dependency_graph.py
├── hyperpolygraph.py
├── predicate_edges.py
├── cycle_detection.py
├── smt_verifier.py
├── explanation.py
├── visualization.py
├── sample_history.json
├── requirements.txt
├── README.md
└── docs/
    ├── Project_Report.pdf
    └── Project_Presentation.pptx
```

This structure follows the architecture proposed in the report and separates dependency extraction, verification, and explanation modules.

```
```

# Project Modules

## 1. SQL Workload Manager

### Description

This module serves as the entry point of the framework. It accepts SQL workloads and transaction histories generated from relational database systems.

### Responsibilities

* Read transaction histories
* Parse SQL operations
* Store transaction metadata
* Prepare input for dependency analysis

### Input

```text
SELECT
INSERT
UPDATE
DELETE
```

### Output

```text
Structured transaction history
```

---

## 2. Dependency Graph Builder

### Description

This module constructs the Direct Serialization Graph (DSG) from transaction histories by identifying dependencies among transactions.

### Dependencies Supported

#### Write-Read (WR)

Transaction Tj reads a value written by Ti.

```text
Ti ----WR----> Tj
```

#### Write-Write (WW)

Transaction Tj overwrites a value written by Ti.

```text
Ti ----WW----> Tj
```

#### Read-Write (RW)

Transaction Ti reads a value that is later modified by Tj.

```text
Ti ----RW----> Tj
```

### Output

```text
Dependency Graph
```

---

## 3. Hyper-Polygraph Constructor

### Description

This module converts dependency graphs into Hyper-Polygraphs.

The Hyper-Polygraph extends traditional dependency graphs by supporting uncertainty caused by duplicate values.

### Responsibilities

* Create transaction vertices
* Add known dependency edges
* Create WR constraints
* Create WW constraints
* Build Hyperedge structures

### Output

```text
Hyper-Polygraph
```

---

## 4. Predicate HyperEdge Generator

### Description

This is the primary extension introduced by RelVeri+.

Existing dependency graphs cannot explicitly represent predicate-based interactions.

RelVeri+ introduces:

```text
Predicate HyperEdge (PH)
```

### Example

```sql
SELECT *
FROM Employee
WHERE Salary > 50000;
```

If another transaction inserts:

```sql
Salary = 60000
```

then:

```text
T1 ----PH----> T2
```

### Benefits

* Phantom Read Detection
* Predicate Conflict Detection
* Range Query Analysis

### Output

```text
Predicate HyperEdges
```

---

## 5. Cycle Detection Engine

### Description

This module searches for cycles in dependency graphs and Hyper-Polygraphs.

A cycle indicates a potential isolation anomaly.

### Techniques Used

#### Tarjan SCC Algorithm

Used for strongly connected component detection.

#### 1-Width Cycle Detection

Detects cycles that always exist regardless of hyperedge choices.

#### 2-Width Cycle Detection

Detects cycles requiring only two hyperedge selections.

### Output

```text
Dependency Cycles
```

---

## 6. SMT Verification Engine

### Description

This module formally verifies whether a transaction history satisfies a target isolation level.

### Technology

* Z3 SMT Solver

### Verification Targets

* Snapshot Isolation (SI)
* Serializable Isolation (SER)

### Process

```text
Hyper-Polygraph
      |
      v
SMT Encoding
      |
      v
Z3 Solver
      |
      v
SAT / UNSAT
```

### Output

```text
Serializable
or
Isolation Violation
```

---

## 7. Anomaly Explanation Engine

### Description

Provides human-readable explanations for detected anomalies.

### Example

```text
Anomaly Type:
Write Skew

Transactions:
T12, T17

Cycle:
T12 --RW--> T17
T17 --RW--> T12
```

### Benefits

* Easier debugging
* Better understanding of violations
* Developer-friendly diagnostics

---

## 8. Visualization and Reporting Module

### Description

Generates visual representations of verification results.

### Features

* Dependency Graph Visualization
* Hyper-Polygraph Visualization
* Cycle Highlighting
* Verification Summary Reports

### Output

```text
Graphs
Reports
Charts
```

---

## 9. RelVeri+ Controller

### Description

Main coordinator module of the framework.

It manages the complete SQL-to-SMT verification workflow.

### Workflow

```text
SQL Workload
      |
      v
Dependency Graph Builder
      |
      v
Hyper-Polygraph Constructor
      |
      v
Predicate HyperEdge Generator
      |
      v
Cycle Detection
      |
      v
SMT Verification
      |
      v
Explanation Engine
      |
      v
Final Report
```

---

# Technologies Used

* Python 3
* NetworkX
* Z3 Solver
* Graph Algorithms
* SMT Verification

---

# Research Contribution

RelVeri+ combines IsoRel's relational dependency extraction with VeriStrong's Hyper-Polygraph verification and extends both approaches through Predicate HyperEdges and automated anomaly explanation.

The framework provides a unified SQL-to-SMT pipeline capable of detecting, explaining, and verifying isolation anomalies in relational database systems.

---

# Future Work

* PostgreSQL Integration
* MySQL Integration
* Distributed Database Support
* Real-Time Verification
* Machine Learning Based Anomaly Prediction
* Cloud-Native Deployment

---

# Authors

Project based on the study of:

* IsoRel
* VeriStrong

Developed as part of the DBMS Project (2026).
