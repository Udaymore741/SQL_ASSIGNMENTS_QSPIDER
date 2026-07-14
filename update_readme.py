"""
Auto README updater for SQL Assignments repo.
Scans all .txt files, extracts SQL keywords used,
and regenerates README.md with an updated TOC and assignment list.
"""

import os
import re

# ── File metadata ────────────────────────────────────────────────────────────
# Maps filename → (display title, short description, bullet points)
# When a new file is added that isn't in this map, a generic entry is created.
FILE_META = {
    "ASSIGNMENT 4_WHERE_CLAUSE_2.txt": (
        "WHERE Clause",
        "Filtering records using the `WHERE` clause with `AND` / `OR` operators.",
        [
            "Filter by job, salary, department, and hire date",
            "Combine multiple conditions using `AND` and `OR`",
            "Compare dates using `<`, `>`, `>=`, `<=`",
        ],
    ),
    "ASSIGNMENT4_CONCATATION.txt": (
        "Concatenation",
        "String concatenation using the `||` operator.",
        [
            "Build custom messages using employee data",
            "Perform arithmetic inside concatenated strings (annual salary, hike, half-term salary)",
            "Examples: salary deduction messages, designation displays, manager ID lookups",
        ],
    ),
    "BETWEEN_ASSIGNMENT.txt": (
        "BETWEEN Operator",
        "Range filtering using `BETWEEN` and `NOT BETWEEN`.",
        [
            "Filter hire dates within a date range",
            "Use `NOT BETWEEN` on numeric and string columns",
            "Combine `BETWEEN` with `IN` and salary conditions",
        ],
    ),
    "IN_ASSIGNMENT.txt": (
        "IN Operator",
        "List-based filtering using `IN` and `NOT IN`.",
        [
            "Filter by department, job, salary, commission, and manager ID",
            "Use `NOT IN` to exclude specific values",
            "Combine `IN` with computed columns like `SAL * 12`",
        ],
    ),
    "LIKE_ASSIGNMRNT.txt": (
        "LIKE Operator",
        "Pattern matching using the `LIKE` operator.",
        [
            "Wildcards: `%` (any characters), `_` (single character)",
            "Match names starting with, ending with, or containing specific letters",
            "Filter by hire date pattern (`%81`, `%82`)",
            "Combine `LIKE` with `IN` and salary filters",
        ],
    ),
    "LIKE_IN_BETWEEN.txt": (
        "LIKE + IN + BETWEEN",
        "Combined practice of `LIKE`, `IN`, and `BETWEEN` in a single session.",
        [
            "All three operators used together in complex queries",
            "Mix of date ranges, job lists, and name patterns",
            "Compute annual salary (`SAL * 12`) with multiple filters",
        ],
    ),
    "ORDER_BY_CLAUSE.txt": (
        "ORDER BY Clause",
        "Sorting results using `ORDER BY`.",
        [
            "Sort by salary, name, and computed columns (`ASC` / `DESC`)",
            "Use aliases in `ORDER BY`",
            "Apply `DISTINCT` with ordering",
            "Percentage-based salary calculations with sorting (35% hike, 49% deduction, 32% half-term)",
        ],
    ),
    "GROUP_BY.txt": (
        "GROUP BY Clause",
        "Aggregating data using `GROUP BY` with aggregate functions.",
        [
            "Functions used: `COUNT(*)`, `SUM(SAL)`, `AVG(SAL)`, `MIN(SAL)`, `MAX(SAL)`",
            "Group by department, job, and salary",
            "Combine `WHERE` filters before grouping",
            "Use `HAVING` to filter grouped results",
        ],
    ),
    "HAVING_CLAUSE.txt": (
        "HAVING Clause",
        "Post-aggregation filtering using `HAVING`.",
        [
            "Filter groups by `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`",
            "Find duplicate salary/hire date values",
            "Combine `WHERE` (row filter) with `HAVING` (group filter)",
        ],
    ),
    "SUB_QUERIES_CASE_1.txt": (
        "Subqueries - Case 1",
        "Introduction to subqueries (nested SELECT statements) - Case 1.",
        [
            "Single-row subqueries using comparison operators",
            "Using subquery results in `WHERE` clause filters",
            "Nesting queries to find employees based on dynamic conditions (e.g. same job, same dept, higher salary)",
        ],
    ),
    "MOCK_TEST.txt": (
        "Mock Test",
        "Mock test with mixed SQL concepts.",
        [
            "Complex multi-condition `WHERE` clauses",
            "Arithmetic expressions in filters (`SAL * 6`, `SAL * 12`)",
            "Combining `AND`, `OR`, `LIKE`, `IN`, comparison operators",
            "Score: **5.5 / 10**",
        ],
    ),
}

# Fixed order for known files (unknown new files are appended after)
FILE_ORDER = list(FILE_META.keys())

# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text):
    """Convert a heading text to a GitHub markdown anchor slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text.strip())
    return text


def get_txt_files():
    """Return sorted list of .txt files in repo root."""
    files = [f for f in os.listdir('.') if f.endswith('.txt')]
    # Sort: known files in defined order, unknown files appended alphabetically
    known = [f for f in FILE_ORDER if f in files]
    unknown = sorted([f for f in files if f not in FILE_ORDER])
    return known + unknown


def infer_meta(filename):
    """Generate generic metadata for an unknown file."""
    name = os.path.splitext(filename)[0]
    title = name.replace('_', ' ').title()
    return (
        title,
        f"SQL practice queries — `{filename}`.",
        ["Queries and results from SQL*Plus session"],
    )


def make_anchor(index, title):
    """Build the TOC anchor link matching GitHub's heading slug format."""
    heading = f"{index}. {title}"
    slug = slugify(heading)
    return f"[{index}. {title}](#{slug})"


# ── README builder ────────────────────────────────────────────────────────────

def build_readme(files):
    txt_files = files

    # ── Static header ────────────────────────────────────────────────────────
    header = """\
# SQL Assignments - QSpider

Oracle SQL practice assignments using the classic `EMP` table. Each file contains SQL queries executed in SQL*Plus, including errors encountered and their corrections."""

    # ── Table of Contents ────────────────────────────────────────────────────
    toc_lines = ["## Table of Contents\n"]
    toc_lines.append("- [EMP Table Structure](#emp-table-structure)")
    toc_lines.append("- [Assignment Files](#assignment-files)")

    assignment_entries = []
    for i, fname in enumerate(txt_files, start=1):
        meta = FILE_META.get(fname) or infer_meta(fname)
        title, desc, bullets = meta
        anchor = make_anchor(i, title)
        toc_lines.append(f"  - {anchor}")
        assignment_entries.append((i, fname, title, desc, bullets))

    toc_lines.append("- [Key Concepts Covered](#key-concepts-covered)")
    toc = "\n".join(toc_lines)

    # ── EMP Table ────────────────────────────────────────────────────────────
    emp_table = """\
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
| DEPTNO   | Department number (10, 20, or 30)  |"""

    # ── Assignment sections ───────────────────────────────────────────────────
    sections = ["## Assignment Files\n"]
    for i, fname, title, desc, bullets in assignment_entries:
        section = f"### {i}. `{fname}`\n{desc}\n"
        section += "\n".join(f"- {b}" for b in bullets)
        sections.append(section)
    assignments_block = "\n\n".join(sections)

    # ── Key Concepts ─────────────────────────────────────────────────────────
    key_concepts = """\
## Key Concepts Covered

- `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`
- `AND`, `OR`, `NOT` logical operators
- `BETWEEN`, `IN`, `LIKE` operators
- String concatenation with `||`
- Aggregate functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- Subqueries (nested `SELECT` statements)
- Arithmetic expressions and column aliases
- Common SQL errors and their fixes (typos, missing keywords, invalid identifiers)"""

    # ── Assemble ──────────────────────────────────────────────────────────────
    readme = "\n\n---\n\n".join([
        header.strip(),
        toc,
        emp_table,
        assignments_block,
        key_concepts,
    ])

    return readme + "\n"


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    files = get_txt_files()
    content = build_readme(files)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README.md updated with {len(files)} assignment file(s):")
    for i, f in enumerate(files, 1):
        print(f"  {i}. {f}")
