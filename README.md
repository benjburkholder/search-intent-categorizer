**Requirements:**
Purchase SERPApi Key~ https://serpapi.com/

**Modules:**

serp-intent-categorizer-static.py ~ This is the SERP intent module that has a static location used when calling the API.
I have it set by default to cleveland,ohio.

serp-intent-categorizer.py ~ This is the SERP intent module that can have a custom set location for calling APi.
Queries placed in 'serp_intent_urls.text' must be in the format: query,city,state. The city and state values are then
stripped and implemented into the location field in query params.

----------------------------------

**Program Summary:**
These scripts read a list of queries from a TXT file, depending on which module you choose above will determine how you
structure the queries to run. 

The API is called with the query, then the SERP is analyzed in a variation of combinations, each corresponding with a
different type of search intent. 

Just for quick context, "Search Intent" simply means what stage in the buying process a user is at with the given query.
Based upon the SERP features present for a given query, a label is assigned to the query.

Results of script run are collected in CSV. 