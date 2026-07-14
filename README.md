# SQL Assignments - QSpider

Oracle SQL practice assignments using the classic `EMP` table. Each file contains SQL queries executed in SQL*Plus, including errors encountered and their corrections.

---

## Table of Contents

- [EMP Table Structure](#emp-table-structure)
- [Assignment Files](#assignment-files)
  - [1. WHERE Clause](#1-where-clause)
  - [2. Concatenation](#2-concatenation)
  - [3. BETWEEN Operator](#3-between-operator)
  - [4. IN Operator](#4-in-operator)
  - [5. LIKE Operator](#5-like-operator)
  - [6. LIKE + IN + BETWEEN](#6-like-in-between)
  - [7. ORDER BY Clause](#7-order-by-clause)
  - [8. GROUP BY Clause](#8-group-by-clause)
  - [9. HAVING Clause](#9-having-clause)
  - [10. Subqueries - Case 1](#10-subqueries---case-1)
  - [11. Mock Test](#11-mock-test)
  - [12. Emp Mgr Releationship](#12-emp-mgr-releationship)
  - [13. Sub Queries Case 2](#13-sub-queries-case-2)
- [Key Concepts Covered](#key-concepts-covered)

---

## EMP Table Structure

| Column   | Description                        |
|----------|------------------------------------|
| EMPNO    | Employee number                    |
| ENAME    | Employee name                      |
| JOB      | Job designation                    |
| MGR      | Manager's employee number          |
| HIREDATE | Date of hiring                     |
| SAL      | Salary                             |
| COMM     | Commission                         |
| DEPTNO   | Department number (10, 20, or 30)  |

---

## Assignment Files


### 1. `ASSIGNMENT 4_WHERE_CLAUSE_2.txt`
Filtering records using the `WHERE` clause with `AND` / `OR` operators.
- Filter by job, salary, department, and hire date
- Combine multiple conditions using `AND` and `OR`
- Compare dates using `<`, `>`, `>=`, `<=`

### 2. `ASSIGNMENT4_CONCATATION.txt`
String concatenation using the `||` operator.
- Build custom messages using employee data
- Perform arithmetic inside concatenated strings (annual salary, hike, half-term salary)
- Examples: salary deduction messages, designation displays, manager ID lookups

### 3. `BETWEEN_ASSIGNMENT.txt`
Range filtering using `BETWEEN` and `NOT BETWEEN`.
- Filter hire dates within a date range
- Use `NOT BETWEEN` on numeric and string columns
- Combine `BETWEEN` with `IN` and salary conditions

### 4. `IN_ASSIGNMENT.txt`
List-based filtering using `IN` and `NOT IN`.
- Filter by department, job, salary, commission, and manager ID
- Use `NOT IN` to exclude specific values
- Combine `IN` with computed columns like `SAL * 12`

### 5. `LIKE_ASSIGNMRNT.txt`
Pattern matching using the `LIKE` operator.
- Wildcards: `%` (any characters), `_` (single character)
- Match names starting with, ending with, or containing specific letters
- Filter by hire date pattern (`%81`, `%82`)
- Combine `LIKE` with `IN` and salary filters

### 6. `LIKE_IN_BETWEEN.txt`
Combined practice of `LIKE`, `IN`, and `BETWEEN` in a single session.
- All three operators used together in complex queries
- Mix of date ranges, job lists, and name patterns
- Compute annual salary (`SAL * 12`) with multiple filters

### 7. `ORDER_BY_CLAUSE.txt`
Sorting results using `ORDER BY`.
- Sort by salary, name, and computed columns (`ASC` / `DESC`)
- Use aliases in `ORDER BY`
- Apply `DISTINCT` with ordering
- Percentage-based salary calculations with sorting (35% hike, 49% deduction, 32% half-term)

### 8. `GROUP_BY.txt`
Aggregating data using `GROUP BY` with aggregate functions.
- Functions used: `COUNT(*)`, `SUM(SAL)`, `AVG(SAL)`, `MIN(SAL)`, `MAX(SAL)`
- Group by department, job, and salary
- Combine `WHERE` filters before grouping
- Use `HAVING` to filter grouped results

### 9. `HAVING_CLAUSE.txt`
Post-aggregation filtering using `HAVING`.
- Filter groups by `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`
- Find duplicate salary/hire date values
- Combine `WHERE` (row filter) with `HAVING` (group filter)

### 10. `SUB_QUERIES_CASE_1.txt`
Introduction to subqueries (nested SELECT statements) - Case 1.
- Single-row subqueries using comparison operators
- Using subquery results in `WHERE` clause filters
- Nesting queries to find employees based on dynamic conditions (e.g. same job, same dept, higher salary)

### 11. `MOCK_TEST.txt`
Mock test with mixed SQL concepts.
- Complex multi-condition `WHERE` clauses
- Arithmetic expressions in filters (`SAL * 6`, `SAL * 12`)
- Combining `AND`, `OR`, `LIKE`, `IN`, comparison operators
- Score: **5.5 / 10**

### 12. `EMP_MGR_RELEATIONSHIP.txt`
SQL practice queries — `EMP_MGR_RELEATIONSHIP.txt`.
- Queries and results from SQL*Plus session

### 13. `SUB_QUERIES_CASE_2.txt`
SQL practice queries — `SUB_QUERIES_CASE_2.txt`.
- Queries and results from SQL*Plus session

---

## Key Concepts Covered

- `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`
- `AND`, `OR`, `NOT` logical operators
- `BETWEEN`, `IN`, `LIKE` operators
- String concatenation with `||`
- Aggregate functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- Subqueries (nested `SELECT` statements)
- Arithmetic expressions and column aliases
- Common SQL errors and their fixes (typos, missing keywords, invalid identifiers)
