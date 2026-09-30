# SQL Sales and Returns Analysis

**Course foundation:** DAD 220 Projects One and Two, plus the sales and returns activity.

## Question

Where are orders and returns concentrated, and what should a product manager investigate?

## Original work

I created a MySQL database in Codio with related Customers, Orders, and RMA tables, loaded CSV records, used joins and filters, updated records, and exported query results. I analyzed orders and returns by geography and product and wrote a summary for nontechnical stakeholders.

The coursework identified Massachusetts as a leading order location and highlighted products and regions for further review. My final report also noted that return counts alone can be misleading: a popular product may have many returns simply because it sells more.

## Portfolio queries

`analysis.sql` contains readable adaptations of the reporting queries. The last query is a new portfolio extension that calculates returned-order percentages using distinct order IDs.

| Measure | Meaning |
| --- | --- |
| Order count | Number of orders, not number of unique customers |
| Return records | Number of RMA records |
| Share of returns | Product return records divided by all return records |
| Returned-order percentage | Distinct returned orders divided by distinct orders for that product |

## Run

Use the Customers, Orders, and RMA tables described in the SQL file, then execute the queries in a SQL client. The course database and CSV files are not distributed here. Queries were checked on a small synthetic SQLite fixture, including an order with multiple return records, to verify the distinct-order denominator. They have not been rerun against the original MySQL database.

## Limits

Returns are not automatically defects. Incomplete records, reporting periods, product mix, and sales volume affect interpretation. The synthetic validation fixture establishes query behavior, not the original business findings. The original activity contained inconsistent regional interpretations, so this portfolio does not repeat unverified regional rankings.

This SQL was adapted with AI assistance from the documented coursework approach. It is not presented as a verbatim export of the original queries.
