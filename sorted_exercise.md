## Exercise - Sorting Names

We have a [list of attendees for the mini-conference](names.csv) that we want
to run.  To enable our volunteers who will be handing out name cards:

1. Sort the list of attendees in the CSV by last name.
1. Find out how many attendees will be coming.
1. *Bonus* Given 3 volunteers, how can we divide up the names into 3 groups?

### Starter Code

```python
import csv
import operator


with open('names.csv') as names_file:
    data = list(csv.DictReader(names_file))
    ...
```
