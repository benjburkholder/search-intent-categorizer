Modules:

serp-intent-categorizer-static.py ~ This is the SERP intent module that has a static location used when calling the API.
I have it set by default to cleveland,ohio.

serp-intent-categorizer.py ~ This is the SERP intent module that can have a custom set location for calling APi.
Queries placed in 'serp_intent_urls.text' must be in the format: query,city,state. The city and state values are then
stripped and implemented into the location field in query params.