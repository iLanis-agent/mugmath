# Mug Math

Event mug box, week, cost and time arithmetic. The 350 mugs at 24 mugs a box take 15 boxes, the last box holding 14 mugs.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The boxes truth** - the mugs (1 to 1000000) divided by the mugs a box (1 to 1000), rounded up, with what the last box holds.
- **The weeks truth** - the mugs divided by the mugs used a week (1 to 100000), with the mugs left for the next week.
- **The cost truth** - the boxes (1 to 100000) times the box price ($0.01 to $999.99) to the cent, and spread over the mugs, half rounded up.
- **The time truth** - the mugs divided by the mugs printed a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any mug, box or press and does not know whether mugs will really arrive unchipped, a press will jam or a price will hold, and it gives no verdict that a box is worth its price or a mug is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every box recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
